"""
Answer synthesis strategies.

Selects the right strategy based on ``AnswerShape`` and produces a
``GeneratedAnswer`` with source citations.
"""

import logging
from typing import Dict, List

from src.rag.common.models import (
    AnswerShape,
    GeneratedAnswer,
    QueryType,
    RetrievalResult,
    SearchResult,
)
from src.utils.config_loader import config
from src.rag.common.llm_client import generate_text
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

def _dedupe_by_context(results: List[SearchResult]) -> List[SearchResult]:
    """Drop results whose context text was already included, keeping rank order.

    Under small-to-big retrieval several sibling children can win slots in the
    same parent section, and each would expand to identical parent text. Without
    this the prompt carries the same passage two or three times, wasting context
    and biasing the model toward whatever it repeats.
    """
    seen: set[str] = set()
    unique: List[SearchResult] = []
    for r in results:
        text = r.context_text
        if text in seen:
            continue
        seen.add(text)
        unique.append(r)
    return unique


def _format_flat_context(results: List[SearchResult]) -> str:
    """Format a flat list of search results into numbered context blocks."""
    parts = []
    for i, r in enumerate(_dedupe_by_context(results), 1):
        # Build section breadcrumb from header hierarchy
        headers = r.section_path
        header_line = f"  Secção: {headers}\n" if headers else ""
        parts.append(
            f"[Documento {i}] Partido: {r.party_name} | Tópicos: {', '.join(r.topics)}\n"
            f"{header_line}"
            f"{r.context_text}"
        )
    return "\n\n---\n\n".join(parts)


def _format_grouped_context(results_by_party: Dict[str, List[SearchResult]]) -> str:
    """Format search results grouped by party for comparison prompts."""
    parts = []
    for party, results in results_by_party.items():
        docs = []
        for i, r in enumerate(_dedupe_by_context(results), 1):
            headers = r.section_path
            header_line = f"  Secção: {headers}\n" if headers else ""
            docs.append(f"  [{i}] {header_line}{r.context_text}")
        parts.append(f"## {party}\n" + "\n\n".join(docs))
    return "\n\n".join(parts)


# ---------------------------------------------------------------------------
# Prompt budget
# ---------------------------------------------------------------------------

# Characters per token for Portuguese prose under a subword tokenizer. The
# generation model is reached over OpenRouter, so its tokenizer is not available
# locally and the count is an estimate. Deliberately on the low side: it
# overstates the token count, so the trim happens slightly early rather than one
# chunk too late.
_CHARS_PER_TOKEN = 3.5


def _estimate_tokens(text: str) -> int:
    return int(len(text) / _CHARS_PER_TOKEN)


def _prompt_budget() -> int:
    """Tokens of context a single generation prompt may carry."""
    return int(config.get("llm.openrouter.max_prompt_tokens", 8000))


def _fit_flat(results: List[SearchResult]) -> List[SearchResult]:
    """Drop lowest-ranked results until the formatted context fits the budget."""
    budget = _prompt_budget()
    kept = list(results)
    while kept and _estimate_tokens(_format_flat_context(kept)) > budget:
        kept.pop()
    dropped = len(results) - len(kept)
    if dropped:
        logger.warning(
            "Context over the %d-token budget: dropped the %d lowest-ranked of %d chunks.",
            budget, dropped, len(results),
        )
    return kept


def _fit_grouped(
    results_by_party: Dict[str, List[SearchResult]],
) -> Dict[str, List[SearchResult]]:
    """Trim a grouped context to budget without losing a party.

    Chunks come off whichever party currently contributes most, so the trim
    equalises rather than truncating the tail of the dict. Dropping a party
    outright would undo the fan-out that produced these results: the answer
    would silently omit it, which is the failure the per-party route exists to
    prevent. Every party therefore keeps at least one chunk, even if that means
    exceeding the budget — an over-long prompt is a visible failure, a missing
    party is not.
    """
    budget = _prompt_budget()
    kept = {party: list(rs) for party, rs in results_by_party.items() if rs}
    total = sum(len(rs) for rs in kept.values())

    while _estimate_tokens(_format_grouped_context(kept)) > budget:
        biggest = max(kept, key=lambda p: len(kept[p]))
        if len(kept[biggest]) <= 1:
            logger.warning(
                "Grouped context still over the %d-token budget at one chunk per "
                "party; sending it rather than dropping a party.", budget,
            )
            break
        kept[biggest].pop()

    dropped = total - sum(len(rs) for rs in kept.values())
    if dropped:
        logger.warning(
            "Grouped context over the %d-token budget: dropped %d of %d chunks, "
            "keeping every party.", budget, dropped, total,
        )
    return kept


def _build_sources(results: List[SearchResult]) -> List[Dict]:
    """Extract source metadata for citations."""
    return [
        {
            "party": r.party_name,
            "topics": r.topics,
            "section": r.section_path,
            "similarity": round(r.similarity, 4),
            "score_type": r.score_type.value,
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
    """Pick a synthesis strategy from the requested answer shape.

    Shape rather than route: they cross. "Que partido propõe mais sobre
    habitação?" retrieves every party but wants one verdict, and dispatching on
    the route would have laid it out party by party.

    There is no longer a result-count trigger for decomposition. The old rule
    sent topic explorations with more than eight results down that path on the
    theory that they were too large, but ``decomposed_answer`` formats the same
    full context once and reuses it for every sub-question — it multiplies LLM
    calls at constant context and never made a prompt smaller. Prompt size is
    now handled where it belongs, by trimming to a measured budget, and
    decomposition is left to the case it actually addresses: a multi-party
    question whose results arrived flat, with no per-party grouping to lay out.
    """
    q = retrieval.query.original_query
    shape = retrieval.query.answer_shape
    grouped = retrieval.results_by_party

    if shape == AnswerShape.PER_PARTY:
        if grouped:
            logger.info("Using comparison synthesis strategy.")
            return comparison_answer(q, _fit_grouped(grouped))
        if retrieval.results:
            logger.info("Per-party answer without grouped results – decomposing.")
            return decomposed_answer(q, _fit_flat(retrieval.results))

    # A narrative answer over a fan-out reads the whole grouped set, not
    # ``results``: the router truncates that flat list to top_k, which would
    # quietly hide most parties behind a verdict claiming to weigh them all.
    if grouped:
        flat = sorted(
            (r for rs in grouped.values() for r in rs),
            key=lambda r: r.similarity,
            reverse=True,
        )
    else:
        flat = retrieval.results

    logger.info("Using direct answer strategy.")
    return direct_answer(q, _fit_flat(flat))
