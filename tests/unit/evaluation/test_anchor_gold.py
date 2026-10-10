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
    assert not ag.parse_anchoring(str(md))[0].curated  # proposed, not yet signed off
    md.write_text(md.read_text().replace("- reviewed: no", "- reviewed: yes", 1))
    qs = {q.id: q for q in ag.parse_anchoring(str(md))}

    assert qs["q-01"].gold_chunk_keys == ["sha1:aa"]
    assert qs["q-01"].query_type == "single_party" and qs["q-01"].curated and qs["q-01"].split == "test"
    # No named party + exhaustive derives the fan-out route; nothing ticked -> not curated.
    assert qs["q-33"].query_type == "comparison" and not qs["q-33"].curated


@pytest.mark.unit
def test_unanswerable_question_is_curated_without_gold_chunks(tmp_path):
    md = tmp_path / "ANCHORING.md"
    md.write_text(
        "## q-52 — O que propõe o PCP sobre a legalização da canábis?\n\n"
        "- split: test\n- coverage: best_match\n- parties: Partido Comunista Português\n"
        "- topics: saude\n- answerable: no\n"
        "- reference: O programa do PCP não aborda a legalização da canábis.\n- reviewed: yes\n"
    )
    (q,) = ag.parse_anchoring(str(md))

    assert not q.answerable and q.gold_chunk_keys == [] and q.curated
