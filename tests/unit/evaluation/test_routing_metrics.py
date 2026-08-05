import pytest

from src.rag.evaluation.metrics.routing import RoutingMetric, set_f1
from src.rag.evaluation.models import EvalQuestion, QuestionRun


@pytest.mark.unit
def test_set_f1_edge_cases():
    assert set_f1([], []) == 1.0  # both empty → perfect
    assert set_f1(["a"], []) == 0.0
    assert set_f1([], ["a"]) == 0.0
    assert set_f1(["a", "b"], ["a", "b"]) == 1.0


@pytest.mark.unit
def test_set_f1_partial_overlap():
    # predicted {a,b} vs expected {a}: precision 0.5, recall 1.0 → F1 = 2/3
    assert set_f1(["a", "b"], ["a"]) == pytest.approx(2 / 3)


@pytest.mark.unit
def test_routing_metric_scores_type_and_sets():
    metric = RoutingMetric()
    q = EvalQuestion(
        id="q", question="?", query_type="comparison",
        expected_parties=["LIVRE", "PS"], expected_topics=["saude"],
    )
    run = QuestionRun(
        question_id="q", variant="v",
        predicted_query_type="comparison",
        predicted_parties=["LIVRE", "PS"], predicted_topics=["saude"],
    )
    scores = metric.score(run, q)
    assert scores == {"query_type_acc": 1.0, "party_f1": 1.0, "topic_f1": 1.0}

    run.predicted_query_type = "general"
    run.predicted_topics = ["educacao"]
    scores = metric.score(run, q)
    assert scores["query_type_acc"] == 0.0
    assert scores["topic_f1"] == 0.0
