"""
Query analyzer – structured understanding of user queries.

Uses structured LLM output (Part 10/11 pattern) to extract:
- the parties named or implied by the question
- whether every party in scope must be covered (``coverage``)
- topics from the closed vocabulary
- the shape the answer should take
- a reformulated query for embedding search

The route label itself is *not* extracted: ``AnalyzedQuery.query_type`` derives
it, so "which programmes must be read" (parties, coverage) and "how to lay out
the answer" (answer_shape) stay separate decisions. "O que pensa cada partido
sobre educação?" needs every party, which a single topic label cannot say.
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
from src.rag.retrieval.prompts import (
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
    unlisted_parties: List[str] = Field(default_factory=list)


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
# document: PSD, CDS-PP and PPM ran as Aliança Democrática, PCP and PEV as CDU.
_PARTY_ALIAS_EXTRAS: Dict[str, str] = {
    "psd": "Aliança Democrática",
    "partido social democrata": "Aliança Democrática",
    "partido social-democrata": "Aliança Democrática",
    "cds": "Aliança Democrática",
    "cds-pp": "Aliança Democrática",
    "partido popular": "Aliança Democrática",
    "ppm": "Aliança Democrática",
    "partido popular monarquico": "Aliança Democrática",
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
# the full names win over their initials. Word-anchored, so "ad" inside
# "sociedade" or "be" inside "liberdade" is not a party.
_PARTY_PATTERN = re.compile(
    r"\b(" + "|".join(re.escape(a) for a in sorted(_PARTY_ALIASES, key=len, reverse=True)) + r")\b"
)


def _normalize_parties(raw: List[str]) -> List[str]:
    """Map free-form party names from the LLM onto canonical names.

    Exact alias lookups only: a substring match would resolve "PSD" to Partido
    Socialista ("ps" is inside "psd") and answer from the wrong programme with
    plausible citations. An unrecognised name is dropped, so retrieval widens
    rather than narrowing to the wrong party.
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


def strip_party_mentions(text: str) -> str:
    """*text* with every party name or alias blanked out; case and accents kept.

    For the lexical query of a party-filtered search: the filter already carries
    the party, and left in, its name is a rare, heavily weighted BM25 term ("ps"
    outweighs "saúde") that ranks a party's self-references above the topic asked
    about. Also the dense query under ``strip_party_names``, which is why the
    case is kept: lowercasing would be a second change in that ablation. Matching
    runs on a lowercased, accent-stripped copy, whose character offsets are the
    same for precomposed text.
    """
    folded = _strip_accents(text.lower())
    out = text if len(folded) == len(text) else folded  # decomposed input: offsets would not line up
    for m in reversed(list(_PARTY_PATTERN.finditer(folded))):
        out = out[: m.start()] + " " + out[m.end():]
    return out


def _coerce_unlisted(raw: Any) -> List[str]:
    """Named parties outside the corpus, minus any that resolve to a corpus party.

    The guard matters because a refusal follows: "PSD" listed here by mistake
    would refuse a question the Aliança Democrática programme answers.
    """
    if not isinstance(raw, list):
        return []
    kept = [p.strip() for p in raw if isinstance(p, str) and p.strip() and not _normalize_parties([p])]
    return list(dict.fromkeys(kept))


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

# Successful analyses, per question, for the life of the process. At temperature 0
# the analyzer still drifts between calls (providers are not bit-exact), and two
# identical eval runs moved recall by up to 0.03; cached, every variant of a run
# routes on the same analysis, so a delta between variants is the feature under
# test. Failures are not cached: a fallback must not outlive the outage.
# ponytail: unbounded dict, fine for an eval or a CLI; an LRU if a long-lived
# server sees many distinct questions.
_ANALYSES: Dict[str, "_QueryAnalysisResponse"] = {}


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

    parsed = _ANALYSES.get(question)
    if parsed is None:
        try:
            parsed = generate_structured(
                QUERY_ANALYSIS_PROMPT.format(question=question),
                response_schema=_QueryAnalysisResponse,
                system_prompt=QUERY_ANALYSIS_SYSTEM_PROMPT,
                temperature=0.0,
                label="query analysis",
            )
        except Exception as exc:
            if config.strict:
                raise
            logger.warning("Structured query analysis failed: %s – using fallback.", exc)
            return _fallback_analysis(question)
        _ANALYSES[question] = parsed

    parties = _normalize_parties(parsed.parties)
    coverage = _coerce_coverage(parsed.coverage)
    return AnalyzedQuery(
        original_query=question,
        parties=parties,
        coverage=coverage,
        topics=_coerce_topics(parsed.topics),
        answer_shape=_coerce_answer_shape(parsed.answer_shape, parties, coverage),
        reformulated_query=parsed.reformulated_query or question,
        unlisted_parties=_coerce_unlisted(parsed.unlisted_parties),
    )


def _fallback_analysis(question: str) -> AnalyzedQuery:
    """Deterministic stand-in once the analysis call has exhausted its retries.

    Only what needs no interpretation is extracted: parties, by an exact alias
    scan over a closed vocabulary. Everything else fails toward coverage – no
    topic filter, and EXHAUSTIVE so the router fans out. A wider search than
    needed beats an answer that silently omits parties.
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
