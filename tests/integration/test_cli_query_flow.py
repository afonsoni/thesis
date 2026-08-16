from types import SimpleNamespace
from unittest.mock import patch

import pytest

from main import cmd_query
from src.rag.common.models import (
    AnalyzedQuery,
    GeneratedAnswer,
    QueryType,
    RetrievalResult,
    SearchResult,
)


@pytest.mark.integration
def test_cmd_query_prints_answer_and_sources(capsys):
    args = SimpleNamespace(question="Pergunta de teste", top_k=2, no_expand=True)
    retrieval = RetrievalResult(
        query=AnalyzedQuery(original_query="Pergunta de teste"),
        results=[
            SearchResult(
                id="doc-1",
                content="Conteudo",
                party_name="Partido Socialista",
                similarity=0.91,
            )
        ],
    )
    generated = GeneratedAnswer(
        answer="Resposta de teste",
        sources=[
            {
                "party": "Partido Socialista",
                "topics": ["educacao"],
                "section": "Educacao",
                "similarity": 0.91,
            }
        ],
        query_type=QueryType.GENERAL,
    )

    with patch("src.rag.retrieval.pipeline.retrieve", return_value=retrieval):
        with patch("src.rag.generation.pipeline.generate", return_value=generated):
            cmd_query(args)

    captured = capsys.readouterr().out
    assert "Resposta de teste" in captured
    assert "Fontes (1):" in captured
    assert "Partido Socialista" in captured
