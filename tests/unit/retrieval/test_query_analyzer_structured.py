from unittest.mock import patch

import pytest

from src.rag.common.models import QueryType
from src.rag.retrieval.query_analyzer import _QueryAnalysisResponse, analyze_query


@pytest.mark.unit
def test_analyze_query_structured_path_uses_llm_output():
    structured = _QueryAnalysisResponse(
        query_type="single_party",
        parties=["PS"],
        topics=["educacao"],
        ideology_filter=None,
        reformulated_query="propostas do partido socialista para a educacao",
    )

    with patch("src.rag.retrieval.query_analyzer.generate_structured", return_value=structured):
        analyzed = analyze_query("Quais as propostas do PS para educacao?")

    assert analyzed.query_type == QueryType.SINGLE_PARTY
    assert analyzed.parties == ["Partido Socialista"]
    assert analyzed.topics == ["educacao"]
    assert "partido socialista" in analyzed.reformulated_query


@pytest.mark.unit
def test_analyze_query_falls_back_when_structured_fails():
    with patch("src.rag.retrieval.query_analyzer.generate_structured", side_effect=RuntimeError("boom")):
        analyzed = analyze_query("Comparar PS e CHEGA sobre saude")

    assert analyzed.query_type == QueryType.COMPARISON
    assert len(analyzed.parties) >= 2
