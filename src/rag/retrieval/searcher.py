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
        topics: Optional[List[str]] = None,
        instruction: Optional[str] = None,
    ) -> List[SearchResult]:
        """Embed query and run similarity search with optional filters."""
        # encode_query, not encode: asymmetric retrieval models prefix queries with
        # an instruction and leave documents bare.
        vec = self.embedder.encode_query(query, instruction=instruction)
        return self.store.similarity_search(
            query_embedding=vec,
            top_k=top_k,
            party_name=party_name,
            topics=topics,
        )

    # ------------------------------------------------------------------
    # Multi-query search with RRF (Part 5 + Part 6)
    # ------------------------------------------------------------------

    def multi_query_search(
        self,
        queries: List[str],
        top_k: int = 5,
        party_name: Optional[str] = None,
        topics: Optional[List[str]] = None,
        rrf_k: int = 60,
        use_rrf: bool = True,
        use_hybrid: bool = False,
        use_reranker: bool = False,
        rerank_query: Optional[str] = None,
        rerank_candidates: int = 30,
        strip_party_names: bool = False,
        query_instruction: Optional[str] = None,
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

        When ``use_reranker`` is True the whole search widens: every sub-query
        retrieves ``rerank_candidates`` instead of *top_k*, the fused list keeps
        that many, and a cross-encoder re-orders them before the trim back to
        *top_k*. Widening is the point — a reranker can only promote what
        retrieval already surfaced, so reranking a list of exactly *top_k* items
        would reshuffle the answer without ever improving what is in it.
        ``rerank_query`` is the text the cross-encoder scores against and should
        be the user's original question, not an expansion of it.
        """
        # Fetch depth: the reranker needs a wider net than the caller asked for.
        fetch_k = max(top_k, rerank_candidates) if use_reranker else top_k

        all_lists: List[List[SearchResult]] = []
        for q in queries:
            all_lists.append(
                self.search(
                    strip_party_mentions(q) if strip_party_names and party_name else q,
                    top_k=fetch_k,
                    party_name=party_name, topics=topics,
                    instruction=query_instruction,
                )
            )
            if use_hybrid:
                all_lists.append(
                    self.store.lexical_search(
                        strip_party_mentions(q) if party_name else q, top_k=fetch_k,
                        party_name=party_name, topics=topics,
                    )
                )

        fused = (
            reciprocal_rank_fusion(all_lists, k=rrf_k)
            if use_rrf
            else merge_preserve_order(all_lists)
        )
        logger.info(
            "Multi-query search: %d queries → %d ranked lists → %d unique results "
            "(hybrid=%s, rrf=%s, rerank=%s, returning top %d).",
            len(queries), len(all_lists), len(fused), use_hybrid, use_rrf,
            use_reranker, top_k,
        )

        if use_reranker and fused:
            if not rerank_query:
                # Refused rather than silently skipped: a variant that reports
                # un-reranked numbers under the reranked name is worse than a crash.
                raise ValueError(
                    "use_reranker=True requires rerank_query (the original question)."
                )
            from src.rag.retrieval.reranker import get_reranker

            return get_reranker().rerank(
                rerank_query, fused[:rerank_candidates], top_k=top_k
            )

        return fused[:top_k]
