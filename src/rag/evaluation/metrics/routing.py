"""
Routing metrics (pure-Python, deterministic).

Validate the query-analysis/routing layer — the system's core contribution over
naive RAG — by comparing predicted query type / parties / topics against the
gold annotations.
"""

from __future__ import annotations

from typing import Dict, Sequence

from src.rag.evaluation.models import EvalQuestion, QuestionRun


def set_f1(predicted: Sequence[str], expected: Sequence[str]) -> float:
    """F1 over two sets of labels. Empty-vs-empty counts as a perfect match."""
    pred, exp = set(predicted), set(expected)
    if not pred and not exp:
        return 1.0
    if not pred or not exp:
        return 0.0
    tp = len(pred & exp)
    if tp == 0:
        return 0.0
    precision = tp / len(pred)
    recall = tp / len(exp)
    return 2 * precision * recall / (precision + recall)


class RoutingMetric:
    """``Metric`` implementation for query-analysis correctness."""

    name = "routing"

    def score(self, run: QuestionRun, question: EvalQuestion) -> Dict[str, float]:
        """Score the analysis against the gold annotations.

        ``query_type_acc`` is not independent of the other three: the route is
        derived from the party set and the coverage decision, so it can only be
        right when those are. It is kept because it is the headline "did the
        pipeline pick the right strategy" number and it is comparable with runs
        recorded before ``coverage`` existed — but read it as a summary of the
        components below, not as extra evidence.

        ``coverage_acc`` is the one that isolates the aggregative failure: an
        analysis can name the right parties (none) and the right topic, and
        still answer from a flat top_k that omits half of them.
        """
        return {
            "query_type_acc": 1.0 if run.predicted_query_type == question.query_type else 0.0,
            "coverage_acc": 1.0 if run.predicted_coverage == question.coverage else 0.0,
            "party_f1": set_f1(run.predicted_parties, question.expected_parties),
            "topic_f1": set_f1(run.predicted_topics, question.expected_topics),
        }
