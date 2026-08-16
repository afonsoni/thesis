"""The degraded path, used when the analysis call is unavailable.

It establishes only what needs no interpretation — parties are a closed
vocabulary — and fails toward coverage for everything else.
"""

import pytest

from src.rag.common.models import Coverage, QueryType
from src.rag.retrieval.query_analyzer import _fallback_analysis, _normalize_parties


@pytest.mark.unit
def test_named_parties_are_searched():
    query = _fallback_analysis("Comparar as politicas do PS e do CHEGA sobre saude")
    assert query.query_type == QueryType.COMPARISON
    assert query.parties == ["Partido Socialista", "CHEGA"]


@pytest.mark.unit
def test_single_party_detection():
    query = _fallback_analysis("O que propoe o LIVRE sobre habitacao?")
    assert query.query_type == QueryType.SINGLE_PARTY
    assert query.parties == ["LIVRE"]


@pytest.mark.unit
def test_unnamed_question_fans_out_rather_than_guessing():
    """No analysis means no basis to narrow, so the whole corpus is in scope."""
    query = _fallback_analysis("Quais sao as propostas sobre educacao?")
    assert query.coverage == Coverage.EXHAUSTIVE
    assert query.parties == []
    assert query.query_type == QueryType.COMPARISON


@pytest.mark.unit
def test_no_topic_filter_is_guessed():
    """A wrong topic is a hard AND against the index; no topic just costs recall."""
    assert _fallback_analysis("Quais sao as propostas sobre educacao?").topics == []


@pytest.mark.unit
@pytest.mark.parametrize(
    "raw, expected",
    [
        ("PSD", "Aliança Democrática"),
        ("Partido Social Democrata", "Aliança Democrática"),
        ("CDS-PP", "Aliança Democrática"),
        ("CDU", "Partido Comunista Português"),
        ("Bloco", "Bloco de Esquerda"),
        ("Alianca Democratica", "Aliança Democrática"),
        ("ps", "Partido Socialista"),
    ],
)
def test_party_aliases_resolve_to_the_published_programme(raw, expected):
    """Coalition members resolve to the coalition that published the programme.

    "PSD" used to resolve to Partido Socialista: the old substring fallback
    accepted any pair where one string contained the other, and "ps" is inside
    "psd".
    """
    assert _normalize_parties([raw]) == [expected]


@pytest.mark.unit
def test_unknown_party_is_dropped_not_guessed():
    assert _normalize_parties(["Partido Trabalhista"]) == []


@pytest.mark.unit
@pytest.mark.parametrize(
    "question",
    [
        "Quais as propostas para a sociedade portuguesa?",   # "ad" inside "sociedade"
        "O que dizem sobre a verdade e a liberdade?",        # "ad" and "be" inside "liberdade"
        "Propostas sobre igualdade de genero",               # "ad" inside "igualdade"
    ],
)
def test_party_scan_is_word_anchored(question):
    """A party initial buried inside an ordinary word is not a party mention."""
    assert _fallback_analysis(question).parties == []


@pytest.mark.unit
def test_party_scan_finds_aliases_in_the_question():
    query = _fallback_analysis("O que propoe o PSD para a saude?")
    assert query.parties == ["Aliança Democrática"]
    assert query.query_type == QueryType.SINGLE_PARTY
