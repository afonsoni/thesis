import pytest

from src.rag.common.models import Chunk, EmbeddedChunk
from src.rag.indexing import pipeline


class _FakeEmbedder:
    dimension = 4

    def embed_chunks(self, chunks, contextual=False):
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
    # Classifying runs always checkpoint; record instead of writing to data/.
    saved = []
    monkeypatch.setattr(
        pipeline, "save_classified_chunks", lambda *args, **kwargs: saved.append(kwargs.get("output_path"))
    )

    return {"markdown_dir": str(tmp_path), "store": store, "classify_calls": calls, "saved": saved}


@pytest.mark.unit
def test_index_documents_skips_classification_when_disabled(indexing_stubs):
    count = pipeline.index_documents(
        markdown_dir=indexing_stubs["markdown_dir"],
        use_llm_classification=False,
    )

    assert count == 1
    assert indexing_stubs["classify_calls"] == []
    # Topics stay at the model default, which is what disables topic filtering.
    assert indexing_stubs["store"].inserted[0].topics == ["outros"]
    # An unclassified checkpoint would silently poison a later --from-classified.
    assert indexing_stubs["saved"] == []
