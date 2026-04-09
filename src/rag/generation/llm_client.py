"""
Unified LLM client using OpenRouter as the runtime transport layer.

All modules should call this file for LLM access instead of creating provider
clients directly. Model selection is done per call and can target any
model exposed by OpenRouter.
"""

import json
import logging
import os
import re
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv
from pydantic import BaseModel

from src.utils.config_loader import config

load_dotenv()
logger = logging.getLogger(__name__)

OPENROUTER_CHAT_COMPLETIONS_URL = "https://openrouter.ai/api/v1/chat/completions"


# ---------------------------------------------------------------------------
# OpenRouter transport
# ---------------------------------------------------------------------------

def _call_openrouter(
    prompt: str,
    model: str,
    temperature: float = 0.3,
    max_tokens: int = 1500,
    system_prompt: Optional[str] = None,
    timeout_seconds: int = 120,
    force_json_output: bool = False,
) -> str:
    """Call OpenRouter chat completions and return assistant text content."""
    import requests

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("Missing OPENROUTER_API_KEY.")

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
    if force_json_output:
        payload["response_format"] = {"type": "json_object"}

    response = requests.post(
        url=OPENROUTER_CHAT_COMPLETIONS_URL,
        headers=_openrouter_headers(api_key),
        data=json.dumps(payload),
        timeout=timeout_seconds,
    )
    if response.status_code >= 400:
        raise RuntimeError(
            f"OpenRouter request failed ({response.status_code}): {response.text[:500]}"
        )

    data = response.json()
    try:
        message = data["choices"][0]["message"]["content"]
    except Exception as exc:
        raise RuntimeError(f"Unexpected OpenRouter response: {data}") from exc

    if isinstance(message, str):
        return message.strip()
    # Some providers may return non-string message content segments.
    return json.dumps(message, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Public high-level API
# ---------------------------------------------------------------------------

def generate_text(
    prompt: str,
    system_prompt: Optional[str] = None,
    temperature: float = 0.3,
    max_tokens: int = 1500,
    provider: Optional[str] = None,
    model: Optional[str] = None,
    timeout_seconds: int = 120,
) -> str:
    """Generate text through OpenRouter transport.

    The provider parameter is retained for backwards compatibility; only
    ``openrouter`` is supported at runtime.
    """
    if provider and provider not in ("openrouter", "auto"):
        logger.warning(
            "Provider '%s' is no longer a direct runtime option. Using OpenRouter transport.",
            provider,
        )

    selected_model = model or config.get(
        "llm.openrouter.model",
        "meta-llama/llama-3.3-70b-instruct",
    )
    return _call_openrouter(
        prompt=prompt,
        model=selected_model,
        temperature=temperature,
        max_tokens=max_tokens,
        system_prompt=system_prompt,
        timeout_seconds=timeout_seconds,
    )


def generate_structured(
    prompt: str,
    response_schema: type,
    system_prompt: Optional[str] = None,
    temperature: float = 0.1,
    model: Optional[str] = None,
    max_tokens: int = 1500,
    timeout_seconds: int = 120,
) -> Any:
    """Generate structured JSON and validate with an optional Pydantic schema."""
    raw = generate_text(
        (
            prompt
            + "\n\nResponde APENAS com JSON valido que cumpra o schema pedido."
        ),
        system_prompt=system_prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        provider="openrouter",
        model=model,
        timeout_seconds=timeout_seconds,
    )

    data = _extract_json_payload(raw)
    if isinstance(response_schema, type) and issubclass(response_schema, BaseModel):
        return response_schema.model_validate(data)
    return data


def generate_structured_batch(
    prompt: str,
    item_schema: Optional[type] = None,
    system_prompt: Optional[str] = None,
    temperature: float = 0.1,
    model: Optional[str] = None,
    max_tokens: int = 2000,
    timeout_seconds: int = 120,
) -> List[Any]:
    """Generate a JSON array and optionally validate each item schema."""
    raw = generate_text(
        (
            prompt
            + "\n\nResponde APENAS com um array JSON valido na ordem pedida."
        ),
        system_prompt=system_prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        provider="openrouter",
        model=model,
        timeout_seconds=timeout_seconds,
    )

    data = _extract_json_payload(raw)
    if not isinstance(data, list):
        data = [data]

    if item_schema and isinstance(item_schema, type) and issubclass(item_schema, BaseModel):
        return [item_schema.model_validate(item) for item in data]
    return data


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

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


def _extract_json_payload(raw_text: str) -> Any:
    """Extract and decode JSON payload from raw model text."""
    candidates = [raw_text.strip()]

    fenced = re.findall(r"```(?:json)?\s*([\s\S]*?)```", raw_text, flags=re.IGNORECASE)
    candidates.extend(item.strip() for item in fenced if item.strip())

    for candidate in candidates:
        try:
            return json.loads(candidate)
        except json.JSONDecodeError:
            pass

    decoder = json.JSONDecoder()
    for idx, ch in enumerate(raw_text):
        if ch not in "[{":
            continue
        try:
            obj, _ = decoder.raw_decode(raw_text[idx:])
            return obj
        except json.JSONDecodeError:
            continue

    raise ValueError(f"Could not parse JSON from model response: {raw_text[:400]}")
