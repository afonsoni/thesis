from unittest.mock import patch

import pytest

import src.rag.retrieval.pipeline as retrieval_pipeline
from src.rag.retrieval.pipeline import retrieve
from src.rag.retrieval.query_analyzer import _QueryAnalysisResponse


@pytest.mark.integration
def test_retrieve_single_party_with_test_db(seeded_searcher, monkeypatch):
    monkeypatch.setattr(retrieval_pipeline, "get_searcher", lambda table=None: seeded_searcher)
    structured = _QueryAnalysisResponse(
        parties=["Partido Socialista"],
        coverage="best_match",
        topics=["educacao"],
        answer_shape="narrative",
        reformulated_query="educacao partido socialista",
    )

    with patch("src.rag.retrieval.query_analyzer.generate_structured", return_value=structured):
        result = retrieve("Quais sao as propostas do PS para educacao?", top_k=3, expand_queries=False)

    assert result.results
    assert all(item.party_name == "Partido Socialista" for item in result.results)
    assert all("educacao" in item.topics for item in result.results)
