"""
Shared Pydantic models and data schemas used across the RAG pipeline.
"""

from __future__ import annotations

import uuid
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


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
    summary: Optional[str] = None  # For multi-representation indexing
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
    """Structured representation of a user query after analysis."""
    original_query: str
    query_type: QueryType = QueryType.GENERAL
    parties: List[str] = Field(default_factory=list)
    topics: List[str] = Field(default_factory=list)
    ideology_filter: Optional[str] = None
    reformulated_query: str = ""


class SearchResult(BaseModel):
    """A single search result returned by the vector store."""
    id: str
    content: str
    summary: Optional[str] = None
    party_name: str = "Unknown"
    ideology: str = "unknown"
    year: int = 2024
    topics: List[str] = Field(default_factory=list)
    header_hierarchy: Dict[str, str] = Field(default_factory=dict)
    similarity: float = 0.0


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
    query_type: QueryType = QueryType.GENERAL
    model_used: str = ""
