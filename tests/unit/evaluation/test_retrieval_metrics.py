import math

import pytest

from src.rag.evaluation.metrics.retrieval import (
    RetrievalMetric,
    aspect_recall,
    capped_recall,
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


def test_capped_recall_divides_by_what_the_list_could_hold():
    gold = [f"g{i}" for i in range(20)]
    # 3 slots, all gold: plain recall is 3/20, capped recall is perfect.
    assert capped_recall(["g0", "g1", "g2"], gold) == 1.0
    assert capped_recall(["g0", "x", "y"], gold) == pytest.approx(1 / 3)
    # Fewer gold than slots: same as plain recall.
    assert capped_recall(["g0", "x", "y", "z"], ["g0", "g1"]) == 0.5
    assert capped_recall([], gold) == 0.0


def test_aspect_recall_counts_sections_not_chunks():
    aspects = {"a1": "PS > Saúde", "a2": "PS > Saúde", "b1": "PCP > Saúde", "c1": "PAN > Saúde"}
    # Two chunks of one section reach one aspect of three.
    assert aspect_recall(["a1", "a2", "x"], aspects) == pytest.approx(1 / 3)
    assert aspect_recall(["a1", "b1", "c1"], aspects) == 1.0
    q = EvalQuestion(id="q", question="?", gold_chunk_keys=list(aspects), gold_aspects=aspects)
    scores = RetrievalMetric().score(QuestionRun(question_id="q", variant="v", retrieved_keys=["b1"]), q)
    assert scores["aspect_recall"] == pytest.approx(1 / 3) and scores["recall_capped"] == 1.0
