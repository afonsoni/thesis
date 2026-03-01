"""
Tests for the indexing pipeline: chunker, classifier fallback, store schema, embedder.
"""

import json
import os
import sys
import pytest

# Ensure project root is on the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ---------------------------------------------------------------------------
# Chunker
# ---------------------------------------------------------------------------

class TestChunker:
    """Tests for src.rag.indexing.chunker."""

    SAMPLE_MD = """# Programa do Partido X

## Economia

### Fiscalidade

Propomos reduzir o IRS para os escalões mais baixos e simplificar o sistema tributário.
As empresas beneficiarão de uma redução do IRC para promover o investimento.

### Emprego

Criação de programas de formação profissional para jovens desempregados.
Reforço do salário mínimo nacional para 1000 euros.

## Saúde

Reforço do SNS e contratação de mais profissionais de saúde.
Construção de novos centros de saúde nas áreas metropolitanas.
"""

    def test_chunk_count(self):
        from src.rag.indexing.chunker import chunk_markdown

        chunks = chunk_markdown(self.SAMPLE_MD, "ps-2024.md")
        assert len(chunks) > 0, "Should produce at least one chunk"

    def test_party_metadata(self):
        from src.rag.indexing.chunker import chunk_markdown

        chunks = chunk_markdown(self.SAMPLE_MD, "ps-2024.md")
        for c in chunks:
            assert c.party_name == "Partido Socialista"
            assert c.ideology == "left"
            assert c.year == 2024

    def test_small_chunks_filtered(self):
        from src.rag.indexing.chunker import chunk_markdown

        tiny_md = "# Title\n\nOk\n\n## Section\n\nToo small"
        chunks = chunk_markdown(tiny_md, "test.md")
        # Both sections are < 50 chars, should be filtered
        for c in chunks:
            assert c.size > 50

    def test_windowed_splitting(self):
        from src.rag.indexing.chunker import chunk_markdown

        # Create a large section that must be split
        long_text = "Esta é uma proposta importante. " * 200
        big_md = f"# Programa\n\n## Secção grande\n\n{long_text}"
        chunks = chunk_markdown(big_md, "ad-2024.md", max_chunk_size=500)
        assert len(chunks) > 1, "Large section should produce multiple windowed chunks"
        assert any(c.chunk_type == "windowed" for c in chunks)


# ---------------------------------------------------------------------------
# Classifier fallback (no LLM needed)
# ---------------------------------------------------------------------------

class TestClassifierFallback:
    """Tests for keyword-based classification (offline path)."""

    def test_tax_classification(self):
        from src.rag.indexing.classifier import classify_topics_fallback

        tc = classify_topics_fallback(
            "Propomos baixar o IRS e simplificar a tributação fiscal."
        )
        assert "impostos" in tc.categorias

    def test_health_classification(self):
        from src.rag.indexing.classifier import classify_topics_fallback

        tc = classify_topics_fallback(
            "Reforço do SNS com mais médicos e hospitais."
        )
        assert "saude" in tc.categorias

    def test_unknown_returns_outros(self):
        from src.rag.indexing.classifier import classify_topics_fallback

        tc = classify_topics_fallback("Lorem ipsum dolor sit amet.")
        assert tc.categorias == ["outros"]

    def test_multi_label(self):
        from src.rag.indexing.classifier import classify_topics_fallback

        tc = classify_topics_fallback(
            "Residências estudantis para jovens na universidade com arrendamento acessível."
        )
        # Should match at least jovens or educacao or habitacao
        assert len(tc.categorias) >= 1
        assert any(t in tc.categorias for t in ["jovens", "educacao", "habitacao"])


# ---------------------------------------------------------------------------
# Common models
# ---------------------------------------------------------------------------

class TestModels:
    """Tests for Pydantic schemas in common/models.py."""

    def test_get_party_info(self):
        from src.rag.common.models import get_party_info

        info = get_party_info("livre-2024-manual.md")
        assert info["name"] == "LIVRE"
        assert info["ideology"] == "left"

    def test_unknown_party(self):
        from src.rag.common.models import get_party_info

        info = get_party_info("random-file.md")
        assert info["name"] == "Unknown"

    def test_chunk_model_defaults(self):
        from src.rag.common.models import Chunk

        c = Chunk(content="teste")
        assert c.topics == ["outros"]
        assert c.party_name == "Unknown"
        assert c.id  # UUID should be auto-generated

    def test_analyzed_query_model(self):
        from src.rag.common.models import AnalyzedQuery, QueryType

        q = AnalyzedQuery(
            original_query="test",
            query_type=QueryType.COMPARISON,
            parties=["PS", "CHEGA"],
        )
        assert q.query_type == QueryType.COMPARISON
        assert len(q.parties) == 2


# ---------------------------------------------------------------------------
# RRF (pure function, no DB needed)
# ---------------------------------------------------------------------------

class TestRRF:
    """Test Reciprocal Rank Fusion logic."""

    def test_basic_fusion(self):
        from src.rag.retrieval.searcher import reciprocal_rank_fusion
        from src.rag.common.models import SearchResult

        r1 = SearchResult(id="a", content="doc A", similarity=0.9)
        r2 = SearchResult(id="b", content="doc B", similarity=0.8)
        r3 = SearchResult(id="a", content="doc A", similarity=0.7)  # duplicate
        r4 = SearchResult(id="c", content="doc C", similarity=0.6)

        fused = reciprocal_rank_fusion([[r1, r2], [r3, r4]], k=60)
        # "a" appears in both lists → should rank higher
        assert fused[0].id == "a"
        assert len(fused) == 3  # a, b, c

    def test_empty_lists(self):
        from src.rag.retrieval.searcher import reciprocal_rank_fusion

        assert reciprocal_rank_fusion([]) == []
        assert reciprocal_rank_fusion([[]]) == []


# ---------------------------------------------------------------------------
# Query analyzer fallback (no LLM needed)
# ---------------------------------------------------------------------------

class TestQueryAnalyzerFallback:
    """Test heuristic fallback query analysis."""

    def test_comparison_detection(self):
        from src.rag.retrieval.query_analyzer import _fallback_analysis
        from src.rag.common.models import QueryType

        q = _fallback_analysis("Comparar as políticas do PS e do CHEGA sobre saúde")
        assert q.query_type == QueryType.COMPARISON

    def test_single_party_detection(self):
        from src.rag.retrieval.query_analyzer import _fallback_analysis
        from src.rag.common.models import QueryType

        q = _fallback_analysis("O que propõe o LIVRE sobre habitação?")
        assert q.query_type == QueryType.SINGLE_PARTY
        assert any("LIVRE" in p for p in q.parties)

    def test_topic_detection(self):
        from src.rag.retrieval.query_analyzer import _fallback_analysis

        q = _fallback_analysis("Quais são as propostas sobre educação?")
        assert "educacao" in q.topics

    def test_general_fallback(self):
        from src.rag.retrieval.query_analyzer import _fallback_analysis
        from src.rag.common.models import QueryType

        q = _fallback_analysis("Previsões para o próximo ano")
        assert q.query_type == QueryType.GENERAL
