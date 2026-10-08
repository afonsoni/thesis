"""
Shared Pydantic models and data schemas used across the RAG pipeline.
"""

from __future__ import annotations

import uuid
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field, computed_field


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class QueryType(str, Enum):
    """Types of user queries the retrieval router can dispatch."""
    SINGLE_PARTY = "single_party"
    COMPARISON = "comparison"
    TOPIC_EXPLORATION = "topic_exploration"
    GENERAL = "general"


class Ideology(str, Enum):
    LEFT = "left"
    RIGHT = "right"
    UNKNOWN = "unknown"


class Coverage(str, Enum):
    """Whether the answer must represent every party in scope.

    The candidate set comes from ``AnalyzedQuery.parties`` (all parties when it
    is empty); this says how to search it. ``EXHAUSTIVE`` fans out, one search
    per party, so no party can be crowded out of a global top-k by a more
    verbose one. ``BEST_MATCH`` runs a single pooled search and accepts whatever
    ranks highest.
    """
    EXHAUSTIVE = "exhaustive"
    BEST_MATCH = "best_match"


class AnswerShape(str, Enum):
    """How the answer should be laid out. A generation concern, not a retrieval one.

    Separate from ``Coverage`` because the two genuinely cross: "que partido
    propõe mais sobre habitação?" needs every party retrieved (EXHAUSTIVE) but
    answered as a single verdict (NARRATIVE), not as eight sections.
    """
    NARRATIVE = "narrative"
    PER_PARTY = "per_party"


class ScoreType(str, Enum):
    """Scale that a ``SearchResult.similarity`` value is expressed on."""
    COSINE = "cosine"
    RRF = "rrf"
    LEXICAL = "lexical"  # BM25 over Portuguese tsvector lexemes (indexing/bm25.py)
    RERANK = "rerank"  # Cross-encoder relevance logit – unbounded, not a similarity


class ChunkStrategy(str, Enum):
    """Chunk windowing strategies, usable as evaluation ablation arms.

    ``CHAR`` is the historical behavior and is retained as the baseline: it
    measures chunk size in characters, which silently overruns the embedding
    model's token window. ``TOKEN`` and ``SMALL_TO_BIG`` measure in tokens so
    every chunk fits; ``SMALL_TO_BIG`` additionally hands the parent section to
    generation instead of the embedded child.
    """
    CHAR = "char"
    TOKEN = "token"
    SMALL_TO_BIG = "small_to_big"


# Markdown header metadata keys, coarsest to finest. Kept here (rather than in
# the chunker) so retrieval and generation can read header paths back out of
# stored metadata without importing the indexing layer.
HEADER_METADATA_KEYS = (
    "Title",
    "Major_Section",
    "Policy_Area",
    "Policy_Topic",
    "Subsection",
    "Details",
)


def section_path(headers: Dict[str, Any]) -> str:
    """Breadcrumb of markdown headers, coarsest first, ignoring bookkeeping keys."""
    return " > ".join(str(headers[key]) for key in HEADER_METADATA_KEYS if headers.get(key))


# ---------------------------------------------------------------------------
# Topic categories (canonical list used across the whole pipeline)
# ---------------------------------------------------------------------------

TOPIC_CATEGORIES: Dict[str, str] = {
    "impostos": "Impostos, taxas, fiscalidade, tributação, política fiscal",
    "seguranca_social": "Segurança social, pensões, reformas, subsídios, proteção social",
    "trabalho": "Trabalho, emprego, salários, direitos laborais, sindicatos, desemprego",
    "economia": "Economia, crescimento económico, competitividade, desenvolvimento económico",
    "financas": "Finanças públicas, orçamento, dívida pública, gestão financeira",
    "habitacao": "Habitação, arrendamento, propriedade, habitação social, urbanismo, residências estudantis",
    "saude": "Saúde, SNS, hospitais, cuidados médicos, saúde mental, medicamentos",
    "educacao": "Educação, ensino, universidades, escolas, formação profissional, ciência",
    "seguranca": "Segurança pública, forças policiais, criminalidade, ordem pública",
    "justica": "Justiça, tribunais, sistema judicial, direitos fundamentais, corrupção, offshores",
    "politica_externa": "Política externa, relações internacionais, UE, diplomacia, offshores",
    "cultura": "Cultura, património, artes, língua portuguesa, criatividade, desporto",
    "ambiente": "Ambiente, clima, sustentabilidade, energia, proteção ambiental",
    "igualdade": "Igualdade de género, direitos humanos, inclusão, discriminação, minorias",
    "jovens": "Juventude, políticas para jovens, emancipação jovem, residências estudantis",
    "imigracao": "Imigração, integração, diversidade, comunidades estrangeiras, refugiados",
    "governacao": "Governação, administração pública, descentralização, poder local, transparência",
    "outros": "Outros temas não classificados nas categorias anteriores",
}

VALID_TOPICS: List[str] = list(TOPIC_CATEGORIES.keys())


# ---------------------------------------------------------------------------
# Party metadata
# ---------------------------------------------------------------------------

PARTY_MAP: Dict[str, Dict[str, str]] = {
    "ad-2024":    {"name": "Aliança Democrática",         "ideology": "right"},
    "be-2024":    {"name": "Bloco de Esquerda",           "ideology": "left"},
    "chega-2024": {"name": "CHEGA",                       "ideology": "right"},
    "il-2024":    {"name": "Iniciativa Liberal",           "ideology": "right"},
    "livre-2024": {"name": "LIVRE",                       "ideology": "left"},
    "pan-2024":   {"name": "Pessoas-Animais-Natureza",    "ideology": "left"},
    "pcp-2024":   {"name": "Partido Comunista Português", "ideology": "left"},
    "ps-2024":    {"name": "Partido Socialista",          "ideology": "left"},
}


def get_party_info(file_name: str) -> Dict[str, str]:
    """Extract party information from a filename."""
    lower = file_name.lower()
    for key, info in PARTY_MAP.items():
        if key in lower:
            return info
    return {"name": "Unknown", "ideology": "unknown"}


# ---------------------------------------------------------------------------
# Chunk models
# ---------------------------------------------------------------------------

class TopicClassification(BaseModel):
    """Result of LLM-based topic classification for a chunk."""
    categorias: List[str] = Field(default_factory=lambda: ["outros"])
    confianca: int = Field(default=3, ge=1, le=5)
    palavras_chave: List[str] = Field(default_factory=list)


class Chunk(BaseModel):
    """A single document chunk ready for embedding / storage."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    content: str
    # Small-to-big retrieval: ``content`` is the small child that gets embedded,
    # while ``parent_content`` holds the full header section it was windowed out
    # of. Retrieval matches on the child; generation reads the parent. None when
    # the chunk was never windowed, or under the char-based baseline strategy.
    parent_content: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    party_name: str = "Unknown"
    ideology: str = "unknown"
    year: int = 2024
    topics: List[str] = Field(default_factory=lambda: ["outros"])
    topic_classification: Optional[TopicClassification] = None
    size: int = 0
    word_count: int = 0
    chunk_type: str = "header_only"


class EmbeddedChunk(Chunk):
    """A chunk with its embedding vector attached."""
    embedding: List[float] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# Query / retrieval models
# ---------------------------------------------------------------------------

class AnalyzedQuery(BaseModel):
    """Structured representation of a user query after analysis.

    The fields describe what the user asked for; they do not encode a retrieval
    plan. Keeping them semantic is what lets the router be evaluated separately
    from the analyzer, and what keeps gold annotations valid across every
    variant in the ladder.

    There is deliberately no ideology field. A single left/right axis is too
    coarse for questions like "os partidos conservadores" and too contested to
    author here, so the analyzer resolves bloc language straight into
    ``parties`` instead. That makes the resolution visible and scoreable rather
    than hidden behind a metadata filter.
    """
    # Rejects unknown keys so that passing the derived ``query_type`` in is a
    # loud error rather than a silently ignored one.
    model_config = ConfigDict(extra="forbid")

    original_query: str
    parties: List[str] = Field(default_factory=list)
    coverage: Coverage = Coverage.BEST_MATCH
    topics: List[str] = Field(default_factory=list)
    answer_shape: AnswerShape = AnswerShape.NARRATIVE
    reformulated_query: str = ""

    @computed_field  # type: ignore[prop-decorator]
    @property
    def query_type(self) -> QueryType:
        """The legacy route label, derived rather than stored.

        Generation and ``RoutingMetric`` still speak in query types, but storing
        one alongside ``parties``/``coverage`` would give the same fact two
        sources of truth — which is the defect this schema replaced. Deriving it
        keeps the old vocabulary without letting it drift.

        Two or more named parties imply the fan-out whatever ``coverage`` says:
        naming them is itself the request that each be covered.
        """
        if len(self.parties) >= 2:
            return QueryType.COMPARISON
        if len(self.parties) == 1:
            return QueryType.SINGLE_PARTY
        if self.coverage == Coverage.EXHAUSTIVE:
            return QueryType.COMPARISON
        if self.topics:
            return QueryType.TOPIC_EXPLORATION
        return QueryType.GENERAL


class SearchResult(BaseModel):
    """A single search result returned by the vector store."""
    id: str
    content: str
    parent_content: Optional[str] = None
    party_name: str = "Unknown"
    ideology: str = "unknown"
    year: int = 2024
    topics: List[str] = Field(default_factory=list)
    # Mirrors the stored ``header_hierarchy`` JSONB, which is the chunker's raw
    # metadata: header keys plus non-string windowing bookkeeping
    # (sub_chunk_index, total_sub_chunks, parent_chunk_size).
    header_hierarchy: Dict[str, Any] = Field(default_factory=dict)
    similarity: float = 0.0
    # What ``similarity`` actually holds: raw cosine from the vector store, or a
    # fused Reciprocal Rank Fusion score once multiple ranked lists are merged.
    # RRF scores are ~1/k-scaled and are NOT comparable to cosine values.
    score_type: ScoreType = ScoreType.COSINE

    @property
    def context_text(self) -> str:
        """Text to hand to the generator: the parent section when one was stored
        (small-to-big), otherwise the embedded chunk itself."""
        return self.parent_content or self.content

    @property
    def section_path(self) -> str:
        """Breadcrumb of markdown headers, coarsest first, ignoring bookkeeping keys."""
        return section_path(self.header_hierarchy)


class RetrievalResult(BaseModel):
    """Aggregated retrieval results ready for generation."""
    query: AnalyzedQuery
    results: List[SearchResult] = Field(default_factory=list)
    results_by_party: Dict[str, List[SearchResult]] = Field(default_factory=dict)


# ---------------------------------------------------------------------------
# Generation models
# ---------------------------------------------------------------------------

class GeneratedAnswer(BaseModel):
    """Final answer produced by the generation pipeline."""
    answer: str
    sources: List[Dict[str, Any]] = Field(default_factory=list)
    # The context block exactly as it went into the prompt (parent sections,
    # after deduplication and budget trimming), so evaluation can check the
    # answer against what the generator actually read.
    context: str = ""
    query_type: QueryType = QueryType.GENERAL
    model_used: str = ""
