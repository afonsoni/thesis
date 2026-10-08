import pytest

from src.rag.evaluation.variants import VARIANTS
from src.rag.retrieval.config import RetrievalConfig


@pytest.mark.unit
def test_default_config_reproduces_current_variant():
    """RetrievalConfig() defaults must equal the 'current' production variant."""
    default = RetrievalConfig().model_dump()
    default.pop("name")
    current = VARIANTS["current"].model_dump()
    current.pop("name")
    assert default == current
