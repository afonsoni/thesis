"""
Topic classifier for political manifesto chunks.

Merges the best of both existing classification systems:
- **Primary path**: Gemini 2.5 Flash with structured Pydantic output,
  multi-label Portuguese categories (up to 4), and confidence scoring.
- **Fallback path**: keyword-based matching when LLM is unavailable.
"""

import json
import logging
import os
import time
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv

from src.rag.common.models import (
    TOPIC_CATEGORIES,
    VALID_TOPICS,
    Chunk,
    TopicClassification,
)

load_dotenv()
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Classification prompt (Portuguese, multi-label)
# ---------------------------------------------------------------------------

CLASSIFICATION_PROMPT = f"""És um especialista em análise de programas políticos portugueses.

CATEGORIAS:
{json.dumps(TOPIC_CATEGORIES, indent=2, ensure_ascii=False)}

INSTRUÇÕES:
1. Um excerto pode ter MÚLTIPLAS categorias (máximo 4)
2. Exemplos multi-tópico:
   - "residências estudantis" → ["jovens", "educacao", "habitacao"]
   - "offshores e corrupção" → ["justica", "politica_externa"]
   - "salário mínimo jovens" → ["trabalho", "jovens"]
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
        sorted_topics = sorted(topic_scores, key=topic_scores.get, reverse=True)
        top_topics = sorted_topics[:4]  # max 4 categories
        matched_kws = []
        for t in top_topics:
            matched_kws.extend(
                kw for kw in TOPIC_KEYWORDS[t] if kw in content_lower
            )
        return TopicClassification(
            categorias=top_topics,
            confianca=min(max(topic_scores[top_topics[0]], 1), 5),
            palavras_chave=list(dict.fromkeys(matched_kws))[:10],
        )

    return TopicClassification(categorias=["outros"], confianca=1, palavras_chave=[])


# ---------------------------------------------------------------------------
# LLM-based classification (Gemini)
# ---------------------------------------------------------------------------

def _classify_with_gemini(
    content: str,
    context_info: str,
    model: str = "gemini-2.5-flash",
) -> TopicClassification:
    """Call Gemini with structured JSON output."""
    from google import genai  # lazy import

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    full_content = f"{context_info}TEXTO:\n{content}" if context_info else f"TEXTO:\n{content}"
    prompt = f"{CLASSIFICATION_PROMPT}\n\n{full_content}"

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": TopicClassification,
        },
    )

    try:
        obj: TopicClassification = response.parsed
        # Validate categories
        valid = [c for c in obj.categorias if c in VALID_TOPICS]
        return TopicClassification(
            categorias=valid or ["outros"],
            confianca=max(1, min(5, obj.confianca)),
            palavras_chave=obj.palavras_chave,
        )
    except Exception:
        # Fallback: try raw JSON parse
        data = json.loads(response.text)
        cats = [c for c in data.get("categorias", []) if c in VALID_TOPICS] or ["outros"]
        return TopicClassification(
            categorias=cats,
            confianca=max(1, min(5, data.get("confianca", 3))),
            palavras_chave=data.get("palavras_chave", []),
        )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def classify_chunk(
    chunk: Chunk,
    use_llm: bool = True,
    model: str = "gemini-2.5-flash",
) -> Chunk:
    """
    Classify a single chunk and attach the result.

    Falls back to keyword matching if the LLM call fails or *use_llm* is False.
    """
    # Build optional context from header metadata
    context_parts = [
        f"{k}: {v}" for k, v in chunk.metadata.items() if v and str(v).strip()
    ]
    context_info = f"Contexto: {' | '.join(context_parts)}\n\n" if context_parts else ""

    if use_llm and os.getenv("GEMINI_API_KEY"):
        try:
            tc = _classify_with_gemini(chunk.content, context_info, model)
        except Exception as exc:
            logger.warning("LLM classification failed for chunk %s: %s – using fallback", chunk.id, exc)
            tc = classify_topics_fallback(chunk.content)
    else:
        tc = classify_topics_fallback(chunk.content)

    chunk.topics = tc.categorias
    chunk.topic_classification = tc
    return chunk


def classify_chunks(
    chunks: List[Chunk],
    use_llm: bool = True,
    model: str = "gemini-2.5-flash",
    delay: float = 0.2,
) -> List[Chunk]:
    """
    Classify a batch of chunks, with progress logging and rate-limiting.
    """
    total = len(chunks)
    logger.info("Classifying %d chunks (llm=%s, model=%s) …", total, use_llm, model)

    for i, chunk in enumerate(chunks):
        classify_chunk(chunk, use_llm=use_llm, model=model)

        if (i + 1) % 25 == 0:
            logger.info("Classified %d / %d chunks", i + 1, total)

        if use_llm and delay > 0:
            time.sleep(delay)

    logger.info("Classification complete – %d chunks processed.", total)
    return chunks
