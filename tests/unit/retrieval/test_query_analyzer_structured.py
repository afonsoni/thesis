from unittest.mock import patch

import pytest

from src.rag.common.models import AnswerShape, Coverage, QueryType
from src.rag.retrieval.query_analyzer import _QueryAnalysisResponse, analyze_query


def _response(**overrides) -> _QueryAnalysisResponse:
    base = dict(
        parties=[],
        coverage="best_match",
        topics=[],
        answer_shape="narrative",
        reformulated_query="",
    )
    base.update(overrides)
    return _QueryAnalysisResponse(**base)


@pytest.mark.unit
def test_analyze_query_structured_path_uses_llm_output():
    structured = _response(
        parties=["PS"],
        topics=["educacao"],
        reformulated_query="propostas do partido socialista para a educacao",
    )

    with patch("src.rag.retrieval.query_analyzer.generate_structured", return_value=structured):
        analyzed = analyze_query("Quais as propostas do PS para educacao?")

    assert analyzed.query_type == QueryType.SINGLE_PARTY
    assert analyzed.parties == ["Partido Socialista"]
    assert analyzed.topics == ["educacao"]
    assert "partido socialista" in analyzed.reformulated_query


@pytest.mark.unit
def test_unreadable_coverage_fails_towards_full_coverage():
    """Over-retrieving costs queries; under-retrieving silently drops parties."""
    structured = _response(coverage="dunno", topics=["saude"])

    with patch("src.rag.retrieval.query_analyzer.generate_structured", return_value=structured):
        analyzed = analyze_query("Propostas para o SNS?")

    assert analyzed.coverage == Coverage.EXHAUSTIVE
    assert analyzed.query_type == QueryType.COMPARISON


@pytest.mark.unit
def test_bad_values_are_dropped_field_by_field():
    """One unusable value must not discard the fields the model got right.

    The transport asks for `json_object`, not a constrained schema, so an
    invented topic reaches Pydantic. Rejecting the whole response would throw
    away a correct party list and fall back for no reason.
    """
    structured = _response(
        parties=["PS", "Partido Pirata"],
        topics=["educacao", "gastronomia"],
        answer_shape="bullet_points",
    )

    with patch("src.rag.retrieval.query_analyzer.generate_structured", return_value=structured):
        analyzed = analyze_query("O que propõe o PS para a educação?")

    assert analyzed.parties == ["Partido Socialista"]
    assert analyzed.topics == ["educacao"]
    assert analyzed.answer_shape == AnswerShape.NARRATIVE  # inferred, single party


@pytest.mark.unit
def test_analyze_query_falls_back_when_structured_fails():
    with patch("src.rag.retrieval.query_analyzer.generate_structured", side_effect=RuntimeError("boom")):
        analyzed = analyze_query("Comparar PS e CHEGA sobre saude")

    assert analyzed.query_type == QueryType.COMPARISON
    assert len(analyzed.parties) >= 2


@pytest.mark.unit
def test_strict_config_raises_instead_of_falling_back():
    from src.rag.retrieval.config import RetrievalConfig

    with patch("src.rag.retrieval.query_analyzer.generate_structured", side_effect=RuntimeError("429")):
        with pytest.raises(RuntimeError):
            analyze_query("O que propõe o PS?", config=RetrievalConfig(strict=True))
