import pytest

from src.rag.common.models import Chunk, TopicClassification
from src.rag.indexing.pipeline import load_classified_chunks, save_classified_chunks


@pytest.mark.unit
def test_save_and_load_classified_checkpoint_roundtrip(tmp_path):
    chunks = [
        Chunk(
            content="Reforco do SNS",
            party_name="Partido Socialista",
            ideology="left",
            topics=["saude"],
            topic_classification=TopicClassification(
                categorias=["saude"],
                confianca=5,
                palavras_chave=["SNS"],
            ),
            metadata={"Major_Section": "Saude"},
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
