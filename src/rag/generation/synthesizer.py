"""
Answer synthesis strategies.

Selects the right strategy based on ``QueryType`` and produces a
``GeneratedAnswer`` with source citations.
"""

import logging
from typing import Dict, List, Optional

from src.rag.common.models import (
    AnalyzedQuery,
    GeneratedAnswer,
    QueryType,
    RetrievalResult,
    SearchResult,
)
from src.rag.generation.llm_client import generate_text
from src.rag.generation.prompts import (
    ANSWER_PROMPT,
    ANSWER_SYSTEM_PROMPT,
    COMPARISON_PROMPT,
    COMPARISON_SYSTEM_PROMPT,
    DECOMPOSITION_PROMPT,
    SYNTHESIS_PROMPT,
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Context formatting helpers
# ---------------------------------------------------------------------------

def _format_flat_context(results: List[SearchResult]) -> str:
    """Format a flat list of search results into numbered context blocks."""
    parts = []
    for i, r in enumerate(results, 1):
        # Build section breadcrumb from header hierarchy
        headers = " > ".join(r.header_hierarchy.values()) if r.header_hierarchy else ""
        header_line = f"  Secção: {headers}\n" if headers else ""
        parts.append(
            f"[Documento {i}] Partido: {r.party_name} | Tópicos: {', '.join(r.topics)}\n"
            f"{header_line}"
            f"{r.content}"
        )
    return "\n\n---\n\n".join(parts)


def _format_grouped_context(results_by_party: Dict[str, List[SearchResult]]) -> str:
    """Format search results grouped by party for comparison prompts."""
    parts = []
    for party, results in results_by_party.items():
        docs = []
        for i, r in enumerate(results, 1):
            headers = " > ".join(r.header_hierarchy.values()) if r.header_hierarchy else ""
            header_line = f"  Secção: {headers}\n" if headers else ""
            docs.append(f"  [{i}] {header_line}{r.content}")
        parts.append(f"## {party}\n" + "\n\n".join(docs))
    return "\n\n".join(parts)


def _build_sources(results: List[SearchResult]) -> List[Dict]:
    """Extract source metadata for citations."""
    return [
        {
            "party": r.party_name,
            "topics": r.topics,
            "section": " > ".join(r.header_hierarchy.values()) if r.header_hierarchy else "",
            "similarity": round(r.similarity, 4),
        }
        for r in results
    ]


# ---------------------------------------------------------------------------
# Synthesis strategies
# ---------------------------------------------------------------------------

def direct_answer(query: str, results: List[SearchResult]) -> GeneratedAnswer:
    """Single-pass generation for simple look-ups."""
    context = _format_flat_context(results)
    prompt = ANSWER_PROMPT.format(context=context, question=query)
    answer = generate_text(prompt, system_prompt=ANSWER_SYSTEM_PROMPT)
    return GeneratedAnswer(
        answer=answer,
        sources=_build_sources(results),
        query_type=QueryType.GENERAL,
    )


def comparison_answer(
    query: str,
    results_by_party: Dict[str, List[SearchResult]],
) -> GeneratedAnswer:
    """Grouped-by-party generation for comparison questions."""
    context = _format_grouped_context(results_by_party)
    prompt = COMPARISON_PROMPT.format(context=context, question=query)
    answer = generate_text(prompt, system_prompt=COMPARISON_SYSTEM_PROMPT)
    all_results = [r for rs in results_by_party.values() for r in rs]
    return GeneratedAnswer(
        answer=answer,
        sources=_build_sources(all_results),
        query_type=QueryType.COMPARISON,
    )


def decomposed_answer(
    query: str,
    results: List[SearchResult],
) -> GeneratedAnswer:
    """
    Decompose a complex question into sub-questions, answer each,
    then synthesise (Part 7 pattern).
    """
    # Step 1: decompose
    decomp_prompt = DECOMPOSITION_PROMPT.format(question=query)
    raw_sub_qs = generate_text(decomp_prompt, temperature=0.2)
    sub_questions = [q.strip() for q in raw_sub_qs.strip().split("\n") if q.strip()]

    if not sub_questions:
        logger.warning("Decomposition produced no sub-questions – falling back to direct.")
        return direct_answer(query, results)

    logger.info("Decomposed into %d sub-questions.", len(sub_questions))

    # Step 2: answer each sub-question with the same context
    context = _format_flat_context(results)
    qa_pairs = []
    for sq in sub_questions:
        sub_prompt = ANSWER_PROMPT.format(context=context, question=sq)
        sub_ans = generate_text(sub_prompt, system_prompt=ANSWER_SYSTEM_PROMPT, temperature=0.2)
        qa_pairs.append(f"Pergunta: {sq}\nResposta: {sub_ans}")

    # Step 3: synthesise
    qa_text = "\n\n---\n\n".join(qa_pairs)
    synth_prompt = SYNTHESIS_PROMPT.format(qa_pairs=qa_text, question=query)
    final = generate_text(synth_prompt, system_prompt=ANSWER_SYSTEM_PROMPT)
    return GeneratedAnswer(
        answer=final,
        sources=_build_sources(results),
        query_type=QueryType.COMPARISON,
    )


# ---------------------------------------------------------------------------
# Dispatcher
# ---------------------------------------------------------------------------

def synthesize(retrieval: RetrievalResult) -> GeneratedAnswer:
    """
    Pick the right synthesis strategy based on the query type
    and produce the final answer.
    """
    qt = retrieval.query.query_type
    q = retrieval.query.original_query

    if qt == QueryType.COMPARISON and retrieval.results_by_party:
        logger.info("Using comparison synthesis strategy.")
        return comparison_answer(q, retrieval.results_by_party)

    if qt == QueryType.COMPARISON and retrieval.results:
        logger.info("Comparison query but no grouped results – using decomposition.")
        return decomposed_answer(q, retrieval.results)

    if qt == QueryType.TOPIC_EXPLORATION and len(retrieval.results) > 8:
        logger.info("Large topic exploration – using decomposition.")
        return decomposed_answer(q, retrieval.results)

    logger.info("Using direct answer strategy.")
    return direct_answer(q, retrieval.results)
