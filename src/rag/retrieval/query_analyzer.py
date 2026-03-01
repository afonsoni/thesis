"""
Query analyzer – structured understanding of user queries.

Uses LLM (Gemini structured output, Part 10/11 pattern) to extract:
- query type (single_party / comparison / topic_exploration / general)
- mentioned parties & topics
- ideology filter
- reformulated query for embedding search
"""

import logging
import unicodedata
from typing import List, Optional

from pydantic import BaseModel, Field

from src.rag.common.models import (
    AnalyzedQuery,
    PARTY_MAP,
    QueryType,
    TOPIC_CATEGORIES,
    VALID_TOPICS,
)
from src.rag.generation.llm_client import generate_structured, generate_text
from src.rag.generation.prompts import (
    QUERY_ANALYSIS_PROMPT,
    QUERY_ANALYSIS_SYSTEM_PROMPT,
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Pydantic schema for structured LLM output
# ---------------------------------------------------------------------------

class _QueryAnalysisResponse(BaseModel):
    """Schema sent to Gemini for structured JSON output."""
    query_type: str = Field(description="One of: single_party, comparison, topic_exploration, general")
    parties: List[str] = Field(default_factory=list)
    topics: List[str] = Field(default_factory=list)
    ideology_filter: Optional[str] = None
    reformulated_query: str = ""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_PARTY_NAME_LOOKUP = {info["name"].lower(): info["name"] for info in PARTY_MAP.values()}
_PARTY_KEY_LOOKUP = {k.split("-")[0].lower(): info["name"] for k, info in PARTY_MAP.items()}

# Merge both lookups
_ALL_PARTY_LOOKUP = {**_PARTY_NAME_LOOKUP, **_PARTY_KEY_LOOKUP}


def _normalize_parties(raw: List[str]) -> List[str]:
    """Map free-form party names to canonical names."""
    canonical: List[str] = []
    known_names = {info["name"] for info in PARTY_MAP.values()}
    for p in raw:
        if p in known_names:
            canonical.append(p)
            continue
        low = p.lower().strip()
        if low in _ALL_PARTY_LOOKUP:
            canonical.append(_ALL_PARTY_LOOKUP[low])
            continue
        # Fuzzy: check if any known name contains the token
        for key, name in _ALL_PARTY_LOOKUP.items():
            if low in key or key in low:
                canonical.append(name)
                break
    return list(dict.fromkeys(canonical))  # deduplicate, keep order


def _normalize_topics(raw: List[str]) -> List[str]:
    return [t for t in raw if t in VALID_TOPICS]


def _normalize_query_type(raw: str) -> QueryType:
    try:
        return QueryType(raw)
    except ValueError:
        return QueryType.GENERAL


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def analyze_query(question: str) -> AnalyzedQuery:
    """
    Analyze a user question and return an ``AnalyzedQuery`` with structured
    metadata for the retrieval router.
    """
    prompt = QUERY_ANALYSIS_PROMPT.format(question=question)

    try:
        parsed: _QueryAnalysisResponse = generate_structured(
            prompt,
            response_schema=_QueryAnalysisResponse,
            system_prompt=QUERY_ANALYSIS_SYSTEM_PROMPT,
            temperature=0.1,
        )

        return AnalyzedQuery(
            original_query=question,
            query_type=_normalize_query_type(parsed.query_type),
            parties=_normalize_parties(parsed.parties),
            topics=_normalize_topics(parsed.topics),
            ideology_filter=parsed.ideology_filter if parsed.ideology_filter in ("left", "right") else None,
            reformulated_query=parsed.reformulated_query or question,
        )

    except Exception as exc:
        logger.warning("Structured query analysis failed: %s – using fallback.", exc)
        return _fallback_analysis(question)


def _fallback_analysis(question: str) -> AnalyzedQuery:
    """Simple heuristic fallback when LLM analysis fails."""
    q_lower = question.lower()

    # Detect parties
    parties = []
    for key, name in _ALL_PARTY_LOOKUP.items():
        if key in q_lower:
            parties.append(name)
    parties = list(dict.fromkeys(parties))

    # Detect topics (normalize accents for matching)
    def _strip_accents(s: str) -> str:
        return "".join(
            c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
        )

    q_norm = _strip_accents(q_lower)
    topics = []
    for topic_key, topic_desc in TOPIC_CATEGORIES.items():
        # Match against key (e.g. "educacao") and description keywords
        key_norm = _strip_accents(topic_key.replace("_", " "))
        if key_norm in q_norm:
            topics.append(topic_key)
            continue
        # Also try matching individual description keywords
        for kw in topic_desc.split(","):
            kw_norm = _strip_accents(kw.strip().lower())
            if len(kw_norm) > 3 and kw_norm in q_norm:
                topics.append(topic_key)
                break
    topics = list(dict.fromkeys(topics))  # deduplicate preserving order

    # Detect ideology
    ideology = None
    if "esquerda" in q_lower or "left" in q_lower:
        ideology = "left"
    elif "direita" in q_lower or "right" in q_lower:
        ideology = "right"

    # Guess query type
    comparison_words = ["comparar", "compara", "diferença", "diferenças", "versus", "vs", "entre"]
    if any(w in q_lower for w in comparison_words) or len(parties) >= 2:
        qt = QueryType.COMPARISON
    elif len(parties) == 1:
        qt = QueryType.SINGLE_PARTY
    elif topics:
        qt = QueryType.TOPIC_EXPLORATION
    else:
        qt = QueryType.GENERAL

    return AnalyzedQuery(
        original_query=question,
        query_type=qt,
        parties=parties,
        topics=topics,
        ideology_filter=ideology,
        reformulated_query=question,
    )
