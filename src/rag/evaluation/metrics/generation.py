"""
Generation metrics.

- ``faithfulness`` (reference-free, RAGAS): the share of the answer's claims that
  the generator's context supports.
- ``correctness`` / ``correctness_recall`` (reference-based, after RAGAS answer
  correctness): the answer's claims are checked against the curated reference
  answer (precision) and the reference's claims against the answer (recall);
  ``correctness`` is their F1. Recall alone reads "did the answer say what the
  reference says", without penalising true detail the reference left out.
- ``answer_relevance`` (reference-free): a holistic 1-5 judgement mapped to [0, 1].
- ``abstention`` (unanswerable questions only): 1 if the answer declined, else 0.
  Its mean is the share of unanswerable questions the system refused.
- ``false_refusal`` (answerable questions only): 1 if the answer declined. Both
  are read off the relevance call, so they add no judge call.

A score whose judge calls failed, or that has nothing to score (an answer with
no claims), is omitted rather than set to 0, so an outage cannot pass for a bad
answer. The claims and verdicts behind each score are kept on
``QuestionRun.judgements`` for auditing and for the human agreement check.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

from src.rag.evaluation.judge import extract_claims, judge_answer_relevance, verify_claims
from src.rag.evaluation.models import EvalQuestion, QuestionRun


def _supported_share(verdicts) -> Optional[float]:
    return sum(v.supported for v in verdicts) / len(verdicts) if verdicts else None


def _f1(p: Optional[float], r: Optional[float]) -> Optional[float]:
    if p is None or r is None:
        return None
    return 0.0 if p + r == 0 else 2 * p * r / (p + r)


def _log(claims: List[str], verdicts) -> List[dict]:
    return [{"claim": c, "supported": v.supported, "reason": v.reason} for c, v in zip(claims, verdicts)]


class GenerationJudgeMetric:
    """``Metric`` scoring the generated answer with claim-level and holistic judges."""

    name = "generation"
    needs_llm = True

    def __init__(self, model: Optional[str] = None):
        self.model = model
        # Reference claims depend only on the question, so every variant in a
        # run reuses them instead of re-extracting per variant.
        self._reference_claims: Dict[Tuple[str, str], Optional[List[str]]] = {}

    def _reference(self, question: EvalQuestion) -> Optional[List[str]]:
        key = (question.id, question.reference_answer)
        if key not in self._reference_claims:
            self._reference_claims[key] = extract_claims(question.question, question.reference_answer, self.model)
        return self._reference_claims[key]

    def score(self, run: QuestionRun, question: EvalQuestion) -> Dict[str, float]:
        if not run.answer.strip():
            return {}
        if not question.answerable:
            # The right answer is a refusal: faithfulness and correctness of one
            # measure nothing, so only whether it declined is scored.
            rel = judge_answer_relevance(question.question, run.answer, self.model)
            if rel is None:
                return {}
            run.judgements["abstention"] = {"abstained": rel.abstained, "rationale": rel.rationale}
            return {"abstention": float(rel.abstained)}
        scores: Dict[str, float] = {}

        claims = extract_claims(question.question, run.answer, self.model)
        if claims:
            verdicts = verify_claims(claims, run.context, self.model)
            if verdicts is not None:
                scores["faithfulness"] = _supported_share(verdicts)
                run.judgements["faithfulness"] = _log(claims, verdicts)

        if claims and question.reference_answer.strip():
            ref_claims = self._reference(question)
            if ref_claims:
                precision_v = verify_claims(claims, question.reference_answer, self.model)
                recall_v = verify_claims(ref_claims, run.answer, self.model)
                precision = _supported_share(precision_v) if precision_v is not None else None
                recall = _supported_share(recall_v) if recall_v is not None else None
                if recall is not None:
                    scores["correctness_recall"] = recall
                    run.judgements["correctness_recall"] = _log(ref_claims, recall_v)
                f1 = _f1(precision, recall)
                if f1 is not None:
                    scores["correctness"] = f1
                    run.judgements["correctness_precision"] = _log(claims, precision_v)

        rel = judge_answer_relevance(question.question, run.answer, self.model)
        if rel is not None:
            scores["answer_relevance"] = rel.normalized
            scores["false_refusal"] = float(rel.abstained)
            run.judgements["answer_relevance"] = {
                "score": rel.score, "abstained": rel.abstained, "rationale": rel.rationale,
            }
        return scores
