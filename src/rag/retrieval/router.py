"""
Retrieval router – picks the search strategy from the analyzed query (Part 10).

Two strategies, keyed on ``AnalyzedQuery.query_type`` (derived from ``parties``
and ``coverage``):

- comparison → one search per party (the named ones, or all of them for an
  exhaustive question), so no party is crowded out of a global top-k;
- everything else → one search, filtered to the single named party (if any)
  and to the analyzed topics (if any). That covers single_party,
  topic_exploration and general, which differ only in which filters are set.
"""

import logging
from typing import List, Optional

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
progress = logging.getLogger("rag.progress")  # see retrieval/pipeline.py


def route(
    query: AnalyzedQuery,
    searcher: Searcher,
    config: Optional[RetrievalConfig] = None,
) -> RetrievalResult:
    """Search for *query* and return flat ``results``, plus ``results_by_party``
    for comparisons. ``config.use_routing=False`` (the naive arms) ignores the
    analysis and runs one unfiltered search."""
    config = config or RetrievalConfig()
    search_text = query.reformulated_query or query.original_query
    if config.use_multi_query:
        progress.info("A reformular a pergunta para a pesquisa…")
    queries = (
        expand_query(search_text, n_queries=config.multi_query_count, strict=config.strict)
        if config.use_multi_query
        else [search_text]
    )
    named = query.parties if config.use_routing else []
    progress.info("A pesquisar %s…", f"no programa de {named[0]}" if len(named) == 1 else
                  f"nos programas de {', '.join(named)}" if 1 < len(named) <= 3 else
                  f"nos programas de {len(named)} partidos" if named else "nos programas de todos os partidos")

    def search(top_k: int, party: Optional[str], topics: Optional[List[str]]) -> List[SearchResult]:
        return _search_relaxing_topics(searcher, queries, config, top_k, query.original_query, party, topics)

    if not config.use_routing:
        logger.info("Routing disabled → one unfiltered search.")
        return RetrievalResult(query=query, results=search(config.top_k, None, None))

    topics = query.topics or None
    if query.query_type == QueryType.COMPARISON:
        # No named party means an exhaustive question over the whole corpus. Bloc
        # questions ("os partidos de direita") arrive already resolved into names.
        parties = query.parties or [info["name"] for info in PARTY_MAP.values()]
        logger.info("Routing COMPARISON → parties: %s", parties)
        # Topics are relaxed per party, so one party lacking a topic does not lose
        # its filter for the others.
        grouped = {p: search(config.top_k_per_party, p, topics) for p in parties}
        flat = sorted((r for rs in grouped.values() for r in rs), key=lambda r: r.similarity, reverse=True)
        return RetrievalResult(query=query, results=flat[: config.top_k], results_by_party=grouped)

    party = query.parties[0] if query.parties else None
    logger.info("Routing %s → party=%s, topics=%s", query.query_type.value.upper(), party, topics)
    return RetrievalResult(query=query, results=search(config.top_k, party, topics))


def _search_relaxing_topics(
    searcher: Searcher,
    queries: List[str],
    config: RetrievalConfig,
    top_k: int,
    rerank_query: str,
    party: Optional[str],
    topics: Optional[List[str]],
) -> List[SearchResult]:
    """Search with the topic filter, retrying without it if nothing matches.

    The topic filter is a hard AND, so a topic no chunk carries (an analyzer
    label outside the classifier's output, or any topic on a --no-classify index)
    would return nothing. Topics are a precision aid, not a requirement: narrow
    first, then fall back to the unfiltered search.

    ``rerank_query`` is the user's original question: the cross-encoder must
    score what was asked, not one of the expansions.
    """
    results = searcher.multi_query_search(queries, config, top_k, rerank_query, party, topics)
    if results or not topics:
        return results
    logger.warning("No chunks matched topics=%s; retrying without the topic filter. "
                   "Is the index classified?", topics)
    return searcher.multi_query_search(queries, config, top_k, rerank_query, party, None)
