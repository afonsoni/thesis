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


def test_per_party_shape_uses_the_grouped_comparison_prompt(captured_prompts):
    grouped = _grouped(["Partido Socialista", "CHEGA"])

    answer = synthesize(_retrieval(AnswerShape.PER_PARTY, grouped=grouped))

    assert len(captured_prompts) == 1
    assert "## Partido Socialista" in captured_prompts[0]
    assert "## CHEGA" in captured_prompts[0]
    assert len(answer.sources) == 4


@pytest.mark.parametrize("retrieval", [
    _retrieval(AnswerShape.PER_PARTY, results=[_result("CHEGA", 1), _result("CHEGA", 2)]),
    _retrieval(AnswerShape.PER_PARTY, grouped=_grouped(["CHEGA"])),
    _retrieval(AnswerShape.PER_PARTY, grouped={"CHEGA": [_result("CHEGA")], "LIVRE": []}),
], ids=["single-party route", "one-party fan-out", "fan-out with one party empty"])
def test_per_party_shape_with_one_party_is_not_a_comparison(retrieval):
    """The analyzer labels single-party questions per_party too (gold q-03); the
    comparison prompt then closes with a "síntese" that there is nothing to compare."""
    with patch.object(synthesizer, "generate_text", return_value="resposta") as gen:
        synthesize(retrieval)

    assert gen.call_args.kwargs["system_prompt"] == synthesizer.ANSWER_SYSTEM_PROMPT


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


def test_per_party_without_grouped_results_groups_them_by_party(captured_prompts):
    retrieval = _retrieval(AnswerShape.PER_PARTY, results=[_result("CHEGA"), _result("LIVRE")])

    synthesize(retrieval)

    assert len(captured_prompts) == 1
    assert "## CHEGA" in captured_prompts[0]
    assert "## LIVRE" in captured_prompts[0]


def test_flat_context_is_trimmed_to_the_prompt_budget(captured_prompts):
    results = [_result("CHEGA", i + 1, size=4000) for i in range(10)]
    retrieval = _retrieval(AnswerShape.NARRATIVE, results=results)

    with patch.object(synthesizer, "_prompt_budget", return_value=2000):
        answer = synthesize(retrieval)

    assert synthesizer._estimate_tokens(captured_prompts[0]) <= 2200
    # Citations follow the trimmed context, not what retrieval returned: a
    # source the model never read is a citation it cannot have used.
    assert len(answer.sources) < 10


def test_grouped_trim_never_drops_a_party(captured_prompts):
    """Coverage is the point of the fan-out; an over-long prompt is the lesser evil."""
    grouped = _grouped(["A", "B", "C", "D"], per_party=4, size=4000)

    with patch.object(synthesizer, "_prompt_budget", return_value=1000):
        synthesize(_retrieval(AnswerShape.PER_PARTY, grouped=grouped))

    prompt = captured_prompts[0]
    for party in ("A", "B", "C", "D"):
        assert f"## {party}" in prompt


def test_grouped_trim_equalises_rather_than_truncating_the_tail():
    """Chunks come off the biggest contributor, not off whichever party is last."""
    grouped = {"A": [_result("A", i + 1, size=2000) for i in range(6)], "B": [_result("B", 1, size=2000)]}

    with patch.object(synthesizer, "_prompt_budget", return_value=1500):
        kept = synthesizer._fit_grouped(grouped)

    assert len(kept["B"]) == 1
    assert len(kept["A"]) < 6


def test_sources_carry_the_number_the_prompt_shows(captured_prompts):
    """Siblings sharing a parent are shown once; [n] in the answer must name the
    same document in ``sources``, so numbering skips the duplicate in both."""
    a, b, c = _result("LIVRE", 1), _result("LIVRE", 2), _result("LIVRE", 3)
    b.parent_content = a.parent_content = "secção partilhada"

    answer = synthesize(_retrieval(AnswerShape.NARRATIVE, results=[a, b, c]))

    assert [(s["n"], s["id"]) for s in answer.sources] == [(1, "LIVRE-1"), (2, "LIVRE-3")]
    assert "[Documento 2]" in captured_prompts[0] and "[Documento 3]" not in captured_prompts[0]


def test_overlapping_windows_of_one_section_become_one_document(captured_prompts):
    """Neighbouring children's parents are overlapping slices of one section;
    showing both repeats most of the passage, so they merge into one span."""
    section = " ".join(f"Frase {i} da secção sobre habitação." for i in range(60))
    a, b, other = _result("LIVRE", 1), _result("LIVRE", 2), _result("LIVRE", 3)
    a.parent_content, b.parent_content = section[:1200], section[800:2000]

    answer = synthesize(_retrieval(AnswerShape.NARRATIVE, results=[a, b, other]))

    assert [s["id"] for s in answer.sources] == ["LIVRE-1", "LIVRE-3"]
    prompt = captured_prompts[0]
    assert section[:2000] in prompt and prompt.count("Frase 30 da secção") == 1


def test_grouped_documents_are_numbered_across_parties(captured_prompts):
    """Per-party numbering restarted at [1] for every party, so [1] was ambiguous."""
    answer = synthesize(_retrieval(AnswerShape.PER_PARTY, grouped=_grouped(["Partido Socialista", "CHEGA"])))

    assert [(s["n"], s["party"]) for s in answer.sources] == [
        (1, "Partido Socialista"), (2, "Partido Socialista"), (3, "CHEGA"), (4, "CHEGA"),
    ]
    assert "[Documento 4]" in captured_prompts[0]


def test_narrative_trim_over_a_fan_out_never_drops_a_party(captured_prompts):
    """A party that ranks low everywhere must survive the budget trim."""
    grouped = _grouped(["A", "B", "C"], per_party=4, size=4000)
    for r in grouped["C"]:
        r.similarity = 0.001  # below every chunk of A and B

    with patch.object(synthesizer, "_prompt_budget", return_value=3000):
        synthesize(_retrieval(AnswerShape.NARRATIVE, grouped=grouped))

    assert "C conteudo" in captured_prompts[0]


def test_fan_out_with_every_party_empty_never_reaches_the_llm(captured_prompts):
    from src.rag.generation.pipeline import generate

    answer = generate(_retrieval(AnswerShape.PER_PARTY, grouped={"A": [], "B": []}))

    assert captured_prompts == [] and answer.sources == []


def test_a_retrieval_can_carry_its_own_prompt_budget():
    """A variant's max_prompt_tokens must reach the trim, so `wide_64k` reads more."""
    from src.rag.common.models import AnalyzedQuery, RetrievalResult, SearchResult

    hits = [SearchResult(id=str(i), content=f"palavra{i} " * 700, party_name="Partido Socialista") for i in range(10)]
    seen = []
    with patch.object(synthesizer, "direct_answer", side_effect=lambda q, rs, on_token=None, model=None: seen.append(len(rs))):
        for budget in (2000, 8000):
            synthesizer.synthesize(RetrievalResult(query=AnalyzedQuery(original_query="q"), results=hits,
                                                   max_prompt_tokens=budget))
    assert seen[0] < seen[1]


def test_closed_book_answers_without_context_from_the_variant_model():
    seen = {}

    def fake_generate(prompt, system_prompt=None, label="", on_token=None, model=None, **kw):
        seen.update(prompt=prompt, system=system_prompt, model=model)
        return "resposta"

    retrieval = RetrievalResult(query=AnalyzedQuery(original_query="Q?"), closed_book=True,
                                generation_model="x/strong")
    with patch.object(synthesizer, "generate_text", fake_generate):
        out = synthesize(retrieval)
    assert out.answer == "resposta" and out.context == "" and out.sources == []
    assert seen["model"] == "x/strong"
    assert "Contexto" not in seen["prompt"] and "Não tens acesso aos documentos" in seen["system"]


def test_the_variant_model_reaches_the_grounded_answer_too():
    seen = {}

    def fake_generate(prompt, system_prompt=None, label="", on_token=None, model=None, **kw):
        seen["model"] = model
        return "resposta"

    retrieval = RetrievalResult(query=AnalyzedQuery(original_query="Q?"), results=[_result("PS")],
                                generation_model="x/strong")
    with patch.object(synthesizer, "generate_text", fake_generate):
        synthesize(retrieval)
    assert seen["model"] == "x/strong"
