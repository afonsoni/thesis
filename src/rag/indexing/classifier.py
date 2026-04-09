"""
Topic classifier for political manifesto chunks.

Merges two complementary strategies:
- Primary path: centralized LLM client through OpenRouter transport.
- Fallback path: local keyword matching when LLM is unavailable/fails.

Handles API limits by using:
- Batch classification (multiple chunks per request).
- Retry with exponential backoff for rate-limit/transient failures.
"""

import json
import logging
import os
import re
import time
from typing import Dict, List, Optional

from dotenv import load_dotenv

from src.rag.common.models import (
    TOPIC_CATEGORIES,
    VALID_TOPICS,
    Chunk,
    TopicClassification,
)
from src.rag.generation.llm_client import generate_structured, generate_structured_batch
from src.utils.config_loader import config

load_dotenv()
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Rate-limit / retry constants
# ---------------------------------------------------------------------------

MAX_RETRIES = 5
BASE_BACKOFF_SECS = 15.0
DEFAULT_RPM_DELAY = 12.0
DEFAULT_CLASSIFICATION_MODEL = str(
    config.get(
        "indexing.classification_model",
        config.get("llm.openrouter.model", "google/gemini-2.5-flash"),
    )
)

# ---------------------------------------------------------------------------
# Classification prompt (Portuguese, multi-label)
# ---------------------------------------------------------------------------

CLASSIFICATION_PROMPT = f"""És um especialista em análise de programas políticos portugueses.

CATEGORIAS:
{json.dumps(TOPIC_CATEGORIES, indent=2, ensure_ascii=False)}

INSTRUÇÕES:
1. Um excerto pode ter MÚLTIPLAS categorias (máximo 4)
2. Exemplos multi-tópico:
   - "residências estudantis" -> ["jovens", "educacao", "habitacao"]
   - "offshores e corrupção" -> ["justica", "politica_externa"]
   - "salário mínimo jovens" -> ["trabalho", "jovens"]
3. Confiança (1-5): 5=muito claro, 3=razoável, 1=incerto

RESPOSTA (JSON):
{{
    "categorias": ["categoria1", "categoria2"],
    "confianca": 4,
    "palavras_chave": ["palavra1", "palavra2", "palavra3"]
}}"""

# ---------------------------------------------------------------------------
# Keyword fallback data
# ---------------------------------------------------------------------------

TOPIC_KEYWORDS: Dict[str, List[str]] = {
    "impostos": ["imposto", "tributação", "fiscal", "taxa", "irs", "iva", "irc"],
    "seguranca_social": ["segurança social", "pensões", "reforma", "subsídio", "prestação social"],
    "trabalho": ["trabalho", "emprego", "laboral", "trabalhador", "sindicat", "salário", "salário mínimo"],
    "economia": ["economia", "crescimento", "competitividade", "pib", "investimento", "desenvolvimento económico"],
    "financas": ["finanças", "orçamento", "dívida pública", "défice", "gestão financeira"],
    "habitacao": ["habitação", "casa", "arrendamento", "imobiliário", "habitacional", "renda"],
    "saude": ["saúde", "hospital", "médico", "sns", "cuidados de saúde", "medicina", "saúde mental"],
    "educacao": ["educação", "escola", "ensino", "professor", "estudante", "universidade", "ciência"],
    "seguranca": ["segurança pública", "crime", "polícia", "proteção civil", "bombeiros", "criminalidade"],
    "justica": ["justiça", "tribunal", "juiz", "direito", "lei", "jurídico", "corrupção"],
    "politica_externa": ["política externa", "diplomacia", "internacional", "europa", "nato", "ue"],
    "cultura": ["cultura", "arte", "património", "museu", "teatro", "cinema", "desporto"],
    "ambiente": ["ambiente", "clima", "ecologia", "sustentabilidade", "verde", "carbono", "energia"],
    "igualdade": ["igualdade", "género", "direitos humanos", "inclusão", "discriminação", "minorias"],
    "jovens": ["juventude", "jovens", "emancipação", "residências estudantis"],
    "imigracao": ["imigração", "integração", "diversidade", "refugiados", "estrangeiros"],
    "governacao": ["governação", "administração pública", "descentralização", "poder local", "transparência"],
}


# ---------------------------------------------------------------------------
# Keyword fallback
# ---------------------------------------------------------------------------

def classify_topics_fallback(content: str) -> TopicClassification:
    """Keyword-based multi-label classification (offline fallback)."""
    content_lower = content.lower()
    topic_scores: Dict[str, int] = {}

    for topic, keywords in TOPIC_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in content_lower)
        if score > 0:
            topic_scores[topic] = score

    if topic_scores:
        sorted_topics = sorted(topic_scores, key=lambda key: topic_scores[key], reverse=True)
        top_topics = sorted_topics[:4]
        matched_kws: List[str] = []
        for topic in top_topics:
            matched_kws.extend(kw for kw in TOPIC_KEYWORDS[topic] if kw in content_lower)
        return TopicClassification(
            categorias=top_topics,
            confianca=min(max(topic_scores[top_topics[0]], 1), 5),
            palavras_chave=list(dict.fromkeys(matched_kws))[:10],
        )

    return TopicClassification(categorias=["outros"], confianca=1, palavras_chave=[])


# ---------------------------------------------------------------------------
# LLM classification helpers
# ---------------------------------------------------------------------------

def _parse_retry_delay(exc: Exception) -> Optional[float]:
    """Try to extract retry delay (seconds) from error messages."""
    msg = str(exc)
    patterns = [
        r"retry(?:[_ ]?[Dd]elay|In)[^\d]*(\d+(?:\.\d+)?)",
        r"retry[-_ ]?after[^\d]*(\d+(?:\.\d+)?)",
    ]
    for pattern in patterns:
        match = re.search(pattern, msg, flags=re.IGNORECASE)
        if match:
            return float(match.group(1))
    return None


def _is_rate_limit_error(exc: Exception) -> bool:
    """Check whether the exception likely represents a rate-limit error."""
    msg = str(exc).lower()
    return "429" in msg or "resource_exhausted" in msg or "rate limit" in msg


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
        categorias=categorias[:4],
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
1. Vais receber VÁRIOS excertos numerados.
2. Para CADA excerto, classifica com MÚLTIPLAS categorias (máximo 4).
3. Exemplos multi-tópico:
   - "residências estudantis" -> ["jovens", "educacao", "habitacao"]
   - "offshores e corrupção" -> ["justica", "politica_externa"]
   - "salário mínimo jovens" -> ["trabalho", "jovens"]
4. Confiança (1-5): 5=muito claro, 3=razoável, 1=incerto
5. Responde em ARRAY JSON, na mesma ordem dos excertos.

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
    use_llm: bool = True,
    model: Optional[str] = None,
) -> Chunk:
    """Classify a single chunk and attach the result."""
    context_parts = [
        f"{k}: {v}" for k, v in chunk.metadata.items() if v and str(v).strip()
    ]
    context_info = f"Contexto: {' | '.join(context_parts)}\n\n" if context_parts else ""

    if use_llm and os.getenv("OPENROUTER_API_KEY"):
        try:
            tc = _classify_with_llm(chunk.content, context_info, model)
        except Exception as exc:
            logger.warning("LLM classification failed for chunk %s: %s - using fallback", chunk.id, exc)
            tc = classify_topics_fallback(chunk.content)
    else:
        tc = classify_topics_fallback(chunk.content)

    chunk.topics = tc.categorias
    chunk.topic_classification = tc
    return chunk


def classify_chunks(
    chunks: List[Chunk],
    use_llm: bool = True,
    model: Optional[str] = None,
    delay: float = DEFAULT_RPM_DELAY,
    batch_size: int = 10,
) -> List[Chunk]:
    """
    Classify chunks with batching, retries, and fallback-safe behavior.

    Args:
        chunks: Chunks to classify.
        use_llm: Use LLM classification (True) or keyword fallback (False).
        model: OpenRouter model name.
        delay: Delay between API calls.
        batch_size: Number of chunks per batch call.
    """
    total = len(chunks)
    selected_model = model or DEFAULT_CLASSIFICATION_MODEL

    logger.info(
        "Classifying %d chunks (llm=%s, model=%s, batch_size=%d, delay=%.1fs) ...",
        total,
        use_llm,
        selected_model,
        batch_size if use_llm else 1,
        delay,
    )

    if not use_llm or not os.getenv("OPENROUTER_API_KEY"):
        for idx, chunk in enumerate(chunks):
            tc = classify_topics_fallback(chunk.content)
            chunk.topics = tc.categorias
            chunk.topic_classification = tc
            if (idx + 1) % 100 == 0:
                logger.info("Classified %d / %d chunks (keyword)", idx + 1, total)
        logger.info("Classification complete - %d chunks processed (keyword fallback).", total)
        return chunks

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

        success = False
        for attempt in range(MAX_RETRIES):
            try:
                results = _classify_batch_with_llm(batch_payload, model=selected_model)
                for idx, tc in enumerate(results):
                    if idx < len(batch_chunks):
                        batch_chunks[idx].topics = tc.categorias
                        batch_chunks[idx].topic_classification = tc
                for idx in range(len(results), len(batch_chunks)):
                    tc = classify_topics_fallback(batch_chunks[idx].content)
                    batch_chunks[idx].topics = tc.categorias
                    batch_chunks[idx].topic_classification = tc
                success = True
                break
            except Exception as exc:
                if _is_rate_limit_error(exc):
                    wait = _parse_retry_delay(exc) or (BASE_BACKOFF_SECS * (2 ** attempt))
                    wait = min(wait + 2, 120)
                    logger.warning(
                        "Rate limited (attempt %d/%d) - waiting %.0fs before retry ...",
                        attempt + 1,
                        MAX_RETRIES,
                        wait,
                    )
                    time.sleep(wait)
                else:
                    logger.warning(
                        "LLM batch classification failed: %s - using keyword fallback for batch",
                        exc,
                    )
                    break

        if not success:
            for chunk in batch_chunks:
                tc = classify_topics_fallback(chunk.content)
                chunk.topics = tc.categorias
                chunk.topic_classification = tc

        classified += len(batch_chunks)
        if classified % 50 <= batch_size or classified == total:
            logger.info("Classified %d / %d chunks", classified, total)

        if batch_end < total and delay > 0:
            time.sleep(delay)

    logger.info("Classification complete - %d chunks processed.", total)
    return chunks
