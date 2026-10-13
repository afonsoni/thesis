"""
Topic classifier for political manifesto chunks.

Multi-label, LLM-only, in batches of several chunks per request. Fail-fast: a
batch that still fails after ``call_with_wait_out`` aborts the run, so no chunk
is ever stored with made-up default topics.
"""

import json
import logging
import os
import time
from typing import List, Optional

from src.rag.common.models import (
    TOPIC_CATEGORIES,
    VALID_TOPICS,
    Chunk,
    TopicClassification,
)
from src.rag.common.llm_client import call_with_wait_out, generate_structured_batch
from src.utils.config_loader import config

logger = logging.getLogger(__name__)

# Per-batch retries before giving up; waiting first keeps one free-tier outage
# from throwing away a whole party's classification.
WAIT_OUT_ATTEMPTS = int(config.get("indexing.classification_wait_out_attempts"))

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

BATCH_CLASSIFICATION_PROMPT = f"""És um especialista em análise de programas políticos portugueses.

CATEGORIAS:
{json.dumps(TOPIC_CATEGORIES, indent=2, ensure_ascii=False)}

INSTRUÇÕES:
1. Vais receber VÁRIOS excertos numerados; classifica CADA um.
2. Responde em ARRAY JSON, na mesma ordem dos excertos.

{_LABELLING_RULES}

RESPOSTA (JSON):
{{"items": [
    {{
    "id": 0,
    "categorias": ["categoria1", "categoria2"],
    "confianca": 4,
    "palavras_chave": ["palavra1", "palavra2"]
    }},
  ...
]}}"""


def _normalize(raw: object) -> TopicClassification:
    """Keep known topics (at most 3), clamp confidence; tolerate a malformed item."""
    data = raw if isinstance(raw, dict) else {}
    categorias = [c for c in data.get("categorias", []) if c in VALID_TOPICS] or ["outros"]
    palavras = data.get("palavras_chave", [])
    return TopicClassification(
        categorias=categorias[:3],
        confianca=max(1, min(5, int(data.get("confianca", 3)))),
        palavras_chave=palavras[:10] if isinstance(palavras, list) else [],
    )


def _classify_batch_with_llm(chunks: List[Chunk], model: str) -> List[Optional[TopicClassification]]:
    """One request for the whole batch; the header path goes along as context.

    Answers are placed by their "id", not by position, and a chunk without one
    is None: matched by position, one skipped item would hand every later chunk
    its neighbour's topics without any error.
    """
    parts: List[str] = []
    for idx, chunk in enumerate(chunks):
        ctx = " | ".join(f"{k}: {v}" for k, v in chunk.metadata.items() if v and str(v).strip())
        header = f"Contexto: {ctx}\n" if ctx else ""
        parts.append(f"--- EXCERTO {idx} ---\n{header}TEXTO:\n{chunk.content}")

    raw_items = generate_structured_batch(
        prompt=f"{BATCH_CLASSIFICATION_PROMPT}\n\n" + "\n\n".join(parts),
        model=model,
        temperature=0.1,
        max_tokens=2500,
    )
    placed: List[Optional[TopicClassification]] = [None] * len(chunks)
    for pos, entry in enumerate(raw_items):
        try:
            idx = int(entry.get("id", pos)) if isinstance(entry, dict) else pos
        except (TypeError, ValueError):
            continue
        if 0 <= idx < len(chunks) and placed[idx] is None:
            placed[idx] = _normalize(entry)
    return placed


def classify_chunks(
    chunks: List[Chunk],
    model: Optional[str] = None,
    delay: Optional[float] = None,
    batch_size: Optional[int] = None,
) -> List[Chunk]:
    """Classify *chunks* in place, *batch_size* per request, *delay* seconds apart
    (defaults: the ``indexing.classification_*`` config keys)."""
    # Checked up front: a missing key is not transient, and waiting it out would
    # take the full retry budget of every batch.
    if not os.getenv("OPENROUTER_API_KEY"):
        raise ValueError("OPENROUTER_API_KEY is required for classification.")

    total = len(chunks)
    model = model or str(config.get("indexing.classification_model"))
    delay = float(config.get("indexing.classification_delay")) if delay is None else delay
    batch_size = batch_size or int(config.get("indexing.classification_batch_size"))
    logger.info("Classifying %d chunks (model=%s, batch_size=%d, delay=%.1fs) ...",
                total, model, batch_size, delay)

    for batch_start in range(0, total, batch_size):
        batch = chunks[batch_start:batch_start + batch_size]
        label = f"classification of chunks {batch_start}-{batch_start + len(batch) - 1}"

        def classify_batch(batch=batch):
            results = _classify_batch_with_llm(batch, model)
            missing = [i for i, r in enumerate(results) if r is None]
            if missing:
                # Gemma can close the list early (the 15th of a batch, every time
                # at this temperature), so a plain retry repeats it: ask for the gap.
                for i, r in zip(missing, _classify_batch_with_llm([batch[i] for i in missing], model)):
                    results[i] = r
            # Still short: as transient as a 503, so retried with the rest.
            unanswered = sum(r is None for r in results)
            if unanswered:
                raise RuntimeError(
                    "Incomplete batch classification response: "
                    f"{unanswered} of {len(batch)} chunks unanswered"
                )
            return results

        try:
            results = call_with_wait_out(classify_batch, label=label, attempts=WAIT_OUT_ATTEMPTS)
        except Exception as exc:
            logger.error("LLM batch %s failed: %s", label, exc)
            raise

        for chunk, tc in zip(batch, results):
            chunk.topics = tc.categorias
            chunk.topic_classification = tc

        done = batch_start + len(batch)
        if done % 75 <= batch_size or done == total:
            logger.info("Classified %d / %d chunks", done, total)
        if done < total and delay > 0:
            time.sleep(delay)

    logger.info("Classification complete - %d chunks processed.", total)
    return chunks
