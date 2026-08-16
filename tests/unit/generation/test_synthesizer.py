"""Dispatch and prompt-budget behaviour of the synthesiser."""

from typing import Dict, List
from unittest.mock import patch

import pytest

from src.rag.common.models import (
    AnalyzedQuery,
    AnswerShape,
    Coverage,
    RetrievalResult,
    SearchResult,
)
from src.rag.generation import synthesizer
from src.rag.generation.synthesizer import synthesize


def _result(party: str, n: int = 1, size: int = 40) -> SearchResult:
    return SearchResult(
        id=f"{party}-{n}",
        content=f"{party} conteudo {n} " + ("x" * size),
        party_name=party,
        topics=["saude"],
        similarity=1.0 / n,
    )


def _grouped(parties: List[str], per_party: int = 2, size: int = 40) -> Dict[str, List[SearchResult]]:
    return {p: [_result(p, i + 1, size) for i in range(per_party)] for p in parties}


def _retrieval(shape: AnswerShape, grouped=None, results=None) -> RetrievalResult:
    return RetrievalResult(
        query=AnalyzedQuery(
            original_query="Pergunta",
            coverage=Coverage.EXHAUSTIVE if grouped else Coverage.BEST_MATCH,
            answer_shape=shape,
        ),
        results=results or [],
        results_by_party=grouped or {},
    )


@pytest.fixture
def captured_prompts():
    """Capture every prompt sent to the LLM instead of calling it."""
    seen: List[str] = []

    def fake_generate_text(prompt, *args, **kwargs):
        seen.append(prompt)
        return "resposta"

    with patch.object(synthesizer, "generate_text", side_effect=fake_generate_text):
        yield seen


@pytest.mark.unit
def test_per_party_shape_uses_the_grouped_comparison_prompt(captured_prompts):
    grouped = _grouped(["Partido Socialista", "CHEGA"])

    answer = synthesize(_retrieval(AnswerShape.PER_PARTY, grouped=grouped))

    assert len(captured_prompts) == 1
    assert "## Partido Socialista" in captured_prompts[0]
    assert "## CHEGA" in captured_prompts[0]
    assert len(answer.sources) == 4


@pytest.mark.unit
def test_narrative_shape_over_a_fan_out_reads_every_party(captured_prompts):
    """The router truncates the flat list to top_k; a verdict must not.

    A narrative answer that claims to weigh all parties while seeing only the
    top-ranked few is wrong in a way nothing in the output reveals.
    """
    grouped = _grouped(["Partido Socialista", "CHEGA", "LIVRE", "Bloco de Esquerda"])
    retrieval = _retrieval(
        AnswerShape.NARRATIVE,
        grouped=grouped,
        results=[_result("Partido Socialista", 1)],  # the truncated flat list
    )

    synthesize(retrieval)

    prompt = captured_prompts[0]
    for party in grouped:
        assert party in prompt


@pytest.mark.unit
def test_per_party_without_grouped_results_decomposes(captured_prompts):
    retrieval = _retrieval(AnswerShape.PER_PARTY, results=[_result("CHEGA")])

    synthesize(retrieval)

    # Decomposition: one call to split the question, one per sub-question, one
    # to synthesise — more than the single call a direct answer would make.
    assert len(captured_prompts) > 1


@pytest.mark.unit
def test_flat_context_is_trimmed_to_the_prompt_budget(captured_prompts):
    results = [_result("CHEGA", i + 1, size=4000) for i in range(10)]
    retrieval = _retrieval(AnswerShape.NARRATIVE, results=results)

    with patch.object(synthesizer, "_prompt_budget", return_value=2000):
        answer = synthesize(retrieval)

    assert synthesizer._estimate_tokens(captured_prompts[0]) <= 2200
    # Citations follow the trimmed context, not what retrieval returned: a
    # source the model never read is a citation it cannot have used.
    assert len(answer.sources) < 10


@pytest.mark.unit
def test_grouped_trim_never_drops_a_party(captured_prompts):
    """Coverage is the point of the fan-out; an over-long prompt is the lesser evil."""
    grouped = _grouped(["A", "B", "C", "D"], per_party=4, size=4000)

    with patch.object(synthesizer, "_prompt_budget", return_value=1000):
        synthesize(_retrieval(AnswerShape.PER_PARTY, grouped=grouped))

    prompt = captured_prompts[0]
    for party in ("A", "B", "C", "D"):
        assert f"## {party}" in prompt


@pytest.mark.unit
def test_grouped_trim_equalises_rather_than_truncating_the_tail():
    """Chunks come off the biggest contributor, not off whichever party is last."""
    grouped = {"A": [_result("A", i + 1, size=2000) for i in range(6)], "B": [_result("B", 1, size=2000)]}

    with patch.object(synthesizer, "_prompt_budget", return_value=1500):
        kept = synthesizer._fit_grouped(grouped)

    assert len(kept["B"]) == 1
    assert len(kept["A"]) < 6
