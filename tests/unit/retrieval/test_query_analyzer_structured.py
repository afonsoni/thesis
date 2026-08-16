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
def test_exhaustive_coverage_without_parties_derives_a_comparison():
    """The aggregative case: no party named, but every party must be covered."""
    structured = _response(
        coverage="exhaustive",
        topics=["educacao"],
        answer_shape="per_party",
        reformulated_query="posicao de cada partido sobre educacao publica",
    )

    with patch("src.rag.retrieval.query_analyzer.generate_structured", return_value=structured):
        analyzed = analyze_query("O que pensa cada partido sobre a educação pública?")

    assert analyzed.query_type == QueryType.COMPARISON
    assert analyzed.parties == []
    assert analyzed.coverage == Coverage.EXHAUSTIVE


@pytest.mark.unit
def test_bloc_questions_arrive_as_an_enumerated_party_list():
    """Ideology is resolved by the analyzer, not passed down as a filter.

    The router has no ideology branch: a bloc question is indistinguishable
    from one that named the same parties outright.
    """
    structured = _response(
        parties=["CHEGA", "Iniciativa Liberal", "Aliança Democrática"],
        coverage="exhaustive",
        topics=["imigracao"],
        answer_shape="per_party",
    )

    with patch("src.rag.retrieval.query_analyzer.generate_structured", return_value=structured):
        analyzed = analyze_query("Qual a diferença entre os partidos de direita na imigração?")

    assert analyzed.query_type == QueryType.COMPARISON
    assert len(analyzed.parties) == 3


@pytest.mark.unit
def test_best_match_with_topics_stays_a_topic_exploration():
    structured = _response(topics=["habitacao"], reformulated_query="propostas sobre habitacao")

    with patch("src.rag.retrieval.query_analyzer.generate_structured", return_value=structured):
        analyzed = analyze_query("Quais são as propostas sobre habitação?")

    assert analyzed.query_type == QueryType.TOPIC_EXPLORATION


@pytest.mark.unit
def test_exhaustive_coverage_can_still_ask_for_a_single_narrative():
    """Coverage and answer shape are independent — a verdict over every party."""
    structured = _response(
        coverage="exhaustive",
        topics=["habitacao"],
        answer_shape="narrative",
    )

    with patch("src.rag.retrieval.query_analyzer.generate_structured", return_value=structured):
        analyzed = analyze_query("Que partido propõe mais sobre habitação?")

    assert analyzed.coverage == Coverage.EXHAUSTIVE
    assert analyzed.answer_shape == AnswerShape.NARRATIVE


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
