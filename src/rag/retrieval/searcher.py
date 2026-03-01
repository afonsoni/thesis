"""
Search interface wrapping pgvector similarity queries.

Supports:
- single-query search with metadata filters
- multi-query search with Reciprocal Rank Fusion (RRF, Part 6 pattern)
- parallel per-party search for comparison queries
"""

import logging
from collections import defaultdict
from typing import Dict, List, Optional

from src.rag.common.models import SearchResult
from src.rag.indexing.embedder import Embedder
from src.rag.indexing.store import VectorStore

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
        out.append(sr)
    return out


# ---------------------------------------------------------------------------
# Searcher class
# ---------------------------------------------------------------------------

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

    # ------------------------------------------------------------------
    # Single-query search
    # ------------------------------------------------------------------

    def search(
        self,
        query: str,
        top_k: int = 5,
        party_name: Optional[str] = None,
        ideology: Optional[str] = None,
        topics: Optional[List[str]] = None,
        year: Optional[int] = None,
    ) -> List[SearchResult]:
        """Embed query and run similarity search with optional filters."""
        vec = self.embedder.encode(query)
        return self.store.similarity_search(
            query_embedding=vec,
            top_k=top_k,
            party_name=party_name,
            ideology=ideology,
            topics=topics,
            year=year,
        )

    # ------------------------------------------------------------------
    # Multi-query search with RRF (Part 5 + Part 6)
    # ------------------------------------------------------------------

    def multi_query_search(
        self,
        queries: List[str],
        top_k: int = 5,
        party_name: Optional[str] = None,
        ideology: Optional[str] = None,
        topics: Optional[List[str]] = None,
        year: Optional[int] = None,
        rrf_k: int = 60,
    ) -> List[SearchResult]:
        """
        Run each query independently, then fuse with RRF.

        Each sub-query retrieves *top_k* results; the final fused list
        is trimmed back to *top_k*.
        """
        all_lists: List[List[SearchResult]] = []
        for q in queries:
            results = self.search(
                q, top_k=top_k,
                party_name=party_name, ideology=ideology,
                topics=topics, year=year,
            )
            all_lists.append(results)

        fused = reciprocal_rank_fusion(all_lists, k=rrf_k)
        logger.info(
            "Multi-query search: %d queries → %d unique results (returning top %d).",
            len(queries), len(fused), top_k,
        )
        return fused[:top_k]

    # ------------------------------------------------------------------
    # Per-party batch search (for comparison queries)
    # ------------------------------------------------------------------

    def batch_search_by_party(
        self,
        query: str,
        parties: List[str],
        top_k_per_party: int = 3,
        topics: Optional[List[str]] = None,
    ) -> Dict[str, List[SearchResult]]:
        """
        Run a separate search for each party and return grouped results.
        """
        results: Dict[str, List[SearchResult]] = {}
        for party in parties:
            results[party] = self.search(
                query,
                top_k=top_k_per_party,
                party_name=party,
                topics=topics,
            )
        return results

    def multi_query_batch_search_by_party(
        self,
        queries: List[str],
        parties: List[str],
        top_k_per_party: int = 3,
        topics: Optional[List[str]] = None,
        rrf_k: int = 60,
    ) -> Dict[str, List[SearchResult]]:
        """
        Multi-query + per-party search: run multiple queries for each party,
        fuse with RRF per party, return grouped results.
        """
        grouped: Dict[str, List[SearchResult]] = {}
        for party in parties:
            all_lists: List[List[SearchResult]] = []
            for q in queries:
                results = self.search(
                    q, top_k=top_k_per_party,
                    party_name=party, topics=topics,
                )
                all_lists.append(results)
            fused = reciprocal_rank_fusion(all_lists, k=rrf_k)
            grouped[party] = fused[:top_k_per_party]
        return grouped
