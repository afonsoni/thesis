"""
Retrieval pipeline – single entry-point for the retrieval stage.

Chains: analyze → expand → route → search → return RetrievalResult.
"""

import logging
from typing import Optional

from src.rag.common.models import RetrievalResult
from src.rag.retrieval.query_analyzer import analyze_query
from src.rag.retrieval.router import route
from src.rag.retrieval.searcher import Searcher

logger = logging.getLogger(__name__)

# Module-level singleton to avoid re-loading the embedding model on every call
_searcher: Optional[Searcher] = None


def _get_searcher() -> Searcher:
    global _searcher
    if _searcher is None:
        _searcher = Searcher()
    return _searcher


def retrieve(
    question: str,
    top_k: int = 5,
    expand_queries: bool = True,
) -> RetrievalResult:
    """
    Full retrieval pipeline:

    1. **Analyze** the question (extract query type, parties, topics, etc.)
    2. **Route** to the appropriate search strategy
    3. **Return** ranked results.

    Args:
        question: Natural-language user question.
        top_k: Number of results to return (per party for comparison queries).
        expand_queries: Whether to use multi-query expansion.

    Returns:
        ``RetrievalResult`` ready for the generation pipeline.
    """
    # Step 1: understand the question
    analyzed = analyze_query(question)
    logger.info(
        "Query analysis → type=%s, parties=%s, topics=%s",
        analyzed.query_type.value,
        analyzed.parties,
        analyzed.topics,
    )

    # Step 2: route & search
    searcher = _get_searcher()
    result = route(analyzed, searcher, top_k=top_k, expand_queries=expand_queries)
    logger.info("Retrieved %d results.", len(result.results))

    return result
