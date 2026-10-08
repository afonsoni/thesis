import pytest

from src.rag.common.models import (
    AnalyzedQuery,
    Coverage,
    QueryType,
)

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
