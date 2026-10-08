import os
import sys
import uuid
from pathlib import Path
from typing import Iterator

import psycopg2
import pytest
from dotenv import load_dotenv

from src.rag.common.models import EmbeddedChunk
from src.rag.indexing.embedder import Embedder
from src.rag.indexing.store import VectorStore
from src.rag.retrieval.searcher import Searcher

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

load_dotenv(PROJECT_ROOT / ".env")

class DeterministicEmbedder(Embedder):
    """Small deterministic embedder for DB-backed integration tests."""

    def __init__(self):
        # Avoid loading the real sentence-transformer model in tests.
        self.dimension = 3

    def encode(self, text: str) -> list[float]:
        lower = text.lower()
        if any(token in lower for token in ("educ", "ensino", "escola")):
            return [1.0, 0.0, 0.0]
        if any(token in lower for token in ("saude", "sns", "hospital")):
            return [0.0, 1.0, 0.0]
        return [0.0, 0.0, 1.0]

    # Symmetric by design: no instruction prompts, so queries and documents
    # encode identically (the real method needs the model this __init__ skips).
    def encode_query(self, text: str, instruction=None) -> list[float]:
        return self.encode(text)


@pytest.fixture
def require_live_e2e() -> None:
    """Fail fast when live E2E prerequisites are missing."""
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENROUTER_API_KEY is required for live E2E tests. "
            "Set it in your environment or .env file."
        )


@pytest.fixture
def test_db_config() -> dict:
    """DB config for a dedicated testing instance."""
    return {
        "host": os.getenv("RAG_TEST_DB_HOST", "localhost"),
        "port": int(os.getenv("RAG_TEST_DB_PORT", "5433")),
        "database": os.getenv("RAG_TEST_DB_NAME", "ragdb_test"),
        "user": os.getenv("RAG_TEST_DB_USER", "postgres"),
        "password": os.getenv("RAG_TEST_DB_PASSWORD", "postgres"),
    }


@pytest.fixture
def test_vector_store(test_db_config: dict) -> Iterator[VectorStore]:
    """Create and tear down an isolated pgvector table for each test."""
    table_name = f"party_programs_test_{uuid.uuid4().hex[:8]}"
    store = VectorStore(db_config=test_db_config)
    store.table = table_name
    try:
        store.connect()
    except psycopg2.OperationalError as exc:
        raise RuntimeError(
            "Could not connect to dedicated test PostgreSQL instance. "
            "Start it with: docker compose up -d postgres_test"
        ) from exc
    store.create_table(embedding_dim=3)

    try:
        yield store
    finally:
        try:
            store.drop_table()
        except Exception:
            pass
        store.close()


@pytest.fixture
def seeded_test_store(test_vector_store: VectorStore) -> VectorStore:
    """Populate the test table with deterministic chunk vectors."""
    chunks = [
        EmbeddedChunk(
            content="O Partido Socialista reforca o investimento em educacao publica.",
            embedding=[1.0, 0.0, 0.0],
            party_name="Partido Socialista",
            ideology="left",
            topics=["educacao"],
            metadata={"Major_Section": "Educacao"},
        ),
        EmbeddedChunk(
            content="A Alianca Democratica propoe novos incentivos para escolas tecnicas.",
            embedding=[1.0, 0.0, 0.0],
            party_name="Aliança Democrática",
            ideology="right",
            topics=["educacao"],
            metadata={"Major_Section": "Educacao"},
        ),
        EmbeddedChunk(
            content="O Partido Socialista defende reforco do SNS e contratacao de medicos.",
            embedding=[0.0, 1.0, 0.0],
            party_name="Partido Socialista",
            ideology="left",
            topics=["saude"],
            metadata={"Major_Section": "Saude"},
        ),
        EmbeddedChunk(
            content="A Alianca Democratica apresenta medidas para modernizar hospitais.",
            embedding=[0.0, 1.0, 0.0],
            party_name="Aliança Democrática",
            ideology="right",
            topics=["saude"],
            metadata={"Major_Section": "Saude"},
        ),
    ]
    inserted = test_vector_store.insert_chunks(chunks)
    assert inserted == len(chunks)
    return test_vector_store


@pytest.fixture
def seeded_searcher(seeded_test_store: VectorStore) -> Iterator[Searcher]:
    """Searcher wired to real pgvector storage with deterministic embeddings."""
    searcher = Searcher(embedder=DeterministicEmbedder(), store=seeded_test_store)
    try:
        yield searcher
    finally:
        searcher.close()
