"""
Unified LLM client supporting Gemini (primary) and OpenRouter (fallback).

No OpenAI models are used. The ``openai`` SDK is only used as an HTTP client
for the OpenRouter API endpoint.
"""

import logging
import os
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Gemini client
# ---------------------------------------------------------------------------

def _call_gemini(
    prompt: str,
    model: str = "gemini-2.5-flash",
    temperature: float = 0.3,
    max_tokens: int = 1500,
    system_prompt: Optional[str] = None,
    response_schema: Optional[type] = None,
) -> str:
    """Call Google GenAI (Gemini) and return the text response."""
    from google import genai  # lazy import

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    contents = prompt
    if system_prompt:
        contents = f"{system_prompt}\n\n{prompt}"

    config_dict: Dict[str, Any] = {
        "temperature": temperature,
        "max_output_tokens": max_tokens,
    }
    if response_schema is not None:
        config_dict["response_mime_type"] = "application/json"
        config_dict["response_schema"] = response_schema

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=config_dict,
    )
    return response.text.strip()


def _call_gemini_structured(
    prompt: str,
    response_schema: type,
    model: str = "gemini-2.5-flash",
    temperature: float = 0.1,
    system_prompt: Optional[str] = None,
):
    """Call Gemini with structured (Pydantic) JSON output and return the parsed object."""
    from google import genai

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    contents = prompt
    if system_prompt:
        contents = f"{system_prompt}\n\n{prompt}"

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config={
            "temperature": temperature,
            "max_output_tokens": 1500,
            "response_mime_type": "application/json",
            "response_schema": response_schema,
        },
    )
    return response.parsed


# ---------------------------------------------------------------------------
# OpenRouter client (uses the openai SDK as transport)
# ---------------------------------------------------------------------------

def _call_openrouter(
    prompt: str,
    model: str = "meta-llama/llama-3.3-70b-instruct",
    temperature: float = 0.3,
    max_tokens: int = 1500,
    system_prompt: Optional[str] = None,
) -> str:
    """Call OpenRouter and return the text response."""
    from openai import OpenAI  # only used as HTTP client

    client = OpenAI(
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
    )

    messages: List[Dict[str, str]] = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content.strip()


# ---------------------------------------------------------------------------
# Public high-level API
# ---------------------------------------------------------------------------

def generate_text(
    prompt: str,
    system_prompt: Optional[str] = None,
    temperature: float = 0.3,
    max_tokens: int = 1500,
    provider: Optional[str] = None,
) -> str:
    """
    Generate text using the configured LLM provider chain.

    Provider precedence (unless overridden):
      1. **Gemini** (if ``GEMINI_API_KEY`` is set)
      2. **OpenRouter / Llama 3.3 70B** (if ``OPENROUTER_API_KEY`` is set)
      3. Raises ``RuntimeError`` if neither key is available.

    Args:
        prompt: User / context prompt.
        system_prompt: Optional system-level instruction.
        temperature: Sampling temperature.
        max_tokens: Maximum response tokens.
        provider: Force a specific provider (``"gemini"`` or ``"openrouter"``).

    Returns:
        The generated text.
    """
    providers = _resolve_providers(provider)

    last_exc: Optional[Exception] = None
    for prov in providers:
        try:
            if prov == "gemini":
                return _call_gemini(prompt, temperature=temperature, max_tokens=max_tokens, system_prompt=system_prompt)
            elif prov == "openrouter":
                return _call_openrouter(prompt, temperature=temperature, max_tokens=max_tokens, system_prompt=system_prompt)
        except Exception as exc:
            logger.warning("Provider '%s' failed: %s – trying next.", prov, exc)
            last_exc = exc

    raise RuntimeError(f"All LLM providers failed. Last error: {last_exc}")


def generate_structured(
    prompt: str,
    response_schema: type,
    system_prompt: Optional[str] = None,
    temperature: float = 0.1,
) -> Any:
    """
    Generate structured (Pydantic) output using Gemini.

    Structured output with a JSON schema is only supported via Gemini.
    Falls back to plain-text generation + manual JSON parsing via OpenRouter
    if Gemini is unavailable.
    """
    if os.getenv("GEMINI_API_KEY"):
        try:
            return _call_gemini_structured(
                prompt,
                response_schema=response_schema,
                temperature=temperature,
                system_prompt=system_prompt,
            )
        except Exception as exc:
            logger.warning("Gemini structured output failed: %s", exc)

    # Fallback: ask OpenRouter for JSON and parse manually
    import json
    raw = generate_text(
        prompt + "\n\nRespond ONLY with valid JSON matching the requested schema.",
        system_prompt=system_prompt,
        temperature=temperature,
        provider="openrouter",
    )
    # Attempt to parse
    data = json.loads(raw)
    if isinstance(response_schema, type) and issubclass(response_schema, BaseModel):
        return response_schema.model_validate(data)
    return data


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _resolve_providers(forced: Optional[str] = None) -> List[str]:
    """Return ordered list of available providers."""
    if forced:
        return [forced]

    providers = []
    if os.getenv("GEMINI_API_KEY"):
        providers.append("gemini")
    if os.getenv("OPENROUTER_API_KEY"):
        providers.append("openrouter")

    if not providers:
        raise RuntimeError(
            "No LLM API keys found. Set GEMINI_API_KEY and/or OPENROUTER_API_KEY."
        )
    return providers
