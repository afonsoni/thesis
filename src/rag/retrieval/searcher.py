"""
Search over the vector store: dense search per query, Reciprocal Rank Fusion
(RRF, Part 6) across queries and modalities, and optional cross-encoder reranking.
"""

import logging
from typing import Dict, List, Optional

from src.rag.common.models import ScoreType, SearchResult
from src.rag.indexing.embedder import Embedder
from src.rag.indexing.store import VectorStore
from src.rag.retrieval.config import RetrievalConfig
from src.rag.retrieval.query_analyzer import strip_party_mentions

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Reciprocal Rank Fusion (from RAG-Fusion, Part 6)
# ---------------------------------------------------------------------------

def reciprocal_rank_fusion(
    result_lists: List[List[SearchResult]],
    k: int = 60,
) -> List[SearchResult]:
    """
    Fuse multiple ranked result lists using RRF.

    score(d) = Σ_q  1 / (k + rank_q(d))

    Returns results ordered by descending fused score.  The ``similarity``
    field of each returned ``SearchResult`` is replaced with the RRF score.
    """
    fused_scores: Dict[str, float] = {}
    doc_map: Dict[str, SearchResult] = {}

    for results in result_lists:
        for rank, sr in enumerate(results):
            key = sr.id
            if key not in doc_map:
                doc_map[key] = sr
                fused_scores[key] = 0.0
            fused_scores[key] += 1.0 / (k + rank)

    ranked = sorted(fused_scores.items(), key=lambda x: x[1], reverse=True)
    out: List[SearchResult] = []
    for doc_id, score in ranked:
        sr = doc_map[doc_id].model_copy()
        sr.similarity = score
        sr.score_type = ScoreType.RRF
        out.append(sr)
    return out


class Searcher:
    """High-level search interface used by the retrieval router."""

    def __init__(
        self,
        embedder: Optional[Embedder] = None,
        store: Optional[VectorStore] = None,
    ):
        self.embedder = embedder or Embedder()
        self.store = store or VectorStore()
        self.store.connect()

    def close(self):
        self.store.close()

    def search(
        self,
        query: str,
        top_k: int = 5,
        party_name: Optional[str] = None,
        topics: Optional[List[str]] = None,
        instruction: Optional[str] = None,
    ) -> List[SearchResult]:
        """Dense search for one query (encoded with the model's query prompt, or
        *instruction* in its place)."""
        vec = self.embedder.encode_query(query, instruction=instruction)
        return self.store.similarity_search(query_embedding=vec, top_k=top_k, party_name=party_name, topics=topics)

    def multi_query_search(
        self,
        queries: List[str],
        config: RetrievalConfig,
        top_k: int,
        rerank_query: str,
        party_name: Optional[str] = None,
        topics: Optional[List[str]] = None,
    ) -> List[SearchResult]:
        """Run each query, fuse the ranked lists with RRF, and return the best *top_k*.

        With ``config.use_hybrid`` each query also contributes a BM25 list, and
        dense and lexical lists are fused in a *single* RRF pass, so every list
        weighs the same.

        With a party filter the party name is redundant in the query: the lexical
        query always drops it (as a rare term it would outweigh the topic), the
        dense one only under ``config.strip_party_names``.

        With ``config.use_reranker`` every sub-query fetches
        ``rerank_candidates`` instead of *top_k*, and a cross-encoder re-orders
        that shortlist against *rerank_query* (the user's original question)
        before the trim. A reranker can only promote what retrieval surfaced, so
        reranking exactly *top_k* items could never improve what is in them.
        """
        fetch_k = max(top_k, config.rerank_candidates) if config.use_reranker else top_k

        all_lists: List[List[SearchResult]] = []
        for q in queries:
            stripped = strip_party_mentions(q) if party_name else q
            dense_q = stripped if config.strip_party_names else q
            all_lists.append(self.search(
                dense_q, top_k=fetch_k, party_name=party_name, topics=topics,
                instruction=config.query_instruction,
            ))
            if config.use_hybrid:
                all_lists.append(
                    self.store.lexical_search(stripped, top_k=fetch_k, party_name=party_name,
                                              topics=topics if config.lexical_topic_filter else None)
                )

        # One ranked list (single query, dense only) is already in order; fusing
        # it would only swap cosine scores for rank-derived ones.
        fused = reciprocal_rank_fusion(all_lists, k=config.rrf_k) if len(all_lists) > 1 else all_lists[0]
        logger.info(
            "Multi-query search: %d queries → %d ranked lists → %d unique results "
            "(hybrid=%s, rerank=%s, returning top %d).",
            len(queries), len(all_lists), len(fused), config.use_hybrid, config.use_reranker, top_k,
        )

        if config.use_reranker and fused:
            from src.rag.retrieval.reranker import get_reranker

            return get_reranker().rerank(rerank_query, fused[: config.rerank_candidates], top_k=top_k)
        return fused[:top_k]
