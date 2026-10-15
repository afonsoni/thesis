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

    def post(url, headers, data, timeout, stream=False):
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
    assert [(c["step"], c["model"]) for c in llm_client.CALL_LOG[first:]] == [
        ("query expansion", "nvidia/nemotron-3-ultra-550b-a55b:free")]


def test_an_answer_cut_off_at_max_tokens_is_marked_truncated(monkeypatch):
    from src.rag.common import llm_client

    monkeypatch.setenv("OPENROUTER_API_KEY", "k")
    monkeypatch.setattr(t, "_fallback_models", lambda model: [model])
    monkeypatch.setattr(t.requests, "post", lambda url, headers, data, timeout, stream=False: _Resp(200, {
        "model": "a/1:free", "choices": [{"message": {"content": "metade da"}, "finish_reason": "length"}],
        "usage": {"prompt_tokens": 120, "completion_tokens": 10, "cost": 0.0003}}))
    first = len(llm_client.CALL_LOG)
    assert llm_client.generate_text("p", model="a/1:free", label="answer") == "metade da"
    (call,) = llm_client.CALL_LOG[first:]
    assert call.pop("secs") >= 0
    assert call == {"step": "answer [truncated]", "model": "a/1:free",
                    "prompt_tokens": 120, "completion_tokens": 10, "cost": 0.0003}


def test_a_streamed_answer_reaches_the_caller_piece_by_piece(monkeypatch):
    import json

    from src.rag.common import llm_client

    chunks = [{"model": "a/1", "choices": [{"delta": {"content": "Olá, "}}]},
              {"model": "a/1", "choices": [{"delta": {"content": "Lisboa"}, "finish_reason": "stop"}],
               "usage": {"prompt_tokens": 9, "completion_tokens": 3, "cost": 0.0001}}]
    lines = [b": OPENROUTER PROCESSING", b""] + [f"data: {json.dumps(c)}".encode() for c in chunks] + [b"data: [DONE]"]

    class _Stream(_Resp):
        def iter_lines(self):
            return iter(lines)

    def post(url, headers, data, timeout, stream=False):
        assert stream and json.loads(data)["stream"]
        return _Stream(200, None)

    monkeypatch.setenv("OPENROUTER_API_KEY", "k")
    monkeypatch.setattr(t, "_fallback_models", lambda model: [model])
    monkeypatch.setattr(t.requests, "post", post)
    seen = []
    first = len(llm_client.CALL_LOG)
    assert llm_client.generate_text("p", model="a/1", label="answer", on_token=seen.append) == "Olá, Lisboa"
    assert seen == ["Olá, ", "Lisboa"]
    (call,) = llm_client.CALL_LOG[first:]
    assert (call["step"], call["prompt_tokens"], call["completion_tokens"], call["cost"]) == ("answer", 9, 3, 0.0001)


def test_a_missing_api_key_fails_at_once_instead_of_being_retried(monkeypatch):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    monkeypatch.setattr(t.time, "sleep", lambda s: pytest.fail("a missing key is not transient"))
    with pytest.raises(t.OpenRouterTransportError, match="OPENROUTER_API_KEY"):
        t.call_openrouter_with_retries("p", "a/1:free")


def test_a_call_can_opt_out_of_fallbacks_provider_sort_and_reasoning(monkeypatch):
    import json

    monkeypatch.setenv("OPENROUTER_API_KEY", "k")
    monkeypatch.setattr(t, "_fallback_models", lambda model: [model, "b/2:free"])
    monkeypatch.setattr(t.config, "get", lambda key, default=None: "throughput"
                        if key == "llm.openrouter.provider_sort" else default)
    sent = []

    def post(url, headers, data, timeout, stream=False):
        sent.append(json.loads(data))
        return _Resp(200, {"model": "a/1", "choices": [{"message": {"content": "ok"}}]})

    monkeypatch.setattr(t.requests, "post", post)
    t._call_openrouter_once("p", "a/1", 0.0, 10, None, 5, None,
                            fallback_models=[], provider_sort="price", reasoning=False)
    body = sent[0]
    assert body["model"] == "a/1" and "models" not in body  # no chain: this model or nothing
    assert body["provider"] == {"sort": "price"}
    assert body["reasoning"] == {"enabled": False}


def test_wait_out_retries_only_the_errors_it_is_told_to(monkeypatch):
    from src.rag.common import llm_client

    monkeypatch.setattr(llm_client.time, "sleep", lambda s: None)
    calls = {"n": 0}

    def bad_reply():
        calls["n"] += 1
        raise ValueError("expected 3 verdicts, got 2")

    with pytest.raises(ValueError):
        llm_client.call_with_wait_out(bad_reply, "judge", attempts=5,
                                      retry_on=(t.OpenRouterTransportError, TimeoutError))
    assert calls["n"] == 1  # deterministic failure: not worth five rounds of sleeping

    def flaky():
        calls["n"] += 1
        if calls["n"] < 3:
            raise t.OpenRouterTransportError("503", status_code=503)
        return "ok"

    calls["n"] = 0
    assert llm_client.call_with_wait_out(flaky, "judge", attempts=5,
                                         retry_on=(t.OpenRouterTransportError, TimeoutError)) == "ok"
    assert calls["n"] == 3


def test_web_search_adds_the_plugin_and_keeps_the_citations(monkeypatch):
    import json

    monkeypatch.setenv("OPENROUTER_API_KEY", "k")
    monkeypatch.setattr(t, "_fallback_models", lambda model: [model])
    monkeypatch.setattr(t.config, "get", lambda key, default=None: 5 if key == "llm.openrouter.web_max_results" else default)
    sent = []
    citation = {"type": "url_citation", "url_citation": {"url": "https://ps.pt/programa", "title": "Programa PS"}}

    def post(url, headers, data, timeout, stream=False):
        sent.append(json.loads(data))
        return _Resp(200, {"model": "a/1", "choices": [{"message": {"content": "ok", "annotations": [citation]}}]})

    monkeypatch.setattr(t.requests, "post", post)
    t._call_openrouter_once("p", "a/1", 0.0, 10, None, 5, None, web_search=True)
    assert sent[0]["plugins"] == [{"id": "web", "max_results": 5}]
    assert t.last_annotations() == [citation]
    t._call_openrouter_once("p", "a/1", 0.0, 10, None, 5, None)
    assert "plugins" not in sent[1]
