"""
Tests for the indexing pipeline: chunker, classifier batching, checkpoints, store schema, embedder.
"""

import os
import sys
from unittest.mock import patch

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


class TestClassifierBatching:
    """Tests for batch orchestration and fail-fast behavior."""

    def test_classify_chunks_batches_requests(self, monkeypatch):
        from src.rag.common.models import Chunk, TopicClassification
        from src.rag.indexing.classifier import classify_chunks

        monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")

        chunks = [Chunk(content=f"Texto economia {i}") for i in range(5)]
        calls = {"count": 0}

        def fake_batch(batch, model):
            calls["count"] += 1
            return [
                TopicClassification(categorias=["economia"], confianca=4, palavras_chave=["economia"])
                for _ in batch
            ]

        with patch("src.rag.indexing.classifier._classify_batch_with_llm", side_effect=fake_batch):
            out = classify_chunks(chunks, batch_size=2, delay=0)

        assert calls["count"] == 3
        assert all("economia" in c.topics for c in out)

    def test_classify_chunks_fails_on_batch_error(self, monkeypatch):
        from src.rag.common.models import Chunk
        from src.rag.indexing.classifier import classify_chunks

        monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")
        chunks = [Chunk(content="Investimento e crescimento económico")]

        with patch(
            "src.rag.indexing.classifier._classify_batch_with_llm",
            side_effect=RuntimeError("429 rate limit, retry after 1"),
        ) as mocked:
            with pytest.raises(RuntimeError, match="429 rate limit"):
                classify_chunks(chunks, batch_size=1, delay=0)

        assert mocked.call_count == 1
        assert chunks[0].topics == ["outros"]

    def test_classify_chunks_requires_api_key(self, monkeypatch):
        from src.rag.common.models import Chunk
        from src.rag.indexing.classifier import classify_chunks

        monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
        chunks = [Chunk(content="Baixar o IRS e simplificar o sistema fiscal")]

        with patch("src.rag.indexing.classifier._classify_batch_with_llm") as mocked:
            with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
                classify_chunks(chunks, batch_size=3, delay=0)

        assert mocked.call_count == 0
        assert chunks[0].topics == ["outros"]

    def test_classify_chunks_fails_on_partial_batch_response(self, monkeypatch):
        from src.rag.common.models import Chunk, TopicClassification
        from src.rag.indexing.classifier import classify_chunks

        monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")
        chunks = [
            Chunk(content="Crescimento económico e investimento"),
            Chunk(content="Reforço do SNS com mais médicos"),
        ]

        with patch(
            "src.rag.indexing.classifier._classify_batch_with_llm",
            return_value=[TopicClassification(categorias=["economia"], confianca=4, palavras_chave=[])],
        ):
            with pytest.raises(RuntimeError, match="Incomplete batch classification response"):
                classify_chunks(chunks, batch_size=2, delay=0)

        assert chunks[0].topics == ["outros"]
        assert chunks[1].topics == ["outros"]


class TestIndexingCheckpoints:
    """Tests for checkpoint save/load helpers in indexing pipeline."""

    def test_save_and_load_classified_checkpoint_roundtrip(self, tmp_path):
        from src.rag.common.models import Chunk, TopicClassification
        from src.rag.indexing.pipeline import load_classified_chunks, save_classified_chunks

        chunks = [
            Chunk(
                content="Reforço do SNS",
                party_name="Partido Socialista",
                ideology="left",
                topics=["saude"],
                topic_classification=TopicClassification(
                    categorias=["saude"],
                    confianca=5,
                    palavras_chave=["SNS"],
                ),
                metadata={"Major_Section": "Saúde"},
            )
        ]

        out_path = tmp_path / "checkpoint.json"
        save_classified_chunks(chunks, str(out_path), source_files=["data/1_markdown/ps/ps-2024.md"])

        loaded = load_classified_chunks(str(out_path))
        assert len(loaded) == 1
        assert loaded[0].topics == ["saude"]
        assert loaded[0].party_name == "Partido Socialista"
        assert loaded[0].topic_classification is not None
        assert loaded[0].topic_classification.confianca == 5

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
