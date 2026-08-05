"""
The ``Metric`` protocol.

A metric maps one (run, question) pair to a dict of named scores in [0, 1].
Keeping this as a Protocol means alternative backends — e.g. a RAGAS adapter —
can be dropped in later purely by implementing ``score`` (and ``needs_llm``),
without changes to the runner or report.
"""

from __future__ import annotations

from typing import Dict, Protocol, runtime_checkable

from src.rag.evaluation.models import EvalQuestion, QuestionRun


@runtime_checkable
class Metric(Protocol):
    name: str
    needs_llm: bool

    def score(self, run: QuestionRun, question: EvalQuestion) -> Dict[str, float]:
        """Return a mapping of metric-name → score in [0, 1]. May be empty."""
        ...
