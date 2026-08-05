"""
Retrieval metrics (pure-Python, deterministic).

All operate on content keys (``sha1:...``): the ranked list of retrieved keys vs
the set of gold keys for a question. No embeddings or LLM involved, so these are
fast and unit-testable in isolation.
"""

from __future__ import annotations

import math
from typing import Dict, List, Sequence

from src.rag.evaluation.models import EvalQuestion, QuestionRun


def hit_at_k(retrieved: Sequence[str], gold: Sequence[str], k: int) -> float:
    """1.0 if any gold key appears in the top-k retrieved keys, else 0.0."""
    if not gold:
        return 0.0
    gold_set = set(gold)
    return 1.0 if any(key in gold_set for key in retrieved[:k]) else 0.0


def recall_at_k(retrieved: Sequence[str], gold: Sequence[str], k: int) -> float:
    """Fraction of gold keys present in the top-k retrieved keys."""
    if not gold:
        return 0.0
    gold_set = set(gold)
    found = sum(1 for key in set(retrieved[:k]) if key in gold_set)
    return found / len(gold_set)


def mrr(retrieved: Sequence[str], gold: Sequence[str]) -> float:
    """Reciprocal rank of the first gold key in the retrieved list (0 if none)."""
    if not gold:
        return 0.0
    gold_set = set(gold)
    for idx, key in enumerate(retrieved, start=1):
        if key in gold_set:
            return 1.0 / idx
    return 0.0


def ndcg_at_k(retrieved: Sequence[str], gold: Sequence[str], k: int) -> float:
    """Binary-relevance nDCG@k."""
    if not gold:
        return 0.0
    gold_set = set(gold)
    dcg = 0.0
    for i, key in enumerate(retrieved[:k], start=1):
        if key in gold_set:
            dcg += 1.0 / math.log2(i + 1)
    ideal_hits = min(len(gold_set), k)
    idcg = sum(1.0 / math.log2(i + 1) for i in range(1, ideal_hits + 1))
    return dcg / idcg if idcg > 0 else 0.0


class RetrievalMetric:
    """``Metric`` implementation bundling the retrieval scores at a fixed k."""

    needs_llm = False

    def __init__(self, k: int = 5):
        self.k = k
        self.name = f"retrieval@{k}"

    def score(self, run: QuestionRun, question: EvalQuestion) -> Dict[str, float]:
        gold = question.gold_chunk_keys
        if not gold:
            return {}
        retrieved: List[str] = run.retrieved_keys
        k = self.k
        return {
            f"hit@{k}": hit_at_k(retrieved, gold, k),
            f"recall@{k}": recall_at_k(retrieved, gold, k),
            "mrr": mrr(retrieved, gold),
            f"ndcg@{k}": ndcg_at_k(retrieved, gold, k),
        }
