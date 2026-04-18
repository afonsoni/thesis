"""
Shared high-level LLM client API.

All indexing/retrieval/generation modules should import from this module.
Prompt construction remains in domain modules; this module only handles transport,
JSON parsing, and optional schema validation.
"""

import json
import logging
import re
from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from src.rag.common.llm_transport import call_openrouter_with_retries
from src.utils.config_loader import config

logger = logging.getLogger(__name__)


def generate_text(
    prompt: str,
    system_prompt: Optional[str] = None,
    temperature: float = 0.3,
    max_tokens: int = 1500,
    provider: Optional[str] = None,
    model: Optional[str] = None,
    timeout_seconds: int = 120,
    response_format: Optional[Dict[str, Any]] = None,
    extra_body: Optional[Dict[str, Any]] = None,
) -> str:
    """Generate text through OpenRouter transport with centralized retries."""
    if provider and provider not in ("openrouter", "auto"):
        logger.warning(
            "Provider '%s' is no longer a direct runtime option. Using OpenRouter transport.",
            provider,
        )

    selected_model = model or config.get(
        "llm.openrouter.model",
        "meta-llama/llama-3.3-70b-instruct",
    )
    return call_openrouter_with_retries(
        prompt=prompt,
        model=selected_model,
        temperature=temperature,
        max_tokens=max_tokens,
        system_prompt=system_prompt,
        timeout_seconds=timeout_seconds,
        response_format=response_format,
        extra_body=extra_body,
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
        response_format={"type": "json_object"},
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
        response_format={"type": "json_object"},
    )

    data = _extract_json_payload(raw)
    if not isinstance(data, list):
        data = [data]

    if item_schema and isinstance(item_schema, type) and issubclass(item_schema, BaseModel):
        return [item_schema.model_validate(item) for item in data]
    return data


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
