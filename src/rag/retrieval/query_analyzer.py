"""
Query analyzer – structured understanding of user queries.

Uses structured LLM output (Part 10/11 pattern) to extract:
- the parties named or implied by the question
- whether every party in scope must be covered (``coverage``)
- topics from the closed vocabulary
- the shape the answer should take
- a reformulated query for embedding search

The route label itself is *not* extracted: ``AnalyzedQuery.query_type`` derives
it. Asking the model for a four-way route conflated "which programmes must be
read" with "what should the answer look like", and questions like "o que pensa
cada partido sobre educação?" sit in the overlap – they were labelled
topic_exploration and answered from a single flat top-k that covered whichever
parties happened to rank.
"""

import logging
import re
import unicodedata
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from src.rag.common.models import (
    AnalyzedQuery,
    AnswerShape,
    Coverage,
    PARTY_MAP,
    VALID_TOPICS,
)
from src.rag.common.llm_client import generate_structured
from src.rag.retrieval.config import RetrievalConfig
from src.rag.generation.prompts import (
    QUERY_ANALYSIS_PROMPT,
    QUERY_ANALYSIS_SYSTEM_PROMPT,
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Pydantic schema for structured LLM output
# ---------------------------------------------------------------------------

class _QueryAnalysisResponse(BaseModel):
    """Schema used for structured JSON output validation.

    Every field is typed loosely and validated by hand in ``_coerce_*`` below.
    ``generate_structured`` asks OpenRouter for ``json_object``, which is JSON
    *mode*, not schema-constrained decoding – so declaring ``Literal`` members
    here would not stop the model emitting an unlisted topic, it would only turn
    that one bad string into a ``ValidationError`` that discards the whole
    response, including the fields it got right. Field-level coercion degrades
    instead: drop the unrecognised value, keep the rest.
    """
    parties: List[str] = Field(default_factory=list)
    coverage: str = ""
    topics: List[str] = Field(default_factory=list)
    answer_shape: str = ""
    reformulated_query: str = ""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _strip_accents(s: str) -> str:
    """Drop combining marks so "Aliança" and "Alianca" match the same entry."""
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )


# Coalition members and common abbreviations that are not the canonical name or
# the corpus file key. The 2024 corpus holds one programme per coalition, so a
# question about a member party can only be answered from the coalition's
# document: PSD and CDS-PP ran as Aliança Democrática, PCP and PEV as CDU.
_PARTY_ALIAS_EXTRAS: Dict[str, str] = {
    "psd": "Aliança Democrática",
    "partido social democrata": "Aliança Democrática",
    "partido social-democrata": "Aliança Democrática",
    "cds": "Aliança Democrática",
    "cds-pp": "Aliança Democrática",
    "partido popular": "Aliança Democrática",
    "bloco": "Bloco de Esquerda",
    "cdu": "Partido Comunista Português",
    "coligacao democratica unitaria": "Partido Comunista Português",
    "partido comunista": "Partido Comunista Português",
    "pessoas animais natureza": "Pessoas-Animais-Natureza",
}


def _build_party_aliases() -> Dict[str, str]:
    """Accent-stripped alias → canonical party name."""
    aliases: Dict[str, str] = {}
    for key, info in PARTY_MAP.items():
        name = info["name"]
        aliases[_strip_accents(name.lower())] = name
        aliases[key.split("-")[0].lower()] = name  # "ad-2024" → "ad"
    aliases.update(_PARTY_ALIAS_EXTRAS)
    return aliases


_PARTY_ALIASES = _build_party_aliases()

# Alternation over the aliases, longest first so "cds-pp" wins over "cds" and
# the full names win over their initials. Word-anchored: an unanchored scan
# matched "ad" inside "sociedade" and "be" inside "liberdade", labelling neutral
# questions with whichever party happened to be a substring.
_PARTY_PATTERN = re.compile(
    r"\b(" + "|".join(re.escape(a) for a in sorted(_PARTY_ALIASES, key=len, reverse=True)) + r")\b"
)


def _normalize_parties(raw: List[str]) -> List[str]:
    """Map free-form party names from the LLM onto canonical names.

    Exact alias lookups only. The previous substring fallback ("does either
    string contain the other") resolved "PSD" to Partido Socialista, because
    "ps" is inside "psd" — a question about one party answered from another
    party's programme, with citations that look correct. An unrecognised name is
    dropped instead: retrieval then widens rather than narrowing to the wrong
    party.
    """
    canonical: List[str] = []
    known_names = {info["name"] for info in PARTY_MAP.values()}
    for p in raw:
        if p in known_names:
            canonical.append(p)
            continue
        alias = _strip_accents(p.lower().strip())
        if alias in _PARTY_ALIASES:
            canonical.append(_PARTY_ALIASES[alias])
        else:
            logger.debug("Dropping unrecognised party name from analysis: %r", p)
    return list(dict.fromkeys(canonical))  # deduplicate, keep order


def _find_parties(question: str) -> List[str]:
    """Canonical parties named in the question text, in order of appearance."""
    found = [_PARTY_ALIASES[m.group(1)] for m in _PARTY_PATTERN.finditer(_strip_accents(question.lower()))]
    return list(dict.fromkeys(found))


def _coerce_topics(raw: Any) -> List[str]:
    """Keep the topics that exist in the closed vocabulary, drop the rest."""
    if not isinstance(raw, list):
        return []
    kept = [t for t in raw if isinstance(t, str) and t in VALID_TOPICS]
    for t in raw:
        if t not in kept:
            logger.debug("Dropping unrecognised topic from analysis: %r", t)
    return list(dict.fromkeys(kept))


def _coerce_coverage(raw: Any) -> Coverage:
    """Read the coverage decision, defaulting to the safe side.

    An unreadable value falls to EXHAUSTIVE. The two failures are not
    symmetric: fanning out on a question that did not need it costs a handful
    of extra pgvector queries, while pooling a question that did need it drops
    parties from the answer with nothing in the output to show they are
    missing.
    """
    try:
        return Coverage(str(raw).strip().lower())
    except ValueError:
        logger.debug("Unreadable coverage value %r; defaulting to exhaustive.", raw)
        return Coverage.EXHAUSTIVE


def _coerce_answer_shape(raw: Any, parties: List[str], coverage: Coverage) -> AnswerShape:
    """Read the answer shape, inferring one when the model omits it."""
    try:
        return AnswerShape(str(raw).strip().lower())
    except ValueError:
        multi_party = len(parties) >= 2 or (not parties and coverage == Coverage.EXHAUSTIVE)
        return AnswerShape.PER_PARTY if multi_party else AnswerShape.NARRATIVE


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def analyze_query(
    question: str,
    config: Optional[RetrievalConfig] = None,
) -> AnalyzedQuery:
    """
    Analyze a user question and return an ``AnalyzedQuery`` with structured
    metadata for the retrieval router.

    When ``config.use_query_analysis`` is False, the LLM call is skipped entirely
    and the question is treated as a GENERAL query – this is the naive-baseline
    path used by the evaluation harness.
    """
    config = config or RetrievalConfig()
    if not config.use_query_analysis:
        # The naive-baseline arm: no parties, no topics, no coverage guarantee,
        # which derives to a GENERAL route and one flat search.
        return AnalyzedQuery(
            original_query=question,
            coverage=Coverage.BEST_MATCH,
            reformulated_query=question,
        )

    prompt = QUERY_ANALYSIS_PROMPT.format(question=question)

    try:
        parsed: _QueryAnalysisResponse = generate_structured(
            prompt,
            response_schema=_QueryAnalysisResponse,
            system_prompt=QUERY_ANALYSIS_SYSTEM_PROMPT,
            temperature=0.1,
        )
    except Exception as exc:
        logger.warning("Structured query analysis failed: %s – using fallback.", exc)
        return _fallback_analysis(question)

    parties = _normalize_parties(parsed.parties)
    coverage = _coerce_coverage(parsed.coverage)
    return AnalyzedQuery(
        original_query=question,
        parties=parties,
        coverage=coverage,
        topics=_coerce_topics(parsed.topics),
        answer_shape=_coerce_answer_shape(parsed.answer_shape, parties, coverage),
        reformulated_query=parsed.reformulated_query or question,
    )


def _fallback_analysis(question: str) -> AnalyzedQuery:
    """Deterministic stand-in for when the analysis call is unavailable.

    This runs when OpenRouter has exhausted its retries, so it is a degraded
    mode, not a second opinion – and it is deliberately dumber than the version
    it replaced. The old one guessed topics by substring-matching the category
    descriptions and guessed a route from comparison keywords; both encoded
    Portuguese phrasing rules in code, and both were wrong in ways nothing
    downstream could detect.

    What survives is what can be established without interpretation: parties are
    a closed vocabulary, so an exact alias scan either finds one or does not.
    Everything else fails toward coverage – no topic filter to narrow with, and
    EXHAUSTIVE so the router fans out. The cost is a wider search than the
    question may have needed; the alternative is an answer that silently omits
    parties.
    """
    parties = _find_parties(question)
    return AnalyzedQuery(
        original_query=question,
        parties=parties,
        coverage=Coverage.EXHAUSTIVE,
        topics=[],
        answer_shape=_coerce_answer_shape("", parties, Coverage.EXHAUSTIVE),
        reformulated_query=question,
    )
