import csv
import os


from src.rag.evaluation.models import QuestionRun, VariantResult
from src.rag.evaluation.report import write_leaderboard


def _make_result(variant: str, hit: float, faith: float) -> VariantResult:
    return VariantResult(
        variant=variant,
        created_at="2026-01-01T00:00:00",
        dataset_size=2,
        aggregate={
            "hit": hit,
            "faithfulness": faith,
            "avg_latency_s": 1.2,
            "error_rate": 0.0,
        },
        per_question=[QuestionRun(question_id="q-0001", variant=variant)],
    )


def test_leaderboard_orders_columns_and_lists_all_variants(tmp_path):
    results = [_make_result("naive", 0.4, 0.5), _make_result("current", 0.8, 0.9)]
    md_path = write_leaderboard(results, str(tmp_path))
    content = open(md_path, encoding="utf-8").read()

    assert "| naive |" in content and "| current |" in content
    # retrieval metric column comes before generation + latency columns
    header = next(line for line in content.splitlines() if line.startswith("| variant |"))
    assert header.index("hit") < header.index("faithfulness") < header.index("avg_latency_s")

    # CSV emitted alongside with matching rows
    csv_path = os.path.join(tmp_path, "leaderboard.csv")
    rows = list(csv.reader(open(csv_path, encoding="utf-8")))
    assert rows[0][0] == "variant"
    assert {r[0] for r in rows[1:]} == {"naive", "current"}


def test_leaderboard_notes_when_fallback_models_answered(tmp_path):
    r = _make_result("current", 0.8, 0.9)
    r.models_used = {"google/gemma-4-26b-a4b-it:free": 40, "nvidia/nemotron-3-ultra-550b-a55b:free": 3}
    content = open(write_leaderboard([r], str(tmp_path)), encoding="utf-8").read()
    assert "Fallback models answered" in content and "nemotron" in content


def test_broad_questions_get_their_own_table(tmp_path):
    runs = [QuestionRun(question_id="q-01", variant="v", metrics={"recall": 0.2}),
            QuestionRun(question_id="q-02", variant="v", metrics={"recall": 1.0})]
    r = VariantResult(variant="v", per_question=runs, aggregate={"recall": 0.6})
    content = open(write_leaderboard([r], str(tmp_path), broad_ids={"q-01"}), encoding="utf-8").read()
    broad = content.split("## Broad questions")[1]
    assert "The 1 questions" in broad and "| v | 0.200 |" in broad
    # Without broad ids there is no such section.
    assert "## Broad questions" not in open(write_leaderboard([r], str(tmp_path)), encoding="utf-8").read()


def test_the_judge_and_a_variant_generator_are_not_reported_as_fallbacks(tmp_path, monkeypatch):
    from src.rag.evaluation import report

    monkeypatch.setattr(report.config, "get", lambda key, default=None: {
        "llm.openrouter.model": "google/gemma", "evaluation.judge_model": "qwen/judge"}.get(key, default))
    r = _make_result("current_strong", 0.8, 0.9)
    r.config = {"generation_model": "openai/strong"}
    r.models_used = {"google/gemma": 2, "qwen/judge": 40, "openai/strong": 25}
    content = open(write_leaderboard([r], str(tmp_path)), encoding="utf-8").read()
    assert "Fallback models answered" not in content


def test_a_metric_a_variant_never_produced_is_a_blank_cell_not_nan(tmp_path):
    with_hit = _make_result("current", 0.8, 0.9)
    with_hit.per_question[0].metrics = {"hit": 0.8, "faithfulness": 0.9}
    closed = _make_result("no_retrieval", 0.0, 0.5)
    closed.aggregate = {"faithfulness": 0.5, "avg_latency_s": 1.0, "error_rate": 0.0}
    closed.per_question[0].metrics = {"faithfulness": 0.5}
    content = open(write_leaderboard([with_hit, closed], str(tmp_path)), encoding="utf-8").read()
    assert "| nan" not in content and " nan " not in content
    assert "| no_retrieval |  |" in content


def test_leaderboard_names_the_code_its_numbers_came_from(tmp_path):
    a, b = _make_result("naive", 0.4, 0.5), _make_result("current", 0.8, 0.9)
    a.code_version, b.code_version = "abc1234", "abc1234-dirty"
    content = open(write_leaderboard([a, b], str(tmp_path)), encoding="utf-8").read()
    assert "_Code: `abc1234, abc1234-dirty`_" in content


def test_code_version_is_a_short_commit_with_an_optional_dirty_mark():
    import re

    from src.rag.evaluation.pipeline import code_version

    assert re.fullmatch(r"[0-9a-f]{7,}(-dirty)?", code_version())
