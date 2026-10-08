import pytest

from src.rag.evaluation.variants import (
    DEFAULT_VARIANTS,
    VARIANTS,
    get_variant,
    resolve_variants,
)
from src.rag.retrieval.config import RetrievalConfig


@pytest.mark.unit
def test_default_config_reproduces_current_variant():
    """RetrievalConfig() defaults must equal the 'current' production variant."""
    default = RetrievalConfig().model_dump()
    default.pop("name")
    current = VARIANTS["current"].model_dump()
    current.pop("name")
    assert default == current


@pytest.mark.unit
def test_naive_variant_disables_all_features():
    naive = VARIANTS["naive"]
    assert not naive.use_query_analysis
    assert not naive.use_routing
    assert not naive.use_multi_query


@pytest.mark.unit
def test_variant_ladder_present_and_resolvable():
    for name in ["naive", "multiquery", "routed", "current"]:
        assert name in VARIANTS
    assert DEFAULT_VARIANTS == ["naive", "current"]
    configs = resolve_variants(["naive", "current"])
    assert [c.name for c in configs] == ["naive", "current"]


@pytest.mark.unit
def test_unknown_variant_raises_helpful_error():
    with pytest.raises(KeyError, match="Unknown variant"):
        get_variant("does-not-exist")
