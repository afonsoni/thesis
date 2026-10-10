import pytest

from src.rag.common.models import Chunk
from src.rag.indexing.embedder import Embedder


@pytest.mark.unit
def test_contextual_embedding_prefixes_party_and_section_but_keeps_content():
    """Only the embedded text changes, so gold keys (hashes of content) still match."""
    embedder = Embedder.__new__(Embedder)
    seen = []
    embedder.encode_batch = lambda texts, batch_size=64: seen.extend(texts) or [[0.0]] * len(texts)
    chunk = Chunk(
        content="Abolir a tourada.",
        party_name="Pessoas-Animais-Natureza",
        metadata={"Title": "Agenda", "Major_Section": "Animais", "sub_chunk_index": 2},
    )

    (out,) = embedder.embed_chunks([chunk], contextual=True)
    embedder.embed_chunks([chunk])

    assert seen == ["Pessoas-Animais-Natureza | Agenda > Animais\nAbolir a tourada.", "Abolir a tourada."]
    assert out.content == "Abolir a tourada."
