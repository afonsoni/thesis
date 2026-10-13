from unittest.mock import patch

import pytest

from src.rag.common.models import Chunk, TopicClassification
from src.rag.indexing.classifier import classify_chunks


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
        monkeypatch.setattr("src.rag.indexing.classifier.WAIT_OUT_ATTEMPTS", 2)
        monkeypatch.setattr("src.rag.common.llm_client.time.sleep", lambda s: None)
        chunks = [Chunk(content="Investimento e crescimento economico")]

        with patch(
            "src.rag.indexing.classifier._classify_batch_with_llm",
            side_effect=RuntimeError("429 rate limit, retry after 1"),
        ) as mocked:
            with pytest.raises(RuntimeError):
                classify_chunks(chunks, batch_size=1, delay=0)

        assert mocked.call_count == 2  # waited out once, then raised
        assert chunks[0].topics == ["outros"]

    def test_an_unanswered_chunk_is_asked_for_again_alone(self, monkeypatch):
        monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")
        chunks = [
            Chunk(content="Crescimento economico e investimento"),
            Chunk(content="Reforco do SNS com mais medicos"),
        ]
        tc = lambda topic: TopicClassification(categorias=[topic], confianca=4, palavras_chave=[])
        answers = iter([[tc("economia"), None], [tc("saude")]])

        with patch("src.rag.indexing.classifier._classify_batch_with_llm",
                   side_effect=lambda batch, model: next(answers)) as mocked:
            classify_chunks(chunks, batch_size=2, delay=0)

        assert mocked.call_args_list[1].args[0] == [chunks[1]]
        assert [c.topics for c in chunks] == [["economia"], ["saude"]]

    def test_classify_chunks_fails_when_a_chunk_stays_unanswered(self, monkeypatch):
        monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")
        monkeypatch.setattr("src.rag.indexing.classifier.WAIT_OUT_ATTEMPTS", 2)
        monkeypatch.setattr("src.rag.common.llm_client.time.sleep", lambda s: None)
        chunks = [Chunk(content="Crescimento economico"), Chunk(content="Reforco do SNS")]

        with patch("src.rag.indexing.classifier._classify_batch_with_llm",
                   side_effect=lambda batch, model: [None] * len(batch)):
            with pytest.raises(RuntimeError, match="Incomplete batch classification response"):
                classify_chunks(chunks, batch_size=2, delay=0)

        assert [c.topics for c in chunks] == [["outros"], ["outros"]]

    def test_answers_are_placed_by_id_not_position(self, monkeypatch):
        from src.rag.indexing import classifier

        monkeypatch.setattr(classifier, "generate_structured_batch", lambda **k: [
            {"id": 2, "categorias": ["saude"]}, {"id": 0, "categorias": ["economia"]}])
        placed = classifier._classify_batch_with_llm([Chunk(content=f"t{i}") for i in range(3)], "m")

        assert [p and p.categorias for p in placed] == [["economia"], None, ["saude"]]


def test_a_batch_comes_back_whole_from_json_mode(monkeypatch):
    """JSON mode returns one object: the list is asked for, and read, inside it."""
    from src.rag.common import llm_client

    monkeypatch.setattr(llm_client, "generate_text", lambda *a, **k: '{"items": [{"id": 0}, {"id": 1}]}')
    assert llm_client.generate_structured_batch("p") == [{"id": 0}, {"id": 1}]
