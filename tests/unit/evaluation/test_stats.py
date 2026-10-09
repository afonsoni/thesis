import pytest

from src.rag.evaluation.models import QuestionRun, VariantResult
from src.rag.evaluation.report import write_leaderboard
from src.rag.evaluation.stats import bootstrap_ci, paired_diff


@pytest.mark.unit
def test_bootstrap_ci_brackets_the_mean_and_is_reproducible():
    values = [0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0]
    lo, hi = bootstrap_ci(values)
    assert lo <= sum(values) / len(values) <= hi
    assert bootstrap_ci(values) == (lo, hi)
    assert bootstrap_ci([1.0]) is None


@pytest.mark.unit
def test_paired_diff_uses_shared_questions_only():
    a = {f"q{i}": 0.5 for i in range(10)}
    b = {f"q{i}": 0.7 for i in range(10)} | {"extra": 0.0}
    mean, (lo, hi), n = paired_diff(a, b)
    assert n == 10 and mean == pytest.approx(0.2) and lo == pytest.approx(0.2) and hi == pytest.approx(0.2)


def _result(variant, scores):
    runs = [QuestionRun(question_id=f"q{i}", variant=variant, metrics={"hit": s}) for i, s in enumerate(scores)]
    return VariantResult(variant=variant, dataset_size=len(runs), per_question=runs,
                         aggregate={"hit": sum(scores) / len(scores)})


@pytest.mark.unit
def test_leaderboard_reports_intervals_and_bolds_a_clear_paired_gain(tmp_path):
    base = _result("naive", [0, 0, 1, 0, 1, 0, 0, 1, 0, 0])
    better = _result("current", [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    content = open(write_leaderboard([base, better], str(tmp_path)), encoding="utf-8").read()
    assert "Paired difference vs `naive`" in content
    assert "| current | **+0.700" in content
    assert "0.300 [" in content  # mean with its interval


@pytest.mark.unit
def test_leaderboard_means_cover_the_same_questions_and_split_gets_its_own_file(tmp_path):
    base = _result("naive", [0, 0, 0, 1])
    other = _result("current", [1, 1, 1, 1])
    other.per_question[3].metrics = {}  # q3 errored in this arm: drop it from both
    other.per_question[3].error = "generation: 429"
    for r in (base, other):
        r.split = "test"
    path = write_leaderboard([base, other], str(tmp_path))
    assert path.endswith("leaderboard-test.md")
    content = open(path, encoding="utf-8").read()
    assert "| naive | 0.000" in content  # mean over q0-q2, not 0.25 over all four
    assert "split `test`" in content
