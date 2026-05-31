import pytest

from src.rag.common.models import SearchResult
from src.rag.retrieval.searcher import reciprocal_rank_fusion


@pytest.mark.unit
def test_basic_fusion():
    result_1 = SearchResult(id="a", content="doc A", similarity=0.9)
    result_2 = SearchResult(id="b", content="doc B", similarity=0.8)
    result_3 = SearchResult(id="a", content="doc A", similarity=0.7)
    result_4 = SearchResult(id="c", content="doc C", similarity=0.6)

    fused = reciprocal_rank_fusion([[result_1, result_2], [result_3, result_4]], k=60)
    assert fused[0].id == "a"
    assert len(fused) == 3


@pytest.mark.unit
def test_empty_lists():
    assert reciprocal_rank_fusion([]) == []
    assert reciprocal_rank_fusion([[]]) == []
