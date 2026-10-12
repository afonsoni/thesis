from unittest.mock import patch

import pytest

from src.rag.retrieval.query_expander import expand_query


def test_expand_query_deduplicates_and_keeps_original():
    model_output = "Pergunta A\nPergunta B\nPergunta A\nPergunta C"
    with patch("src.rag.retrieval.query_expander.generate_text", return_value=model_output):
        expanded = expand_query("Pergunta original", n_queries=3)

    assert expanded[0] == "Pergunta original"
    assert len(expanded) == 4
    assert len({item.lower() for item in expanded}) == len(expanded)


def test_expand_query_strict_raises_instead_of_degrading():
    with patch("src.rag.retrieval.query_expander.generate_text", side_effect=RuntimeError("rate limited")):
        with pytest.raises(RuntimeError):
            expand_query("Pergunta original", n_queries=4, strict=True)


@pytest.mark.parametrize("synonyms", [False, True])
def test_expand_query_asks_for_manifesto_vocabulary_only_when_told(synonyms):
    from src.rag.retrieval.prompts import QUERY_EXPANSION_SYNONYMS

    with patch("src.rag.retrieval.query_expander.generate_text", return_value="A") as gen:
        expand_query("Pergunta original", n_queries=2, synonyms=synonyms)
    prompt = gen.call_args.args[0]
    assert (QUERY_EXPANSION_SYNONYMS in prompt) is synonyms
    assert prompt.endswith("Perguntas reformuladas:")


def test_a_question_is_expanded_once_per_process_but_a_failure_is_retried():
    """Every eval variant must search with the same expansions; a failure must not stick."""
    with patch("src.rag.retrieval.query_expander.generate_text", side_effect=RuntimeError("down")):
        assert expand_query("Pergunta original", n_queries=2) == ["Pergunta original"]
    with patch("src.rag.retrieval.query_expander.generate_text", return_value="A\nB") as gen:
        first = expand_query("Pergunta original", n_queries=2)
        second = expand_query("Pergunta original", n_queries=2)
    assert first == second == ["Pergunta original", "A", "B"]
    assert gen.call_count == 1
