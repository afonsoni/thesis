"""
Retrieval router – dispatches search strategies based on query type (Part 10).

Routes:
- single_party   → metadata-filtered search with multi-query expansion
- comparison      → parallel per-party searches with multi-query + RRF
- topic_exploration → multi-query + topic-filtered search across all parties
- general         → broad multi-query search with RRF
"""

import logging
from typing import Dict, List, Optional

from src.rag.common.models import (
    AnalyzedQuery,
    PARTY_MAP,
    QueryType,
    RetrievalResult,
    SearchResult,
)
from src.rag.retrieval.config import RetrievalConfig
from src.rag.retrieval.query_expander import expand_query
from src.rag.retrieval.searcher import Searcher

logger = logging.getLogger(__name__)

DEFAULT_TOP_K = 5
DEFAULT_TOP_K_PER_PARTY = 3


def route(
    query: AnalyzedQuery,
    searcher: Searcher,
    config: Optional[RetrievalConfig] = None,
) -> RetrievalResult:
    """
    Route the analyzed query to the appropriate search strategy.

    Returns a ``RetrievalResult`` with either a flat ``results`` list
    or a grouped ``results_by_party`` dict (for comparisons).

    Behavior is driven by ``config``: ``use_multi_query`` controls expansion,
    ``use_routing`` toggles type-specific strategies (off → always GENERAL),
    and ``use_rrf`` / ``rrf_k`` / ``top_k`` / ``top_k_per_party`` size the search.
    """
    config = config or RetrievalConfig()
    qt = query.query_type
    search_text = query.reformulated_query or query.original_query

    # Multi-query expansion (Part 5)
    if config.use_multi_query:
        queries = expand_query(search_text, n_queries=config.multi_query_count)
    else:
        queries = [search_text]

    if not config.use_routing:
        return _route_general(query, queries, searcher, config)

    if qt == QueryType.SINGLE_PARTY and query.parties:
        return _route_single_party(query, queries, searcher, config)
    elif qt == QueryType.COMPARISON:
        return _route_comparison(query, queries, searcher, config)
    elif qt == QueryType.TOPIC_EXPLORATION:
        return _route_topic_exploration(query, queries, searcher, config)
    else:
        return _route_general(query, queries, searcher, config)


# ---------------------------------------------------------------------------
# Strategy implementations
# ---------------------------------------------------------------------------

def _route_single_party(
    query: AnalyzedQuery,
    queries: List[str],
    searcher: Searcher,
    config: RetrievalConfig,
) -> RetrievalResult:
    """Metadata-filtered search for a specific party."""
    party = query.parties[0]
    logger.info("Routing SINGLE_PARTY → %s", party)
    results = searcher.multi_query_search(
        queries,
        top_k=config.top_k,
        party_name=party,
        topics=query.topics or None,
        rrf_k=config.rrf_k,
        use_rrf=config.use_rrf,
        use_hybrid=config.use_hybrid,
    )
    return RetrievalResult(query=query, results=results)


def _route_comparison(
    query: AnalyzedQuery,
    queries: List[str],
    searcher: Searcher,
    config: RetrievalConfig,
) -> RetrievalResult:
    """Per-party parallel search for comparison queries."""
    parties = query.parties
    if not parties:
        # If no parties detected, compare by ideology or all parties
        if query.ideology_filter:
            parties = [
                info["name"]
                for info in PARTY_MAP.values()
                if info["ideology"] == query.ideology_filter
            ]
        else:
            parties = [info["name"] for info in PARTY_MAP.values()]

    logger.info("Routing COMPARISON → parties: %s", parties)
    grouped = searcher.multi_query_batch_search_by_party(
        queries,
        parties=parties,
        top_k_per_party=config.top_k_per_party,
        topics=query.topics or None,
        rrf_k=config.rrf_k,
        use_rrf=config.use_rrf,
        use_hybrid=config.use_hybrid,
    )
    # Also provide a flat list for fallback
    flat = [r for rs in grouped.values() for r in rs]
    flat.sort(key=lambda r: r.similarity, reverse=True)
    return RetrievalResult(
        query=query,
        results=flat[: config.top_k],
        results_by_party=grouped,
    )


def _route_topic_exploration(
    query: AnalyzedQuery,
    queries: List[str],
    searcher: Searcher,
    config: RetrievalConfig,
) -> RetrievalResult:
    """Topic-filtered search across all parties."""
    logger.info("Routing TOPIC_EXPLORATION → topics: %s", query.topics)
    results = searcher.multi_query_search(
        queries,
        top_k=config.top_k,
        ideology=query.ideology_filter,
        topics=query.topics or None,
        rrf_k=config.rrf_k,
        use_rrf=config.use_rrf,
        use_hybrid=config.use_hybrid,
    )
    return RetrievalResult(query=query, results=results)


def _route_general(
    query: AnalyzedQuery,
    queries: List[str],
    searcher: Searcher,
    config: RetrievalConfig,
) -> RetrievalResult:
    """Broad search with no filters, multi-query + RRF."""
    logger.info("Routing GENERAL query.")
    results = searcher.multi_query_search(
        queries,
        top_k=config.top_k,
        rrf_k=config.rrf_k,
        use_rrf=config.use_rrf,
        use_hybrid=config.use_hybrid,
    )
    return RetrievalResult(query=query, results=results)
