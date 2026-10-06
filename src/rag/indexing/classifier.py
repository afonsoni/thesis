"""
Topic classifier for political manifesto chunks.

LLM-only classification through centralized OpenRouter transport.

Handles API limits by using:
- Batch classification (multiple chunks per request).
- Retry/backoff handled by the shared transport layer.
"""

import json
import logging
import os
import time
from typing import Dict, List, Optional

from src.rag.common.models import (
    TOPIC_CATEGORIES,
    VALID_TOPICS,
    Chunk,
    TopicClassification,
)
from src.rag.common.llm_client import generate_structured, generate_structured_batch
from src.utils.config_loader import config
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Classification runtime constants
# ---------------------------------------------------------------------------

DEFAULT_RPM_DELAY = 1.0
DEFAULT_CLASSIFICATION_MODEL = str(
    config.get(
        "indexing.classification_model",
        config.get("llm.openrouter.model", "google/gemma-4-31b-it:free"),
    )
)

# ---------------------------------------------------------------------------
# Classification prompt (Portuguese, multi-label)
# ---------------------------------------------------------------------------

_LABELLING_RULES = """REGRAS DE CLASSIFICAÇÃO:
- Começa pela categoria principal: o tema de que o excerto trata.
- Acrescenta outra categoria só se o excerto contém uma proposta, medida ou
  dado concreto sobre esse tema. Uma menção de passagem não chega.
- Na dúvida, omite a categoria. A maioria dos excertos tem 1 ou 2; usa 3 só
  quando o excerto trata claramente de três temas.
- Não uses "governacao" só porque a medida envolve o Estado, autarquias ou
  licenciamentos; usa-a quando o tema é a própria organização do Estado.
- "financas" são as finanças PÚBLICAS; financiamento de empresas é "economia".
- Exemplos:
   - "residências estudantis" -> ["habitacao", "educacao", "jovens"]
   - "offshores e corrupção" -> ["justica", "politica_externa"]
   - "salário mínimo jovens" -> ["trabalho", "jovens"]
   - "diagnóstico do SNS" -> ["saude"]
- Confiança (1-5): 5=muito claro, 3=razoável, 1=incerto
"""

CLASSIFICATION_PROMPT = f"""És um especialista em análise de programas políticos portugueses.

CATEGORIAS:
{json.dumps(TOPIC_CATEGORIES, indent=2, ensure_ascii=False)}

{_LABELLING_RULES}

RESPOSTA (JSON):
{{
    "categorias": ["categoria1", "categoria2"],
    "confianca": 4,
    "palavras_chave": ["palavra1", "palavra2", "palavra3"]
}}"""

# ---------------------------------------------------------------------------
# LLM classification helpers
# ---------------------------------------------------------------------------


def _normalize_topic_classification(raw: object) -> TopicClassification:
    """Normalize arbitrary JSON/Pydantic output into TopicClassification."""
    if isinstance(raw, TopicClassification):
        data = raw.model_dump()
    elif isinstance(raw, dict):
        data = raw
    else:
        data = {}

    categorias = [c for c in data.get("categorias", []) if c in VALID_TOPICS] or ["outros"]
    confianca = max(1, min(5, int(data.get("confianca", 3))))
    palavras = data.get("palavras_chave", [])
    if not isinstance(palavras, list):
        palavras = []

    return TopicClassification(
        categorias=categorias[:3],
        confianca=confianca,
        palavras_chave=palavras[:10],
    )


def _classify_with_llm(
    content: str,
    context_info: str,
    model: Optional[str] = None,
) -> TopicClassification:
    """Classify one chunk through centralized LLM client."""
    selected_model = model or DEFAULT_CLASSIFICATION_MODEL
    full_content = f"{context_info}TEXTO:\n{content}" if context_info else f"TEXTO:\n{content}"
    prompt = f"{CLASSIFICATION_PROMPT}\n\n{full_content}"

    parsed = generate_structured(
        prompt=prompt,
        response_schema=TopicClassification,
        model=selected_model,
        temperature=0.1,
        max_tokens=500,
    )
    return _normalize_topic_classification(parsed)


# ---------------------------------------------------------------------------
# Batch LLM classification
# ---------------------------------------------------------------------------

BATCH_CLASSIFICATION_PROMPT = f"""És um especialista em análise de programas políticos portugueses.

CATEGORIAS:
{json.dumps(TOPIC_CATEGORIES, indent=2, ensure_ascii=False)}

INSTRUÇÕES:
1. Vais receber VÁRIOS excertos numerados; classifica CADA um.
2. Responde em ARRAY JSON, na mesma ordem dos excertos.

{_LABELLING_RULES}

RESPOSTA (JSON array):
[
    {{
    "id": 0,
    "categorias": ["categoria1", "categoria2"],
    "confianca": 4,
    "palavras_chave": ["palavra1", "palavra2"]
    }},
  ...
]"""


def _classify_batch_with_llm(
    batch: List[Dict[str, str]],
    model: Optional[str] = None,
) -> List[TopicClassification]:
    """Classify a batch through centralized LLM client.

    Primary path uses the shared OpenRouter transport. Retry/fallback orchestration
    remains in `classify_chunks`.
    """
    selected_model = model or DEFAULT_CLASSIFICATION_MODEL
    parts: List[str] = []
    for item in batch:
        ctx = item.get("context", "")
        header = f"Contexto: {ctx}\n" if ctx else ""
        parts.append(f"--- EXCERTO {item['id']} ---\n{header}TEXTO:\n{item['content']}")

    prompt = f"{BATCH_CLASSIFICATION_PROMPT}\n\n" + "\n\n".join(parts)

    raw_items = generate_structured_batch(
        prompt=prompt,
        model=selected_model,
        temperature=0.1,
        max_tokens=2500,
    )

    results: List[TopicClassification] = []
    for entry in raw_items:
        results.append(_normalize_topic_classification(entry))
    return results


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def classify_chunk(
    chunk: Chunk,
    model: Optional[str] = None,
) -> Chunk:
    """Classify a single chunk and attach the result (LLM-only, fail-fast)."""
    if not os.getenv("OPENROUTER_API_KEY"):
        raise ValueError("OPENROUTER_API_KEY is required for classification.")

    context_parts = [
        f"{k}: {v}" for k, v in chunk.metadata.items() if v and str(v).strip()
    ]
    context_info = f"Contexto: {' | '.join(context_parts)}\n\n" if context_parts else ""

    tc = _classify_with_llm(chunk.content, context_info, model)

    chunk.topics = tc.categorias
    chunk.topic_classification = tc
    return chunk


def classify_chunks(
    chunks: List[Chunk],
    model: Optional[str] = None,
    delay: float = DEFAULT_RPM_DELAY,
    batch_size: int = 10,
) -> List[Chunk]:
    """
    Classify chunks with batching and fail-fast behavior.

    Args:
        chunks: Chunks to classify.
        model: OpenRouter model name.
        delay: Delay between API calls.
        batch_size: Number of chunks per batch call.
    """
    if not os.getenv("OPENROUTER_API_KEY"):
        raise ValueError("OPENROUTER_API_KEY is required for classification.")

    total = len(chunks)
    selected_model = model or DEFAULT_CLASSIFICATION_MODEL

    logger.info(
        "Classifying %d chunks (model=%s, batch_size=%d, delay=%.1fs) ...",
        total,
        selected_model,
        batch_size,
        delay,
    )

    classified = 0
    for batch_start in range(0, total, batch_size):
        batch_end = min(batch_start + batch_size, total)
        batch_chunks = chunks[batch_start:batch_end]

        batch_payload: List[Dict[str, str]] = []
        for idx, chunk in enumerate(batch_chunks):
            ctx_parts = [
                f"{k}: {v}" for k, v in chunk.metadata.items() if v and str(v).strip()
            ]
            batch_payload.append(
                {
                    "id": str(idx),
                    "context": " | ".join(ctx_parts),
                    "content": chunk.content,
                }
            )

        try:
            results = _classify_batch_with_llm(batch_payload, model=selected_model)
        except Exception as exc:
            logger.error(
                "LLM batch classification failed for chunks %d-%d: %s",
                batch_start,
                batch_end - 1,
                exc,
            )
            raise

        if len(results) != len(batch_chunks):
            raise RuntimeError(
                "Incomplete batch classification response: "
                f"expected {len(batch_chunks)} results, got {len(results)}"
            )

        for idx, tc in enumerate(results):
            batch_chunks[idx].topics = tc.categorias
            batch_chunks[idx].topic_classification = tc

        classified += len(batch_chunks)
        if classified % 75 <= batch_size or classified == total:
            logger.info("Classified %d / %d chunks", classified, total)

        if batch_end < total and delay > 0:
            time.sleep(delay)

    logger.info("Classification complete - %d chunks processed.", total)
    return chunks
