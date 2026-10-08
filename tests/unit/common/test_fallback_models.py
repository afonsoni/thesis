import pytest

from src.rag.common import llm_transport as t


@pytest.mark.unit
def test_fallback_chain_starts_with_requested_model_without_repeats(monkeypatch):
    monkeypatch.setattr(t.config, "get", lambda key, default=None: (
        ["google/gemma-4-31b-it:free", "nvidia/nemotron-3-ultra-550b-a55b:free"]
        if key == "llm.openrouter.fallback_models" else default))
    assert t._fallback_models("google/gemma-4-31b-it:free") == [
        "google/gemma-4-31b-it:free", "nvidia/nemotron-3-ultra-550b-a55b:free"]
    assert t._fallback_models("x/y")[0] == "x/y"
