from src.rag.evaluation.variants import VARIANTS
from src.rag.retrieval.config import RetrievalConfig


def test_default_config_reproduces_current_variant():
    """RetrievalConfig() defaults must equal the 'current' production variant."""
    default = RetrievalConfig().model_dump()
    default.pop("name")
    current = VARIANTS["current"].model_dump()
    current.pop("name")
    assert default == current


def test_the_rungs_below_current_search_the_plain_index():
    """Contextual retrieval is the last rung, so every earlier rung must not use it."""
    from src.utils.config_loader import config

    plain = config.get("indexing.plain_table")
    for name in ("naive", "multiquery", "routed", "dense_only", "hybrid", "hybrid_only", "reranked_only"):
        assert VARIANTS[name].table == plain, name
    assert VARIANTS["current"].table is None


def test_closed_book_rungs_differ_from_current_by_retrieval_and_generator_only():
    def without(name, *fields):
        return VARIANTS[name].model_dump(exclude={"name", *fields})

    assert VARIANTS["no_retrieval"].use_retrieval is False
    assert without("no_retrieval", "use_retrieval") == without("current", "use_retrieval")
    assert VARIANTS["current_strong"].generation_model
    assert without("current_strong", "generation_model") == without("current", "generation_model")
