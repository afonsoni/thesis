"""
Retrieval pipeline – single entry-point for the retrieval stage.

Chains: analyze → expand → route → search → return RetrievalResult.
"""

import logging
from typing import Dict, Optional

from src.rag.common.models import RetrievalResult
from src.rag.indexing.store import VectorStore
from src.rag.retrieval.config import RetrievalConfig
from src.rag.retrieval.query_analyzer import analyze_query
from src.rag.retrieval.router import route
from src.rag.retrieval.searcher import Searcher

logger = logging.getLogger(__name__)

# Module-level singleton to avoid re-loading the embedding model on every call
_searcher: Optional[Searcher] = None
# Searchers over alternative index tables (RetrievalConfig.table), sharing the
# default searcher's embedder so the model is loaded once.
_table_searchers: Dict[str, Searcher] = {}


def _get_searcher(table: Optional[str] = None) -> Searcher:
    global _searcher
    if _searcher is None:
        _searcher = Searcher()
    if not table or table == _searcher.store.table:
        return _searcher
    if table not in _table_searchers:
        store = VectorStore()
        store.table = table
        _table_searchers[table] = Searcher(embedder=_searcher.embedder, store=store)
    return _table_searchers[table]


def retrieve(
    question: str,
    top_k: Optional[int] = None,
    expand_queries: Optional[bool] = None,
    config: Optional[RetrievalConfig] = None,
) -> RetrievalResult:
    """
    Full retrieval pipeline:

    1. **Analyze** the question (extract query type, parties, topics, etc.)
    2. **Route** to the appropriate search strategy
    3. **Return** ranked results.

    Args:
        question: Natural-language user question.
        top_k: Number of results to return (per party for comparison queries).
               Overrides ``config.top_k`` when provided (CLI back-compat).
        expand_queries: Whether to use multi-query expansion. Overrides
               ``config.use_multi_query`` when provided (CLI back-compat).
        config: Full retrieval feature-flag config. Defaults to production
               behavior. This is how the evaluation harness selects a variant.

    Returns:
        ``RetrievalResult`` ready for the generation pipeline.
    """
    config = config or RetrievalConfig()
    overrides = {}
    if top_k is not None:
        overrides["top_k"] = top_k
    if expand_queries is not None:
        overrides["use_multi_query"] = expand_queries
    if overrides:
        config = config.model_copy(update=overrides)

    # Step 1: understand the question
    analyzed = analyze_query(question, config=config)
    logger.info(
        "Query analysis → type=%s, parties=%s, topics=%s",
        analyzed.query_type.value,
        analyzed.parties,
        analyzed.topics,
    )

    # Step 2: route & search
    searcher = _get_searcher(config.table)
    result = route(analyzed, searcher, config=config)
    logger.info("Retrieved %d results.", len(result.results))

    return result
