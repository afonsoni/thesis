"""
Metrics for the evaluation stage.

Three families, all behind the ``Metric`` protocol in ``base`` so a RAGAS backend
can be added later without touching the runner:

- ``retrieval`` – hit@k, recall@k, MRR, nDCG@k (pure-Python, needs gold chunk keys).
- ``routing``   – query-type accuracy, party-set F1, topic-set F1.
- ``generation``– LLM-judge faithfulness, answer relevance, correctness.
"""

from src.rag.evaluation.metrics.base import Metric
from src.rag.evaluation.metrics.generation import GenerationJudgeMetric
from src.rag.evaluation.metrics.retrieval import RetrievalMetric
from src.rag.evaluation.metrics.routing import RoutingMetric

__all__ = ["Metric", "RetrievalMetric", "RoutingMetric", "GenerationJudgeMetric"]
