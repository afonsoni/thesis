"""
Metadata-filtered vector search must return the true top-k, not a truncated list.

pgvector applies a WHERE clause *after* the HNSW scan: with the default
``hnsw.ef_search`` of 40 and a party filter matching ~1/8 of the rows, an HNSW
plan hands back 3 rows for a LIMIT 30 (measured; the reranker's candidate count).
At this corpus size Postgres instead plans the party B-tree plus an exact sort,
so the result is exact. This test pins that down on a table shaped like the real
one (2815 chunks, the real per-party sizes, 1024-dim vectors); if growth or a
pgvector upgrade flips the plan to HNSW, it fails here instead of silently
starving retrieval.
"""

import os
import uuid

import numpy as np
import pytest

from src.rag.common.models import EmbeddedChunk
from src.rag.indexing.store import VectorStore

# Chunks per party in the indexed corpus (SELECT party_name, count(*) ...).
PARTY_SIZES = {
    "Aliança Democrática": 383,
    "Bloco de Esquerda": 448,
    "CHEGA": 358,
    "Iniciativa Liberal": 442,
    "LIVRE": 366,
    "Partido Comunista Português": 306,
    "Partido Socialista": 333,
    "Pessoas-Animais-Natureza": 179,
}
TOPICS = ["saude", "educacao", "habitacao", "economia", "ambiente", "justica"]
DIM = 1024
TOP_K = 30  # rerank_candidates: the widest filtered fetch retrieval makes


@pytest.fixture(scope="module")
def corpus_store():
    store = VectorStore(db_config={
        "host": os.getenv("RAG_TEST_DB_HOST", "localhost"),
        "port": int(os.getenv("RAG_TEST_DB_PORT", "5433")),
        "database": os.getenv("RAG_TEST_DB_NAME", "ragdb_test"),
        "user": os.getenv("RAG_TEST_DB_USER", "postgres"),
        "password": os.getenv("RAG_TEST_DB_PASSWORD", "postgres"),
    })
    store.table = f"party_programs_filter_{uuid.uuid4().hex[:8]}"
    store.connect()  # raises if the test DB is down: docker compose up -d postgres_test
    store.create_table(embedding_dim=DIM)

    rng = np.random.default_rng(0)
    rows = []
    for party, n in PARTY_SIZES.items():
        vecs = rng.standard_normal((n, DIM)).astype(np.float32)
        vecs /= np.linalg.norm(vecs, axis=1, keepdims=True)
        for v in vecs:
            topics = list(rng.choice(TOPICS, size=int(rng.integers(1, 3)), replace=False))
            rows.append((party, topics, v))
    store.insert_chunks([
        EmbeddedChunk(content=f"chunk {i}", embedding=v.tolist(), party_name=p, topics=t)
        for i, (p, t, v) in enumerate(rows)
    ])
    cur = store._conn().cursor()
    cur.execute(f"ANALYZE {store.table};")
    store._conn().commit()

    try:
        yield store, rows
    finally:
        store.drop_table()
        store.close()


def _exact_top_k(rows, query, party, topic=None):
    """Brute-force cosine top-k over the rows the filter allows, as content ids."""
    hits = [
        (float(v @ query), f"chunk {i}")
        for i, (p, t, v) in enumerate(rows)
        if p == party and (topic is None or topic in t)
    ]
    return [cid for _, cid in sorted(hits, reverse=True)[:TOP_K]]


@pytest.mark.parametrize("party", list(PARTY_SIZES))
def test_party_filter_returns_exact_top_k(corpus_store, party):
    store, rows = corpus_store
    query = np.random.default_rng(1).standard_normal(DIM).astype(np.float32)
    query /= np.linalg.norm(query)

    got = [r.content for r in store.similarity_search(query.tolist(), top_k=TOP_K, party_name=party)]

    assert got == _exact_top_k(rows, query, party)


def test_party_and_topic_filter_returns_exact_top_k(corpus_store):
    """The router's other filter: topics overlap, on top of party (fewer than k may exist)."""
    store, rows = corpus_store
    query = np.random.default_rng(2).standard_normal(DIM).astype(np.float32)
    query /= np.linalg.norm(query)
    party = "Pessoas-Animais-Natureza"  # smallest party: the most selective combination

    got = [
        r.content
        for r in store.similarity_search(query.tolist(), top_k=TOP_K, party_name=party, topics=["saude"])
    ]

    assert got == _exact_top_k(rows, query, party, topic="saude")
