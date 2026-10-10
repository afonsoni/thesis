import pytest

from src.rag.common import llm_transport as t


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
    assert t._call_openrouter_once("p", "a/1:free", 0.0, 10, None, 5, None) == "ok"
    assert sent == [("a/1:free", ["a/1:free", "b/2:free", "c/3:free"]), ("d/4:free", None)]
    assert t.MODEL_USAGE == {"d/4:free": 1}


@pytest.mark.parametrize("text, secs", [
    ("Please retry in 37.1s.", 37.1),
    ('"retryDelay": "37s"', 37.0),
    ("retry-after: 5", 5.0),
    ("retrying soon, limit: 20", None),  # "retrying" is not a delay
])


def test_retry_after_is_read_from_provider_text(text, secs):
    assert t._parse_retry_after_from_text(text) == secs


def test_each_call_is_logged_with_its_step_and_the_model_that_answered(monkeypatch):
    from src.rag.common import llm_client

    def fake_transport(**kwargs):
        t._LAST_ANSWER.model = "nvidia/nemotron-3-ultra-550b-a55b:free"  # a fallback answered
        return "ok"

    monkeypatch.setattr(llm_client, "call_openrouter_with_retries", fake_transport)
    first = len(llm_client.CALL_LOG)
    llm_client.generate_text("p", model="google/gemma-4-26b-a4b-it:free", label="query expansion")
    assert llm_client.CALL_LOG[first:] == [("query expansion", "nvidia/nemotron-3-ultra-550b-a55b:free")]


def test_an_answer_cut_off_at_max_tokens_is_marked_truncated(monkeypatch):
    from src.rag.common import llm_client

    monkeypatch.setenv("OPENROUTER_API_KEY", "k")
    monkeypatch.setattr(t, "_fallback_models", lambda model: [model])
    monkeypatch.setattr(t.requests, "post", lambda url, headers, data, timeout: _Resp(200, {
        "model": "a/1:free", "choices": [{"message": {"content": "metade da"}, "finish_reason": "length"}]}))
    first = len(llm_client.CALL_LOG)
    assert llm_client.generate_text("p", model="a/1:free", label="answer") == "metade da"
    assert llm_client.CALL_LOG[first:] == [("answer [truncated]", "a/1:free")]


def test_a_missing_api_key_fails_at_once_instead_of_being_retried(monkeypatch):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    monkeypatch.setattr(t.time, "sleep", lambda s: pytest.fail("a missing key is not transient"))
    with pytest.raises(t.OpenRouterTransportError, match="OPENROUTER_API_KEY"):
        t.call_openrouter_with_retries("p", "a/1:free")
