"""
Low-level OpenRouter transport helpers.

This module centralizes:
- HTTP request/response handling
- Retry policy for transient failures and rate limits
- OpenRouter error normalization
"""

import json
import logging
import os
import random
import re
import threading
import time
from collections import Counter
from typing import Any, Callable, Dict, List, Mapping, Optional

import requests

from src.utils.config_loader import config

logger = logging.getLogger(__name__)
progress = logging.getLogger("rag.progress")  # see retrieval/pipeline.py

OPENROUTER_CHAT_COMPLETIONS_URL = "https://openrouter.ai/api/v1/chat/completions"

# Retry/​give-up messages carry the provider's error text, which for a rate limit
# includes the quota JSON. Truncate so a long payload cannot dominate the log.
_ERROR_LOG_MAX_CHARS = 300

_MAX_RETRIES = int(config.get("llm.openrouter.max_retries"))
_BASE_BACKOFF_SECS = float(config.get("llm.openrouter.base_backoff_secs"))
_MAX_BACKOFF_SECS = float(config.get("llm.openrouter.max_backoff_secs"))


# Which model actually answered, per model id. With fallbacks configured the
# answering model can differ from the requested one; evaluation snapshots this
# so a run can report how often a fallback was used (e.g. by the judge).
MODEL_USAGE: Counter = Counter()

# The model that answered this thread's latest successful call, read back by
# ``llm_client.generate_text`` to label the call. Per thread because eval runs
# each pipeline stage in a ``with_deadline`` worker thread.
_LAST_ANSWER = threading.local()


def last_answering_model() -> Optional[str]:
    return getattr(_LAST_ANSWER, "model", None)


def last_answer_truncated() -> bool:
    """Whether that call stopped at ``max_tokens``, i.e. its text is cut off."""
    return getattr(_LAST_ANSWER, "truncated", False)


def last_usage() -> Dict[str, Any]:
    """That call's ``usage`` block: ``prompt_tokens``, ``completion_tokens`` and
    ``cost`` (USD, 0 on free models), which OpenRouter returns on every response."""
    return getattr(_LAST_ANSWER, "usage", None) or {}


_MAX_MODELS_PER_REQUEST = 3  # OpenRouter rejects a longer `models` array (400)


def _fallback_models(model: str) -> List[str]:
    """``model`` followed by the configured fallbacks, without repeats."""
    chain = [model, *list(config.get("llm.openrouter.fallback_models", []) or [])]
    return list(dict.fromkeys(chain))


class OpenRouterTransportError(RuntimeError):
    """Structured transport error used by higher-level callers."""

    def __init__(self, message: str, status_code: Optional[int] = None, retry_after: Optional[float] = None):
        super().__init__(message)
        self.status_code = status_code
        self.retry_after = retry_after


def call_openrouter_with_retries(
    prompt: str,
    model: str,
    temperature: float = 0.3,
    max_tokens: int = 1500,
    system_prompt: Optional[str] = None,
    timeout_seconds: int = 120,
    response_format: Optional[Dict[str, Any]] = None,
    on_token: Optional[Callable[[str], None]] = None,
    fallback_models: Optional[List[str]] = None,
    provider_sort: Optional[str] = None,
    reasoning: Optional[bool] = None,
) -> str:
    """Call OpenRouter, retrying transient failures with jittered exponential backoff.

    With *on_token* the answer is streamed: each piece of text is passed to it as
    it arrives, and the whole text is still returned. A stream that breaks off is
    retried from the start, so *on_token* may see a partial answer, then a new one.

    ``fallback_models``, ``provider_sort`` and ``reasoning`` override the
    ``llm.openrouter.*`` config for this call: an empty fallback list means the
    requested model answers or the call fails, and ``reasoning=False`` turns a
    hybrid-reasoning model's thinking off so it is not billed as output.
    """
    for attempt in range(_MAX_RETRIES):
        try:
            return _call_openrouter_once(
                prompt=prompt,
                model=model,
                temperature=temperature,
                max_tokens=max_tokens,
                system_prompt=system_prompt,
                timeout_seconds=timeout_seconds,
                response_format=response_format,
                on_token=on_token,
                fallback_models=fallback_models,
                provider_sort=provider_sort,
                reasoning=reasoning,
            )
        except OpenRouterTransportError as exc:
            retriable = _is_retriable_error(exc)
            if attempt == _MAX_RETRIES - 1 or not retriable:
                # Logged here: otherwise exhausting retries on a slow provider looks
                # like a hang until the error surfaces, attempts * timeout later.
                logger.warning(
                    "OpenRouter call failed on attempt %d/%d and will not be retried (%s): %s",
                    attempt + 1, _MAX_RETRIES,
                    "retries exhausted" if retriable else "not retriable",
                    _truncate_error(exc),
                )
                raise
            retry_after = exc.retry_after
            backoff = random.uniform(0.0, min(_MAX_BACKOFF_SECS, _BASE_BACKOFF_SECS * (2 ** attempt)))
            wait_for = max(retry_after, backoff) if retry_after is not None else backoff
            logger.warning(
                "OpenRouter call failed on attempt %d/%d, retrying in %.1fs%s: %s",
                attempt + 1, _MAX_RETRIES, wait_for,
                f" (provider asked for {retry_after:.0f}s)" if retry_after is not None else "",
                _truncate_error(exc),
            )
            progress.info("O modelo não respondeu (%s); nova tentativa dentro de %.0f s…",
                          exc.status_code or type(exc).__name__, wait_for)
            time.sleep(wait_for)
    raise OpenRouterTransportError("llm.openrouter.max_retries must be at least 1.")


def _call_openrouter_once(
    prompt: str,
    model: str,
    temperature: float,
    max_tokens: int,
    system_prompt: Optional[str],
    timeout_seconds: int,
    response_format: Optional[Dict[str, Any]],
    on_token: Optional[Callable[[str], None]] = None,
    fallback_models: Optional[List[str]] = None,
    provider_sort: Optional[str] = None,
    reasoning: Optional[bool] = None,
) -> str:
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:  # 401: not transient, so neither retried nor waited out as one
        raise OpenRouterTransportError("Missing OPENROUTER_API_KEY.", status_code=401)

    messages: List[Dict[str, str]] = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    payload: Dict[str, Any] = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    if response_format:
        payload["response_format"] = response_format
    if provider_sort is None:
        provider_sort = config.get("llm.openrouter.provider_sort")
    if provider_sort:
        payload["provider"] = {"sort": provider_sort}
    if reasoning is False:
        payload["reasoning"] = {"enabled": False}

    # OpenRouter model fallbacks: on any error from one model (rate limit,
    # downtime, context length) it tries the next in ``models``. It accepts at
    # most 3 there, so a longer chain goes out in groups of 3, the next group
    # only once every model in the previous one has failed.
    chain = _fallback_models(model) if fallback_models is None else list(dict.fromkeys([model, *fallback_models]))
    last_error: Optional[Exception] = None
    for start in range(0, len(chain), _MAX_MODELS_PER_REQUEST):
        group = chain[start:start + _MAX_MODELS_PER_REQUEST]
        payload["model"] = group[0]
        if len(group) > 1:
            payload["models"] = group
        else:
            payload.pop("models", None)
        try:
            return _post_chat(payload, api_key, timeout_seconds, requested=group[0], on_token=on_token)
        except OpenRouterTransportError as exc:
            if exc.status_code in (401, 403):  # bad key: no model will do better
                raise
            last_error = exc
            if start + _MAX_MODELS_PER_REQUEST < len(chain):
                logger.warning("Models %s all failed (%s); trying %s.", group, _truncate_error(exc),
                               chain[start + _MAX_MODELS_PER_REQUEST:])
    raise last_error  # type: ignore[misc]


def _post_chat(payload: Dict[str, Any], api_key: str, timeout_seconds: int, requested: str,
               on_token: Optional[Callable[[str], None]] = None) -> str:
    """POST one chat completion; return its text or raise ``OpenRouterTransportError``.
    With *on_token*, stream it (see ``call_openrouter_with_retries``)."""
    stream = on_token is not None
    try:
        response = requests.post(
            url=OPENROUTER_CHAT_COMPLETIONS_URL,
            headers=_openrouter_headers(api_key),
            data=json.dumps({**payload, "stream": True} if stream else payload),
            timeout=timeout_seconds,  # with a stream: the longest gap between chunks
            stream=stream,
        )
    except requests.RequestException as exc:
        raise OpenRouterTransportError(f"OpenRouter request failed: {exc}") from exc

    if response.status_code >= 400:
        excerpt = response.text[:500]
        retry_after = _parse_retry_after_from_headers(response.headers)
        if retry_after is None:
            # The full body: Google's retryDelay sits past the excerpt's cut-off.
            retry_after = _parse_retry_after_from_text(response.text)
        raise OpenRouterTransportError(
            f"OpenRouter request failed ({response.status_code}): {excerpt}",
            status_code=response.status_code,
            retry_after=retry_after,
        )

    try:
        data = _read_stream(response, on_token) if stream else response.json()
        choice = data["choices"][0]
        message = choice["message"]["content"]
    except OpenRouterTransportError:
        raise
    except Exception as exc:
        detail = f"stream broke off ({exc})" if stream else response.text[:500]
        raise OpenRouterTransportError(f"Unexpected OpenRouter response: {detail}") from exc

    answered_by = str(data.get("model") or requested)
    MODEL_USAGE[answered_by] += 1
    _LAST_ANSWER.model = answered_by
    _LAST_ANSWER.usage = data.get("usage") or {}
    # A cut-off answer comes back as a normal 200 with whatever text fit, so it
    # would otherwise pass for a complete one.
    _LAST_ANSWER.truncated = str(choice.get("finish_reason") or "").lower() in ("length", "max_tokens")
    if _LAST_ANSWER.truncated:
        logger.warning("%s stopped at max_tokens=%s: the answer is cut off.",
                       answered_by, payload.get("max_tokens"))
    if not answered_by.startswith(requested.split(":")[0]):
        logger.info("Answered by fallback model %s (requested %s).", answered_by, requested)

    if isinstance(message, str):
        return message.strip()
    return json.dumps(message, ensure_ascii=False)


def _read_stream(response: requests.Response, on_token: Callable[[str], None]) -> Dict[str, Any]:
    """Read a server-sent-event chat stream, passing each text delta to *on_token*,
    and return it shaped like a non-streamed response (the last chunk has ``usage``)."""
    parts: List[str] = []
    model = usage = finish = None
    for raw in response.iter_lines():
        line = raw.decode("utf-8")  # decoded here: requests would assume latin-1 for SSE
        if not line.startswith("data: "):
            continue  # blank separators and ": OPENROUTER PROCESSING" keep-alives
        if line == "data: [DONE]":
            break
        chunk = json.loads(line[len("data: "):])
        if "error" in chunk:  # a failure after the 200 arrives inside the stream
            raise OpenRouterTransportError(f"OpenRouter stream failed: {chunk['error']}")
        model = chunk.get("model") or model
        usage = chunk.get("usage") or usage
        choice = (chunk.get("choices") or [{}])[0]
        delta = (choice.get("delta") or {}).get("content")
        if delta:
            parts.append(delta)
            on_token(delta)
        finish = choice.get("finish_reason") or finish
    return {"model": model, "usage": usage,
            "choices": [{"message": {"content": "".join(parts)}, "finish_reason": finish}]}


def _openrouter_headers(api_key: str) -> Dict[str, str]:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    site_url = os.getenv("OPENROUTER_SITE_URL")
    app_name = os.getenv("OPENROUTER_APP_NAME")
    if site_url:
        headers["HTTP-Referer"] = site_url
    if app_name:
        headers["X-OpenRouter-Title"] = app_name
    return headers


def _parse_retry_after_from_headers(headers: Mapping[str, str]) -> Optional[float]:
    value = headers.get("Retry-After") or headers.get("retry-after")
    if not value:
        return None
    try:
        return max(0.0, float(value))
    except ValueError:
        return None


def _parse_retry_after_from_text(text: str) -> Optional[float]:
    patterns = [
        r"retry(?:[_ ]?delay|[_ ]?in\b)[^\d]{0,20}(\d+(?:\.\d+)?)",  # retryDelay, retry_delay, retryIn, "retry in 37.1s"
        r"retry[-_ ]?after[^\d]*(\d+(?:\.\d+)?)",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return float(match.group(1))
    return None


def _truncate_error(exc: Exception) -> str:
    """One-line, length-capped rendering of an exception for retry logs."""
    text = " ".join(str(exc).split())
    if len(text) > _ERROR_LOG_MAX_CHARS:
        text = text[:_ERROR_LOG_MAX_CHARS] + "…"
    return f"{type(exc).__name__}: {text}" if text else type(exc).__name__


def _is_retriable_error(exc: OpenRouterTransportError) -> bool:
    """Network failures (no status), timeouts/conflicts/rate limits, and 5xx."""
    code = exc.status_code
    return code is None or code in (408, 409, 429) or 500 <= code < 600
