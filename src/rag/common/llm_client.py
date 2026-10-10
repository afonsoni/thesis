"""
Shared high-level LLM client API.

All indexing/retrieval/generation modules should import from this module.
Prompt construction remains in domain modules; this module only handles transport,
JSON parsing, and optional schema validation.
"""

import json
import logging
import re
import threading
import time
from typing import Any, Callable, Dict, List, Optional, TypeVar

from pydantic import BaseModel

from src.rag.common.llm_transport import (
    call_openrouter_with_retries,
    last_answer_truncated,
    last_answering_model,
    last_usage,
)
from src.utils.config_loader import config

logger = logging.getLogger(__name__)

# Every successful LLM call this process made, in order: {"step", "model",
# "prompt_tokens", "completion_tokens", "cost", "secs"}, the model being the one that
# answered, so a fallback shows up here. Slicing it from a remembered length gives
# one question's calls (``main.py query``, the eval runner), and its token counts
# are what ``scripts/llm_cost.py`` prices. A call cut off at max_tokens has
# " [truncated]" appended to its step.
CALL_LOG: List[Dict[str, Any]] = []

T = TypeVar("T")


def with_deadline(fn: Callable[[], T], secs: float) -> T:
    """Run *fn* in a daemon thread; raise TimeoutError if it has not returned in *secs*.

    A provider can hold a connection open for many minutes without answering,
    which a per-read socket timeout never catches. A hung call's thread is abandoned
    (daemon, so it cannot block interpreter exit).
    """
    box: Dict[str, Any] = {}

    def run():
        try:
            box["value"] = fn()
        except BaseException as exc:  # noqa: BLE001 - re-raised in the caller's thread
            box["error"] = exc

    worker = threading.Thread(target=run, daemon=True)
    worker.start()
    worker.join(secs)
    if worker.is_alive():
        raise TimeoutError(f"no answer within {secs:.0f}s")
    if "error" in box:
        raise box["error"]
    return box["value"]


def call_with_wait_out(
    fn: Callable[[], T],
    label: str,
    attempts: int = 10,
    base_secs: float = 30,
    max_secs: float = 300,
    deadline_secs: float = 600,
) -> T:
    """Call *fn*, waiting out transient failures; re-raise once *attempts* run out.

    For batch jobs on the free tier, where 429/500/503s and timeouts come in bursts
    that outlast the transport's few quick retries. Still fail-fast in the sense
    that matters: the last error is raised, never swallowed into a default.
    """
    for attempt in range(attempts):
        try:
            return with_deadline(fn, deadline_secs)
        except Exception as exc:  # noqa: BLE001 - retried, then re-raised
            if attempt == attempts - 1:
                raise
            wait = min(max_secs, base_secs * (attempt + 1))
            logger.warning("%s failed (%s); waiting %ds (attempt %d/%d)",
                           label, str(exc)[:120], wait, attempt + 1, attempts)
            time.sleep(wait)
    raise AssertionError("unreachable")


def generate_text(
    prompt: str,
    system_prompt: Optional[str] = None,
    temperature: Optional[float] = None,
    max_tokens: Optional[int] = None,
    model: Optional[str] = None,
    timeout_seconds: int = 120,
    response_format: Optional[Dict[str, Any]] = None,
    label: str = "",
) -> str:
    """Generate text through OpenRouter transport with centralized retries.

    ``temperature`` / ``max_tokens`` default to ``llm.openrouter.*`` in config.
    ``label`` names the pipeline step in the log and in ``CALL_LOG``.
    """
    if temperature is None:
        temperature = float(config.get("llm.openrouter.temperature"))
    if max_tokens is None:
        max_tokens = int(config.get("llm.openrouter.max_tokens"))
    selected_model = model or config.get("llm.openrouter.model")
    start = time.perf_counter()
    text = call_openrouter_with_retries(
        prompt=prompt,
        model=selected_model,
        temperature=temperature,
        max_tokens=max_tokens,
        system_prompt=system_prompt,
        timeout_seconds=timeout_seconds,
        response_format=response_format,
    )
    answered_by = last_answering_model() or selected_model
    step = (label or "llm") + (" [truncated]" if last_answer_truncated() else "")
    usage = last_usage()
    CALL_LOG.append({
        "step": step,
        "model": answered_by,
        "prompt_tokens": int(usage.get("prompt_tokens") or 0),
        "completion_tokens": int(usage.get("completion_tokens") or 0),
        "cost": float(usage.get("cost") or 0.0),
        "secs": round(time.perf_counter() - start, 2),  # retries included
    })
    logger.info("[%s] answered by %s", step, answered_by)
    return text


def generate_structured(
    prompt: str,
    response_schema: type,
    system_prompt: Optional[str] = None,
    temperature: float = 0.1,
    model: Optional[str] = None,
    max_tokens: int = 1500,
    timeout_seconds: int = 120,
    label: str = "",
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
        model=model,
        timeout_seconds=timeout_seconds,
        response_format={"type": "json_object"},
        label=label,
    )

    data = _extract_json_payload(raw)
    if isinstance(response_schema, type) and issubclass(response_schema, BaseModel):
        # gemma-4-26b sometimes wraps the requested object in a one-item array.
        if isinstance(data, list) and len(data) == 1 and isinstance(data[0], dict):
            data = data[0]
        return response_schema.model_validate(data)
    return data


def generate_structured_batch(
    prompt: str,
    system_prompt: Optional[str] = None,
    temperature: float = 0.1,
    model: Optional[str] = None,
    max_tokens: int = 2000,
    timeout_seconds: int = 120,
) -> List[Any]:
    """Generate a JSON array (a lone object counts as a one-item array)."""
    raw = generate_text(
        (
            prompt
            + "\n\nResponde APENAS com um array JSON valido na ordem pedida."
        ),
        system_prompt=system_prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        model=model,
        timeout_seconds=timeout_seconds,
        response_format={"type": "json_object"},
    )
    data = _extract_json_payload(raw)
    return data if isinstance(data, list) else [data]


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
