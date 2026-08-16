import pytest
from pydantic import ValidationError

from src.rag.common.models import (
    AnalyzedQuery,
    Chunk,
    Coverage,
    QueryType,
    get_party_info,
)


@pytest.mark.unit
def test_get_party_info():
    info = get_party_info("livre-2024-manual.md")
    assert info["name"] == "LIVRE"
    assert info["ideology"] == "left"


@pytest.mark.unit
def test_unknown_party():
    info = get_party_info("random-file.md")
    assert info["name"] == "Unknown"


@pytest.mark.unit
def test_chunk_model_defaults():
    chunk = Chunk(content="teste")
    assert chunk.topics == ["outros"]
    assert chunk.party_name == "Unknown"
    assert chunk.id


@pytest.mark.unit
def test_analyzed_query_model():
    query = AnalyzedQuery(
        original_query="test",
        parties=["PS", "CHEGA"],
    )
    assert query.query_type == QueryType.COMPARISON
    assert len(query.parties) == 2


@pytest.mark.unit
@pytest.mark.parametrize(
    "parties, coverage, topics, expected",
    [
        (["PS"], Coverage.BEST_MATCH, [], QueryType.SINGLE_PARTY),
        (["PS"], Coverage.EXHAUSTIVE, [], QueryType.SINGLE_PARTY),
        (["PS", "CHEGA"], Coverage.BEST_MATCH, [], QueryType.COMPARISON),
        ([], Coverage.EXHAUSTIVE, ["saude"], QueryType.COMPARISON),
        ([], Coverage.BEST_MATCH, ["saude"], QueryType.TOPIC_EXPLORATION),
        ([], Coverage.BEST_MATCH, [], QueryType.GENERAL),
    ],
)
def test_query_type_is_derived(parties, coverage, topics, expected):
    """The route label follows from the party set and the coverage requirement.

    Naming two parties implies the fan-out whatever coverage says; exhaustive
    coverage over a one-party set is just that party's search.
    """
    query = AnalyzedQuery(
        original_query="test", parties=parties, coverage=coverage, topics=topics
    )
    assert query.query_type == expected


@pytest.mark.unit
def test_query_type_cannot_be_set():
    """It is derived, so passing one in is a mistake worth surfacing."""
    with pytest.raises(ValidationError):
        AnalyzedQuery(original_query="test", query_type=QueryType.COMPARISON)
