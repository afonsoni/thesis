import math

import pytest

from src.rag.evaluation.metrics.retrieval import (
    RetrievalMetric,
    hit_at_k,
    mrr,
    ndcg_at_k,
    recall_at_k,
)
from src.rag.evaluation.models import EvalQuestion, QuestionRun


def test_hit_at_k_respects_cutoff():
    retrieved = ["x", "g1", "y"]
    assert hit_at_k(retrieved, ["g1"], k=5) == 1.0
    assert hit_at_k(retrieved, ["g1"], k=1) == 0.0  # g1 is at rank 2
    assert hit_at_k(retrieved, [], k=5) == 0.0  # no gold → 0


def test_recall_at_k_counts_unique_gold_found():
    assert recall_at_k(["g1", "g2", "z"], ["g1", "g2"], k=5) == 1.0
    assert recall_at_k(["g1", "z", "w"], ["g1", "g2"], k=5) == 0.5
    assert recall_at_k(["g2"], ["g1", "g2"], k=1) == 0.5


def test_mrr_uses_first_gold_rank():
    assert mrr(["x", "g1", "y"], ["g1"]) == pytest.approx(0.5)
    assert mrr(["g1", "x"], ["g1"]) == pytest.approx(1.0)
    assert mrr(["a", "b"], ["g1"]) == 0.0


def test_ndcg_matches_manual_computation():
    # single gold at rank 2 → dcg = 1/log2(3), idcg = 1/log2(2) = 1
    assert ndcg_at_k(["x", "g1", "y"], ["g1"], k=5) == pytest.approx(1 / math.log2(3))
    # gold at rank 1 → perfect
    assert ndcg_at_k(["g1", "x"], ["g1"], k=5) == pytest.approx(1.0)


def test_retrieval_metric_bundle_and_empty_gold():
    metric = RetrievalMetric()
    run = QuestionRun(question_id="q", variant="v", retrieved_keys=["x", "g1"])
    q = EvalQuestion(id="q", question="?", gold_chunk_keys=["g1"])
    scores = metric.score(run, q)
    assert scores["hit"] == 1.0 and scores["mrr"] == pytest.approx(0.5)

    # No gold keys → metric yields nothing (so it's excluded from averages).
    assert metric.score(run, EvalQuestion(id="q", question="?")) == {}


def test_retrieval_metric_scores_the_whole_list_without_a_cutoff():
    # A fan-out hands generation more than top_k chunks; gold at rank 7 counts.
    run = QuestionRun(question_id="q", variant="v", retrieved_keys=[f"x{i}" for i in range(6)] + ["g1"])
    scores = RetrievalMetric().score(run, EvalQuestion(id="q", question="?", gold_chunk_keys=["g1", "g2"]))
    assert scores["hit"] == 1.0 and scores["recall"] == 0.5
