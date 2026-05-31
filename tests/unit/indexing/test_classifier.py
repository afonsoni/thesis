from unittest.mock import patch

import pytest

from src.rag.common.models import Chunk, TopicClassification
from src.rag.indexing.classifier import classify_chunks


@pytest.mark.unit
class TestClassifierBatching:
    def test_classify_chunks_batches_requests(self, monkeypatch):
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
            output = classify_chunks(chunks, batch_size=2, delay=0)

        assert calls["count"] == 3
        assert all("economia" in chunk.topics for chunk in output)

    def test_classify_chunks_fails_on_batch_error(self, monkeypatch):
        monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")
        chunks = [Chunk(content="Investimento e crescimento economico")]

        with patch(
            "src.rag.indexing.classifier._classify_batch_with_llm",
            side_effect=RuntimeError("429 rate limit, retry after 1"),
        ) as mocked:
            with pytest.raises(RuntimeError):
                classify_chunks(chunks, batch_size=1, delay=0)

        assert mocked.call_count == 1
        assert chunks[0].topics == ["outros"]

    def test_classify_chunks_requires_api_key(self, monkeypatch):
        monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
        chunks = [Chunk(content="Baixar o IRS e simplificar o sistema fiscal")]

        with patch("src.rag.indexing.classifier._classify_batch_with_llm") as mocked:
            with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
                classify_chunks(chunks, batch_size=3, delay=0)

        assert mocked.call_count == 0
        assert chunks[0].topics == ["outros"]

    def test_classify_chunks_fails_on_partial_batch_response(self, monkeypatch):
        monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")
        chunks = [
            Chunk(content="Crescimento economico e investimento"),
            Chunk(content="Reforco do SNS com mais medicos"),
        ]

        with patch(
            "src.rag.indexing.classifier._classify_batch_with_llm",
            return_value=[TopicClassification(categorias=["economia"], confianca=4, palavras_chave=[])],
        ):
            with pytest.raises(RuntimeError, match="Incomplete batch classification response"):
                classify_chunks(chunks, batch_size=2, delay=0)

        assert chunks[0].topics == ["outros"]
        assert chunks[1].topics == ["outros"]
