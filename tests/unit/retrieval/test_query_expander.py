from unittest.mock import patch

import pytest

from src.rag.retrieval.query_expander import expand_query


@pytest.mark.unit
def test_expand_query_deduplicates_and_keeps_original():
    model_output = "Pergunta A\nPergunta B\nPergunta A\nPergunta C"
    with patch("src.rag.retrieval.query_expander.generate_text", return_value=model_output):
        expanded = expand_query("Pergunta original", n_queries=3)

    assert expanded[0] == "Pergunta original"
    assert len(expanded) == 4
    assert len({item.lower() for item in expanded}) == len(expanded)


@pytest.mark.unit
def test_expand_query_strict_raises_instead_of_degrading():
    with patch("src.rag.retrieval.query_expander.generate_text", side_effect=RuntimeError("rate limited")):
        with pytest.raises(RuntimeError):
            expand_query("Pergunta original", n_queries=4, strict=True)
