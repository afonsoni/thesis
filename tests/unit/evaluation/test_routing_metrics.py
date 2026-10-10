import pytest

from src.rag.evaluation.metrics.routing import RoutingMetric, set_f1
from src.rag.evaluation.models import EvalQuestion, QuestionRun


def test_set_f1_edge_cases():
    assert set_f1([], []) == 1.0  # both empty → perfect
    assert set_f1(["a"], []) == 0.0
    assert set_f1([], ["a"]) == 0.0
    assert set_f1(["a", "b"], ["a", "b"]) == 1.0
    # predicted {a,b} vs expected {a}: precision 0.5, recall 1.0 → F1 = 2/3
    assert set_f1(["a", "b"], ["a"]) == pytest.approx(2 / 3)


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
    assert scores == {
        "query_type_acc": 1.0,
        "coverage_acc": 1.0,
        "party_f1": 1.0,
        "topic_f1": 1.0,
    }

    run.predicted_query_type = "general"
    run.predicted_topics = ["educacao"]
    scores = metric.score(run, q)
    assert scores["query_type_acc"] == 0.0
    assert scores["topic_f1"] == 0.0


def test_coverage_isolates_the_aggregative_failure():
    """Right parties, right topic, wrong coverage — the flat-search failure.

    Nothing else in the metric set moves: the analysis correctly reports that
    no party was named, and still routes to a search that can omit most of them.
    """
    metric = RoutingMetric()
    q = EvalQuestion(
        id="q",
        question="O que defende cada partido sobre saude?",
        query_type="comparison",
        coverage="exhaustive",
        expected_topics=["saude"],
    )
    run = QuestionRun(
        question_id="q", variant="v",
        predicted_query_type="topic_exploration",
        predicted_coverage="best_match",
        predicted_topics=["saude"],
    )

    scores = metric.score(run, q)

    assert scores["party_f1"] == 1.0   # both empty: nothing was named
    assert scores["topic_f1"] == 1.0
    assert scores["coverage_acc"] == 0.0
    assert scores["query_type_acc"] == 0.0


def test_gold_labels_must_agree_with_each_other():
    """A route the pipeline cannot derive is a broken annotation, not a hard question."""
    with pytest.raises(ValueError, match="contradicts"):
        EvalQuestion(
            id="q-bad",
            question="Quais as propostas sobre saude?",
            query_type="comparison",   # implies a fan-out...
            coverage="best_match",     # ...but nothing asks for one
            expected_topics=["saude"],
        )
