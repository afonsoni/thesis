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

def _search_relaxing_topics(
    queries: List[str],
    searcher: Searcher,
    config: RetrievalConfig,
    topics: Optional[List[str]],
    **filters,
) -> List[SearchResult]:
    """Search with the topic filter, retrying without it if nothing matches.

    The topic filter is a hard AND: a topic the query analyzer proposes but that
    no chunk carries silently yields zero results, and the caller cannot tell an
    empty corpus from a filter mismatch. That happens whenever the analyzer's
    label does not match the classifier's vocabulary, and always on an index built
    with --no-classify, where every chunk keeps the default topic.

    Topics are a precision aid, not a correctness requirement, so they are treated
    as a preference: narrow first, then fall back to the unfiltered search rather
    than return nothing.
    """
    results = searcher.multi_query_search(
        queries,
        top_k=config.top_k,
        topics=topics,
        rrf_k=config.rrf_k,
        use_rrf=config.use_rrf,
        use_hybrid=config.use_hybrid,
        **filters,
    )
    if results or not topics:
        return results

    logger.warning(
        "No chunks matched topics=%s; retrying without the topic filter. "
        "Is the index classified?",
        topics,
    )
    return searcher.multi_query_search(
        queries,
        top_k=config.top_k,
        topics=None,
        rrf_k=config.rrf_k,
        use_rrf=config.use_rrf,
        use_hybrid=config.use_hybrid,
        **filters,
    )


def _route_single_party(
    query: AnalyzedQuery,
    queries: List[str],
    searcher: Searcher,
    config: RetrievalConfig,
) -> RetrievalResult:
    """Metadata-filtered search for a specific party."""
    party = query.parties[0]
    logger.info("Routing SINGLE_PARTY → %s", party)
    results = _search_relaxing_topics(
        queries, searcher, config,
        topics=query.topics or None,
        party_name=party,
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
    # Relax per party, not across the batch: one party lacking a topic must not
    # drop it from a comparison while the others keep their filtered hits.
    grouped = {
        party: _search_relaxing_topics(
            queries, searcher,
            config.model_copy(update={"top_k": config.top_k_per_party}),
            topics=query.topics or None,
            party_name=party,
        )
        for party in parties
    }
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
    results = _search_relaxing_topics(
        queries, searcher, config,
        topics=query.topics or None,
        ideology=query.ideology_filter,
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
