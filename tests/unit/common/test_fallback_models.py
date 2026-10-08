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


class _Resp:
    def __init__(self, status, body):
        self.status_code, self._body, self.headers = status, body, {}
        self.text = str(body)

    def json(self):
        return self._body


@pytest.mark.unit
def test_chain_longer_than_three_goes_out_in_groups(monkeypatch):
    import json

    chain = ["a/1:free", "b/2:free", "c/3:free", "d/4:free"]
    monkeypatch.setenv("OPENROUTER_API_KEY", "k")
    monkeypatch.setattr(t, "_fallback_models", lambda model: chain)
    sent = []

    def post(url, headers, data, timeout):
        body = json.loads(data)
        sent.append((body["model"], body.get("models")))
        if len(sent) == 1:  # every model of the first group failed
            return _Resp(429, {"error": "rate limited"})
        return _Resp(200, {"model": "d/4:free", "choices": [{"message": {"content": "ok"}}]})

    monkeypatch.setattr(t.requests, "post", post)
    t.MODEL_USAGE.clear()
    assert t._call_openrouter_once("p", "a/1:free", 0.0, 10, None, 5, None, None) == "ok"
    assert sent == [("a/1:free", ["a/1:free", "b/2:free", "c/3:free"]), ("d/4:free", None)]
    assert t.MODEL_USAGE == {"d/4:free": 1}
