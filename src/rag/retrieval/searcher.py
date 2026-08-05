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

from src.rag.common.models import ScoreType, SearchResult
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
        sr.score_type = ScoreType.RRF
        out.append(sr)
    return out


def merge_preserve_order(result_lists: List[List[SearchResult]]) -> List[SearchResult]:
    """Flatten ranked lists into a single list, de-duplicating by id and
    keeping the first occurrence order.

    Used as the no-RRF fusion path (e.g. the naive baseline), where results are
    simply concatenated rather than rank-fused.
    """
    seen: set = set()
    out: List[SearchResult] = []
    for results in result_lists:
        for sr in results:
            if sr.id in seen:
                continue
            seen.add(sr.id)
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
        # encode_query, not encode: asymmetric retrieval models prefix queries with
        # an instruction and leave documents bare.
        vec = self.embedder.encode_query(query)
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
        use_rrf: bool = True,
        use_hybrid: bool = False,
    ) -> List[SearchResult]:
        """
        Run each query independently, then fuse the ranked lists.

        Each sub-query retrieves *top_k* results; the final list is trimmed back
        to *top_k*. When ``use_rrf`` is True the lists are fused with Reciprocal
        Rank Fusion; otherwise they are merged by first-occurrence order (the
        naive-baseline path).

        When ``use_hybrid`` is True each query also contributes a Portuguese
        full-text ranked list, and dense plus lexical lists are fused together in
        a *single* RRF pass. Fusing once over all ``2 * len(queries)`` lists —
        rather than fusing each modality and then fusing the fusions — keeps
        every list's contribution weighted equally and the result interpretable.
        """
        all_lists: List[List[SearchResult]] = []
        for q in queries:
            all_lists.append(
                self.search(
                    q, top_k=top_k,
                    party_name=party_name, ideology=ideology,
                    topics=topics, year=year,
                )
            )
            if use_hybrid:
                all_lists.append(
                    self.store.lexical_search(
                        q, top_k=top_k,
                        party_name=party_name, ideology=ideology,
                        topics=topics, year=year,
                    )
                )

        fused = (
            reciprocal_rank_fusion(all_lists, k=rrf_k)
            if use_rrf
            else merge_preserve_order(all_lists)
        )
        logger.info(
            "Multi-query search: %d queries → %d ranked lists → %d unique results "
            "(hybrid=%s, rrf=%s, returning top %d).",
            len(queries), len(all_lists), len(fused), use_hybrid, use_rrf, top_k,
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
        use_rrf: bool = True,
        use_hybrid: bool = False,
    ) -> Dict[str, List[SearchResult]]:
        """
        Multi-query + per-party search: run multiple queries for each party,
        fuse per party, return grouped results.

        Each party is an independent ``multi_query_search`` constrained by a
        ``party_name`` filter, so fusion happens *within* a party and the same
        number of slots is contested for every one of them.
        """
        return {
            party: self.multi_query_search(
                queries,
                top_k=top_k_per_party,
                party_name=party,
                topics=topics,
                rrf_k=rrf_k,
                use_rrf=use_rrf,
                use_hybrid=use_hybrid,
            )
            for party in parties
        }
