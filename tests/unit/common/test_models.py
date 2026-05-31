import pytest

from src.rag.common.models import AnalyzedQuery, Chunk, QueryType, get_party_info


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
        query_type=QueryType.COMPARISON,
        parties=["PS", "CHEGA"],
    )
    assert query.query_type == QueryType.COMPARISON
    assert len(query.parties) == 2
