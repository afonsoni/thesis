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
