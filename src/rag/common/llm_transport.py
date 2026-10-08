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
import time
from collections import Counter
from typing import Any, Dict, List, Mapping, Optional

import requests

from src.utils.config_loader import config

logger = logging.getLogger(__name__)

OPENROUTER_CHAT_COMPLETIONS_URL = "https://openrouter.ai/api/v1/chat/completions"

# Retry/​give-up messages carry the provider's error text, which for a rate limit
# includes the quota JSON. Truncate so a long payload cannot dominate the log.
_ERROR_LOG_MAX_CHARS = 300

_DEFAULT_MAX_RETRIES = int(config.get("llm.openrouter.max_retries", 5))
_DEFAULT_BASE_BACKOFF_SECS = float(config.get("llm.openrouter.base_backoff_secs", 1.0))
_DEFAULT_MAX_BACKOFF_SECS = float(config.get("llm.openrouter.max_backoff_secs", 30.0))


# Which model actually answered, per model id. With fallbacks configured the
# answering model can differ from the requested one; evaluation snapshots this
# so a run can report how often a fallback was used (e.g. by the judge).
MODEL_USAGE: Counter = Counter()


def _fallback_models(model: str) -> List[str]:
    """``model`` followed by the configured fallbacks, without repeats."""
    chain = [model, *list(config.get("llm.openrouter.fallback_models", []) or [])]
    return list(dict.fromkeys(chain))


class OpenRouterTransportError(RuntimeError):
    """Structured transport error used by higher-level callers."""

    def __init__(
        self,
        message: str,
        status_code: Optional[int] = None,
        retry_after: Optional[float] = None,
        response_excerpt: str = "",
    ):
        super().__init__(message)
        self.status_code = status_code
        self.retry_after = retry_after
        self.response_excerpt = response_excerpt


def call_openrouter_with_retries(
    prompt: str,
    model: str,
    temperature: float = 0.3,
    max_tokens: int = 1500,
    system_prompt: Optional[str] = None,
    timeout_seconds: int = 120,
    response_format: Optional[Dict[str, Any]] = None,
    extra_body: Optional[Dict[str, Any]] = None,
    max_retries: Optional[int] = None,
    base_backoff_secs: Optional[float] = None,
    max_backoff_secs: Optional[float] = None,
) -> str:
    """Call OpenRouter with centralized retry/backoff policy."""
    attempts = max_retries if max_retries is not None else _DEFAULT_MAX_RETRIES
    base_backoff = base_backoff_secs if base_backoff_secs is not None else _DEFAULT_BASE_BACKOFF_SECS
    max_backoff = max_backoff_secs if max_backoff_secs is not None else _DEFAULT_MAX_BACKOFF_SECS

    last_error: Optional[Exception] = None
    for attempt in range(attempts):
        try:
            return _call_openrouter_once(
                prompt=prompt,
                model=model,
                temperature=temperature,
                max_tokens=max_tokens,
                system_prompt=system_prompt,
                timeout_seconds=timeout_seconds,
                response_format=response_format,
                extra_body=extra_body,
            )
        except Exception as exc:
            last_error = exc
            if attempt >= attempts - 1 or not _is_retriable_error(exc):
                # Without this, exhausting retries on a slow provider is
                # indistinguishable from a hang: the caller only logs once the
                # final error propagates, which can be attempts * timeout later.
                logger.warning(
                    "OpenRouter call failed on attempt %d/%d and will not be retried "
                    "(%s): %s",
                    attempt + 1,
                    attempts,
                    "retries exhausted" if _is_retriable_error(exc) else "not retriable",
                    _truncate_error(exc),
                )
                break

            retry_after = _extract_retry_after(exc)
            exp_backoff = min(max_backoff, base_backoff * (2 ** attempt))
            jitter_wait = random.uniform(0.0, exp_backoff)
            wait_for = max(retry_after, jitter_wait) if retry_after is not None else jitter_wait
            logger.warning(
                "OpenRouter call failed on attempt %d/%d, retrying in %.1fs%s: %s",
                attempt + 1,
                attempts,
                wait_for,
                f" (provider asked for {retry_after:.0f}s)" if retry_after is not None else "",
                _truncate_error(exc),
            )
            time.sleep(wait_for)

    if last_error is None:
        raise OpenRouterTransportError("OpenRouter call failed without an explicit error.")
    raise last_error


def _call_openrouter_once(
    prompt: str,
    model: str,
    temperature: float,
    max_tokens: int,
    system_prompt: Optional[str],
    timeout_seconds: int,
    response_format: Optional[Dict[str, Any]],
    extra_body: Optional[Dict[str, Any]],
) -> str:
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise OpenRouterTransportError("Missing OPENROUTER_API_KEY.")

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
    chain = _fallback_models(model)
    if len(chain) > 1:
        # OpenRouter model fallbacks: on any error from one model (rate limit,
        # downtime, context length) it tries the next, in this order.
        payload["models"] = chain
    if extra_body:
        payload.update(extra_body)

    try:
        response = requests.post(
            url=OPENROUTER_CHAT_COMPLETIONS_URL,
            headers=_openrouter_headers(api_key),
            data=json.dumps(payload),
            timeout=timeout_seconds,
        )
    except requests.RequestException as exc:
        raise OpenRouterTransportError(f"OpenRouter request failed: {exc}") from exc

    if response.status_code >= 400:
        excerpt = response.text[:500]
        retry_after = _parse_retry_after_from_headers(response.headers)
        if retry_after is None:
            retry_after = _parse_retry_after_from_text(excerpt)
        raise OpenRouterTransportError(
            message=f"OpenRouter request failed ({response.status_code}): {excerpt}",
            status_code=response.status_code,
            retry_after=retry_after,
            response_excerpt=excerpt,
        )

    try:
        data = response.json()
        message = data["choices"][0]["message"]["content"]
    except Exception as exc:
        raise OpenRouterTransportError(f"Unexpected OpenRouter response: {response.text[:500]}") from exc

    answered_by = str(data.get("model") or model)
    MODEL_USAGE[answered_by] += 1
    if not answered_by.startswith(model.split(":")[0]):
        logger.info("Answered by fallback model %s (requested %s).", answered_by, model)

    if isinstance(message, str):
        return message.strip()
    return json.dumps(message, ensure_ascii=False)


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
        r"retry(?:[_ ]?[Dd]elay|In)[^\d]*(\d+(?:\.\d+)?)",
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


def _extract_retry_after(exc: Exception) -> Optional[float]:
    if isinstance(exc, OpenRouterTransportError):
        return exc.retry_after
    return _parse_retry_after_from_text(str(exc))


def _is_retriable_error(exc: Exception) -> bool:
    if isinstance(exc, OpenRouterTransportError):
        if exc.status_code is None:
            return True
        if exc.status_code in (408, 409, 429):
            return True
        return 500 <= exc.status_code < 600

    if isinstance(exc, requests.RequestException):
        return True

    msg = str(exc).lower()
    return "429" in msg or "rate limit" in msg or "resource_exhausted" in msg
