import pytest

from src.rag.indexing.bm25 import Bm25Index, parse_tsvector


@pytest.mark.unit
def test_parse_tsvector_counts_positions_and_unescapes():
    assert parse_tsvector("'tourad':4,9 'é':1 'd''hondt':2 'pan'") == {"tourad": 2, "é": 1, "d'hondt": 1, "pan": 1}
    assert parse_tsvector("") == {}


def _index():
    # 'é' is everywhere, 'tourad' in one chunk only
    return Bm25Index([
        ("bulls", {"é": 1, "tourad": 2, "abol": 1}),
        ("press", {"é": 3, "posiçã": 2, "jornal": 4}),
        ("health", {"é": 2, "posiçã": 1, "sns": 3}),
    ])


@pytest.mark.unit
def test_rare_term_beats_common_ones_and_any_term_matches():
    ranked = _index().top_k(["é", "posiçã", "pan", "tourad"], k=3)
    assert ranked[0][0] == "bulls"  # one rare match outweighs several common ones
    assert {doc for doc, _ in ranked} == {"bulls", "press", "health"}  # OR semantics


@pytest.mark.unit
def test_allowed_ids_filter_and_unknown_terms():
    idx = _index()
    assert [d for d, _ in idx.top_k(["tourad", "posiçã"], k=5, allowed={"press"})] == ["press"]
    assert idx.top_k(["inexistente"], k=5) == []
    assert idx.idf("é") < idx.idf("tourad")
