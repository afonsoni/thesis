import pytest

from src.rag.common.models import QueryType
from src.rag.retrieval.query_analyzer import _fallback_analysis


@pytest.mark.unit
def test_comparison_detection():
    query = _fallback_analysis("Comparar as politicas do PS e do CHEGA sobre saude")
    assert query.query_type == QueryType.COMPARISON


@pytest.mark.unit
def test_single_party_detection():
    query = _fallback_analysis("O que propoe o LIVRE sobre habitacao?")
    assert query.query_type == QueryType.SINGLE_PARTY
    assert any("LIVRE" in party for party in query.parties)


@pytest.mark.unit
def test_topic_detection():
    query = _fallback_analysis("Quais sao as propostas sobre educacao?")
    assert "educacao" in query.topics


@pytest.mark.unit
def test_general_fallback():
    query = _fallback_analysis("Previsoes para o proximo ano")
    assert query.query_type == QueryType.GENERAL
