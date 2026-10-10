"""
Answer synthesis strategies.

Selects the right strategy based on ``AnswerShape`` and produces a
``GeneratedAnswer`` with source citations.
"""

import logging
from typing import Dict, List, Optional, Tuple

from src.rag.common.models import (
    AnswerShape,
    GeneratedAnswer,
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
)

logger = logging.getLogger(__name__)
progress = logging.getLogger("rag.progress")  # see retrieval/pipeline.py


# ---------------------------------------------------------------------------
# Context formatting helpers
# ---------------------------------------------------------------------------

def _merge_windows(a: str, b: str) -> Optional[str]:
    """One text covering both windows if one contains or overlaps the other, else None."""
    if b in a:
        return a
    if a in b:
        return b
    for first, second in ((a, b), (b, a)):
        start = first.find(second[:200])
        if start >= 0 and second.startswith(first[start:]):
            return first + second[len(first) - start:]
    return None


def _dedupe_by_context(results: List[SearchResult]) -> List[SearchResult]:
    """Collapse results whose context windows repeat or overlap, keeping rank order.

    Under small-to-big retrieval several sibling children of one section win
    slots, and their parent windows are the same text or overlapping slices of
    it (neighbouring windows share most of their lines). Left alone, the prompt
    carries the same passage two or three times, wasting budget and biasing the
    model toward what it repeats. Overlapping windows of one section become a
    single document spanning both, at the rank of the best-ranked child.
    """
    kept: List[SearchResult] = []
    for r in results:
        for i, k in enumerate(kept):
            if (k.party_name, k.section_path) != (r.party_name, r.section_path):
                continue
            merged = _merge_windows(k.context_text, r.context_text)
            if merged is not None:
                kept[i] = k.model_copy(update={"parent_content": merged})
                break
        else:
            kept.append(r)
    return kept


def _numbered_flat(results: List[SearchResult]) -> List[Tuple[int, SearchResult]]:
    """The documents a flat prompt shows, with the number it shows them under."""
    return list(enumerate(_dedupe_by_context(results), 1))


def _numbered_grouped(
    results_by_party: Dict[str, List[SearchResult]],
) -> Dict[str, List[Tuple[int, SearchResult]]]:
    """Per-party documents numbered across the whole prompt, so ``[n]`` names one."""
    numbered: Dict[str, List[Tuple[int, SearchResult]]] = {}
    n = 0
    for party, results in results_by_party.items():
        numbered[party] = []
        for r in _dedupe_by_context(results):
            n += 1
            numbered[party].append((n, r))
    return numbered


def _format_flat_context(results: List[SearchResult]) -> str:
    """Format a flat list of search results into numbered context blocks."""
    parts = []
    for i, r in _numbered_flat(results):
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
    for party, numbered in _numbered_grouped(results_by_party).items():
        docs = []
        for i, r in numbered:
            headers = r.section_path
            header_line = f"  Secção: {headers}\n" if headers else ""
            docs.append(f"[Documento {i}]\n{header_line}{r.context_text}")
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
    return int(config.get("llm.openrouter.max_prompt_tokens"))


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


def _build_sources(numbered: List[Tuple[int, SearchResult]]) -> List[Dict]:
    """Source metadata for citations: ``n`` is the ``[n]`` the answer cites."""
    return [
        {
            "n": n,
            "id": r.id,
            "party": r.party_name,
            "topics": r.topics,
            "section": r.section_path,
            "similarity": round(r.similarity, 4),
            "score_type": r.score_type.value,
        }
        for n, r in numbered
    ]


# ---------------------------------------------------------------------------
# Synthesis strategies
# ---------------------------------------------------------------------------

def direct_answer(query: str, results: List[SearchResult]) -> GeneratedAnswer:
    """Single-pass generation for simple look-ups."""
    context = _format_flat_context(results)
    prompt = ANSWER_PROMPT.format(context=context, question=query)
    progress.info("A redigir a resposta a partir de %d excertos…", len(results))
    answer = generate_text(prompt, system_prompt=ANSWER_SYSTEM_PROMPT, label="answer")
    return GeneratedAnswer(
        answer=answer,
        sources=_build_sources(_numbered_flat(results)),
        context=context,
    )


def comparison_answer(
    query: str,
    results_by_party: Dict[str, List[SearchResult]],
) -> GeneratedAnswer:
    """Grouped-by-party generation for comparison questions."""
    context = _format_grouped_context(results_by_party)
    prompt = COMPARISON_PROMPT.format(context=context, question=query)
    if len(results_by_party) > 1:
        progress.info("A redigir a comparação entre %d partidos…", len(results_by_party))
    else:
        progress.info("A redigir a resposta…")
    answer = generate_text(prompt, system_prompt=COMPARISON_SYSTEM_PROMPT, label="comparison answer")
    return GeneratedAnswer(
        answer=answer,
        sources=_build_sources([x for xs in _numbered_grouped(results_by_party).values() for x in xs]),
        context=context,
    )


# ---------------------------------------------------------------------------
# Dispatcher
# ---------------------------------------------------------------------------

def synthesize(retrieval: RetrievalResult) -> GeneratedAnswer:
    """Pick a synthesis strategy from the requested answer shape.

    Shape rather than route: they cross. "Que partido propõe mais sobre
    habitação?" retrieves every party but wants one verdict, not eight sections.
    """
    q = retrieval.query.original_query
    shape = retrieval.query.answer_shape
    grouped = retrieval.results_by_party

    if shape == AnswerShape.PER_PARTY:
        if grouped:
            logger.info("Using comparison synthesis strategy.")
            return comparison_answer(q, _fit_grouped(grouped))
        if retrieval.results:
            # Flat results (e.g. a single-party route): group them so the answer
            # can still be laid out party by party.
            by_party: Dict[str, List[SearchResult]] = {}
            for r in retrieval.results:
                by_party.setdefault(r.party_name, []).append(r)
            logger.info("Per-party answer from flat results – grouping by party.")
            return comparison_answer(q, _fit_grouped(by_party))

    # A narrative answer over a fan-out reads the whole grouped set, not
    # ``results``: the router truncates that flat list to top_k, which would
    # quietly hide most parties behind a verdict claiming to weigh them all.
    # It is trimmed per party before flattening, for the same reason: a flat
    # lowest-ranked-first trim drops every chunk of a party that ranks low.
    if grouped:
        flat = sorted(
            (r for rs in _fit_grouped(grouped).values() for r in rs),
            key=lambda r: r.similarity,
            reverse=True,
        )
    else:
        flat = _fit_flat(retrieval.results)

    logger.info("Using direct answer strategy.")
    return direct_answer(q, flat)
