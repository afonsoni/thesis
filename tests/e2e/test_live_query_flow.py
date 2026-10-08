import pytest

from src.rag.common.models import Chunk, VALID_TOPICS
from src.rag.indexing.classifier import classify_chunks
import src.rag.retrieval.pipeline as retrieval_pipeline
from src.rag.generation.pipeline import generate
from src.rag.retrieval.pipeline import retrieve


@pytest.mark.e2e
@pytest.mark.live
def test_live_query_flow_smoke(require_live_e2e, seeded_searcher):
    """Live smoke: analyze -> expand -> retrieve -> synthesize."""
    retrieval_pipeline._searcher = seeded_searcher

    retrieval_result = retrieve(
        "Quais sao as propostas do Partido Socialista para a educacao?",
        top_k=3,
        expand_queries=True,
    )
    assert retrieval_result.results or retrieval_result.results_by_party

    answer = generate(retrieval_result)
    assert answer.answer.strip()
    assert answer.sources


@pytest.mark.e2e
@pytest.mark.live
def test_live_classification_on_manifesto_snippet(require_live_e2e):
    """Live classifier smoke using a short political-program snippet."""
    snippet = (
        "Reforcar o ensino profissional e criar bolsas de apoio para estudantes "
        "de baixos rendimentos, com foco na igualdade de acesso a educacao."
    )
    chunk = Chunk(
        content=snippet,
        metadata={"Major_Section": "Educacao"},
        party_name="Partido Socialista",
        ideology="left",
    )

    [classified] = classify_chunks([chunk])

    assert classified.topic_classification is not None
    assert classified.topic_classification.categorias
    assert all(topic in VALID_TOPICS for topic in classified.topic_classification.categorias)
    assert 1 <= classified.topic_classification.confianca <= 5
