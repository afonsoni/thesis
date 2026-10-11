"""
Multi-query expansion (Part 5 pattern).

Generates multiple reformulations of the user query to overcome the
limitations of single-query cosine similarity search – especially
important for Portuguese political language where the same concept can
be expressed in many different ways.
"""

import logging
from typing import List

from src.rag.common.llm_client import generate_text
from src.rag.retrieval.prompts import QUERY_EXPANSION_PROMPT, QUERY_EXPANSION_SYNONYMS

logger = logging.getLogger(__name__)

def expand_query(question: str, n_queries: int, strict: bool = False, synonyms: bool = False) -> List[str]:
    """
    Generate *n_queries* reformulated versions of *question*.

    Always returns at least the original question (first element). On an LLM
    failure it returns only the original, unless *strict*, in which case it raises.
    *synonyms* asks for manifesto vocabulary in place of the user's words.
    """
    prompt = QUERY_EXPANSION_PROMPT.format(question=question, n_queries=n_queries)
    if synonyms:
        prompt = prompt.replace("Perguntas reformuladas:", QUERY_EXPANSION_SYNONYMS + "\n\nPerguntas reformuladas:")

    try:
        raw = generate_text(prompt, temperature=0.0, max_tokens=500, label="query expansion")
        expanded = [q.strip() for q in raw.strip().split("\n") if q.strip()]
        # De-duplicate while preserving order
        seen = set()
        unique = []
        for q in expanded:
            if q.lower() not in seen:
                seen.add(q.lower())
                unique.append(q)
        # Ensure the original is always included
        if question.lower() not in seen:
            unique.insert(0, question)
        logger.info("Expanded query into %d variants.", len(unique))
        return unique[:n_queries + 1]  # n expansions + original

    except Exception as exc:
        if strict:
            raise
        logger.warning("Query expansion failed: %s – using original only.", exc)
        return [question]
