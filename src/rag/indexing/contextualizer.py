"""
Contextual retrieval (Anthropic, 2024): an LLM writes a short context that
situates each chunk in its manifesto, and the context is embedded and
BM25-indexed together with the chunk. A windowed child past its section's first
carries no heading of its own, and a voter rarely uses the manifesto's words.

Contexts are cached by content hash in ``paths.processed_data``, so rebuilding
an index never pays for them twice. Like classification, this is fail-fast: a
chunk whose context cannot be written stops the run (the cache keeps the rest).
"""

import hashlib
import json
import logging
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Dict, List, Optional

from src.rag.common.llm_client import call_with_wait_out, generate_text
from src.rag.common.models import Chunk, section_path
from src.utils.config_loader import config

logger = logging.getLogger(__name__)

CONTEXT_PROMPT = """<programa partido="{party}" secção="{section}">
{section_text}
</programa>

Este é um excerto dessa secção:
<excerto>
{chunk}
</excerto>

Escreve um contexto curto (uma ou duas frases, em português de Portugal) que situe \
este excerto no programa eleitoral, para melhorar a sua pesquisa: o partido, o tema \
e o que o excerto propõe ou defende, com as palavras com que um eleitor procuraria \
este tema. Responde apenas com o contexto."""


def context_key(chunk: Chunk) -> str:
    """The key :func:`contextualize` returns a chunk's context under."""
    return hashlib.sha1(chunk.content.encode("utf-8")).hexdigest()


def _write(chunk: Chunk, model: str) -> str:
    prompt = CONTEXT_PROMPT.format(
        party=chunk.party_name,
        section=section_path(chunk.metadata),
        section_text=chunk.parent_content or chunk.content,
        chunk=chunk.content,
    )
    # One model, no fallbacks: every context in an index must come from the same
    # writer. The cheapest provider: a batch job gains nothing from a fast one, and
    # for this model the fastest charged ~4x as much.
    return call_with_wait_out(
        lambda: generate_text(prompt, model=model, temperature=0.0, max_tokens=200, label="chunk context",
                              fallback_models=[], provider_sort="price", reasoning=False),
        label="chunk context", attempts=5,
    ).strip()


def contextualize(chunks: List[Chunk], model: Optional[str] = None, workers: int = 8) -> Dict[str, str]:
    """Context for every chunk, keyed by :func:`context_key`; writes only the uncached ones."""
    model = model or str(config.get("indexing.contextual_model"))
    path = Path(str(config.get("paths.processed_data"))) / f"contexts-{model.split('/')[-1]}.json"
    cache: Dict[str, str] = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    todo = list({context_key(c): c for c in chunks if context_key(c) not in cache}.values())
    logger.info("Contexts: %d cached, %d to write with %s.", len(chunks) - len(todo), len(todo), model)

    def save():
        path.write_text(json.dumps(cache, ensure_ascii=False, indent=0), encoding="utf-8")

    try:
        with ThreadPoolExecutor(workers) as pool:
            for i, (chunk, context) in enumerate(zip(todo, pool.map(lambda c: _write(c, model), todo)), 1):
                cache[context_key(chunk)] = context
                if i % 100 == 0:
                    save()
                    logger.info("  %d / %d contexts written.", i, len(todo))
    finally:
        save()
    return {context_key(c): cache[context_key(c)] for c in chunks}
