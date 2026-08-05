import pytest

from src.rag.common.models import Chunk, EmbeddedChunk
from src.rag.indexing import pipeline


class _FakeEmbedder:
    dimension = 4

    def embed_chunks(self, chunks):
        return [
            EmbeddedChunk(**chunk.model_dump(), embedding=[0.0] * self.dimension)
            for chunk in chunks
        ]


class _FakeStore:
    def __init__(self):
        self.inserted = []

    def connect(self):
        pass

    def drop_table(self):
        pass

    def create_table(self, embedding_dim):
        pass

    def insert_chunks(self, chunks):
        self.inserted = list(chunks)
        return len(chunks)

    def close(self):
        pass


@pytest.fixture
def indexing_stubs(monkeypatch, tmp_path):
    """Stub out chunking, embedding and storage so only the classify step matters."""
    md_path = tmp_path / "ad" / "ad-2024.md"
    md_path.parent.mkdir(parents=True)
    md_path.write_text("# Saude\nReforco do SNS.\n", encoding="utf-8")

    monkeypatch.setattr(
        pipeline,
        "chunk_markdown_file",
        lambda *args, **kwargs: [
            Chunk(content="Reforco do SNS", party_name="AD", ideology="right")
        ],
    )

    store = _FakeStore()
    monkeypatch.setattr(pipeline, "Embedder", lambda: _FakeEmbedder())
    monkeypatch.setattr(pipeline, "VectorStore", lambda: store)

    calls = []

    def _spy_classify(chunks, **kwargs):
        calls.append(chunks)
        for chunk in chunks:
            chunk.topics = ["saude"]
        return chunks

    monkeypatch.setattr(pipeline, "classify_chunks", _spy_classify)

    return {"markdown_dir": str(tmp_path), "store": store, "classify_calls": calls}


@pytest.mark.unit
def test_index_documents_skips_classification_when_disabled(indexing_stubs):
    count = pipeline.index_documents(
        markdown_dir=indexing_stubs["markdown_dir"],
        use_llm_classification=False,
        save_checkpoint=False,
    )

    assert count == 1
    assert indexing_stubs["classify_calls"] == []
    # Topics stay at the model default, which is what disables topic filtering.
    assert indexing_stubs["store"].inserted[0].topics == ["outros"]


@pytest.mark.unit
def test_index_documents_classifies_when_enabled(indexing_stubs):
    count = pipeline.index_documents(
        markdown_dir=indexing_stubs["markdown_dir"],
        use_llm_classification=True,
        save_checkpoint=False,
    )

    assert count == 1
    assert len(indexing_stubs["classify_calls"]) == 1
    assert indexing_stubs["store"].inserted[0].topics == ["saude"]


@pytest.mark.unit
def test_index_documents_writes_no_checkpoint_without_classification(
    indexing_stubs, tmp_path, monkeypatch
):
    """An unclassified checkpoint would silently poison a later --from-classified."""
    saved = []
    monkeypatch.setattr(
        pipeline,
        "save_classified_chunks",
        lambda *args, **kwargs: saved.append(kwargs.get("output_path")),
    )

    pipeline.index_documents(
        markdown_dir=indexing_stubs["markdown_dir"],
        use_llm_classification=False,
        checkpoint_output_path=str(tmp_path / "checkpoint.json"),
    )

    assert saved == []


@pytest.mark.unit
def test_classify_only_rejects_disabled_classification(indexing_stubs):
    with pytest.raises(ValueError, match="requires LLM classification"):
        pipeline.index_documents(
            markdown_dir=indexing_stubs["markdown_dir"],
            use_llm_classification=False,
            classify_only=True,
        )
