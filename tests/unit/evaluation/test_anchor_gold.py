import pytest

import scripts.anchor_gold as ag


@pytest.mark.unit
def test_rendered_ticks_and_labels_compile_into_gold_questions(tmp_path, monkeypatch):
    md = tmp_path / "ANCHORING.md"
    monkeypatch.setattr(ag, "ANCHORING_MD", str(md))
    seeds = [
        {"id": "q-01", "question": "Qual é a taxa única de IRS da IL?", "parties": ["Iniciativa Liberal"],
         "topics": ["impostos"], "coverage": "best_match", "split": "test", "stresses": "hybrid",
         "diff": "E", "note": "15%", "candidates": [
             {"key": "sha1:aa", "party": "Iniciativa Liberal", "section": "S", "content": "taxa única de 15%"},
             {"key": "sha1:bb", "party": "Iniciativa Liberal", "section": "S", "content": "outra coisa"}]},
        {"id": "q-33", "question": "O que propõem os partidos para o salário mínimo?", "parties": [],
         "topics": ["trabalho"], "coverage": "exhaustive", "split": "dev", "stresses": "routing",
         "diff": "M", "note": "", "candidates": []},
    ]
    ag.render(seeds, {"q-01": {"gold": ["sha1:aa"], "reference": "Uma taxa única de 15%."}})
    qs = {q.id: q for q in ag.parse_anchoring(str(md))}

    assert qs["q-01"].gold_chunk_keys == ["sha1:aa"]
    assert qs["q-01"].query_type == "single_party" and qs["q-01"].curated and qs["q-01"].split == "test"
    # No named party + exhaustive derives the fan-out route; nothing ticked -> not curated.
    assert qs["q-33"].query_type == "comparison" and not qs["q-33"].curated
