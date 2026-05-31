from unittest.mock import patch

import pytest

import src.rag.retrieval.pipeline as retrieval_pipeline
from src.rag.generation.pipeline import generate
from src.rag.retrieval.pipeline import retrieve
from src.rag.retrieval.query_analyzer import _QueryAnalysisResponse


@pytest.mark.integration
def test_retrieve_single_party_with_test_db(seeded_searcher):
    retrieval_pipeline._searcher = seeded_searcher
    structured = _QueryAnalysisResponse(
        query_type="single_party",
        parties=["Partido Socialista"],
        topics=["educacao"],
        ideology_filter=None,
        reformulated_query="educacao partido socialista",
    )

    with patch("src.rag.retrieval.query_analyzer.generate_structured", return_value=structured):
        result = retrieve("Quais sao as propostas do PS para educacao?", top_k=3, expand_queries=False)

    assert result.results
    assert all(item.party_name == "Partido Socialista" for item in result.results)
    assert all("educacao" in item.topics for item in result.results)


@pytest.mark.integration
def test_retrieve_then_generate_with_mocked_llm(seeded_searcher):
    retrieval_pipeline._searcher = seeded_searcher
    structured = _QueryAnalysisResponse(
        query_type="single_party",
        parties=["Partido Socialista"],
        topics=["saude"],
        ideology_filter=None,
        reformulated_query="saude partido socialista",
    )

    with patch("src.rag.retrieval.query_analyzer.generate_structured", return_value=structured):
        retrieval_result = retrieve("Quais sao as propostas do PS para saude?", top_k=3, expand_queries=False)

    with patch("src.rag.generation.synthesizer.generate_text", return_value="Resposta sintetizada de teste"):
        answer = generate(retrieval_result)

    assert answer.answer == "Resposta sintetizada de teste"
    assert answer.sources
    assert all(source["party"] == "Partido Socialista" for source in answer.sources)
