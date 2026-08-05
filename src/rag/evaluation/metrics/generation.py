"""
Generation metrics via LLM-as-judge.

Faithfulness and answer-relevance are reference-free (need the retrieved context
and the question). Correctness is reference-based and only scored when the gold
question carries a reference answer. Failed judge calls are omitted (not zero),
so a transient API error doesn't silently depress the score.
"""

from __future__ import annotations

from typing import Dict, Optional

from src.rag.evaluation.judge import (
    judge_answer_relevance,
    judge_correctness,
    judge_faithfulness,
)
from src.rag.evaluation.models import EvalQuestion, QuestionRun


class GenerationJudgeMetric:
    """``Metric`` implementation that scores the generated answer with an LLM judge."""

    name = "generation"
    needs_llm = True

    def __init__(self, model: Optional[str] = None):
        self.model = model

    def score(self, run: QuestionRun, question: EvalQuestion) -> Dict[str, float]:
        if not run.answer.strip():
            return {}

        scores: Dict[str, float] = {}

        faith = judge_faithfulness(question.question, run.answer, run.context, self.model)
        if faith is not None:
            scores["faithfulness"] = faith.normalized

        rel = judge_answer_relevance(question.question, run.answer, self.model)
        if rel is not None:
            scores["answer_relevance"] = rel.normalized

        if question.reference_answer.strip():
            corr = judge_correctness(
                question.question, run.answer, question.reference_answer, self.model
            )
            if corr is not None:
                scores["correctness"] = corr.normalized

        return scores
