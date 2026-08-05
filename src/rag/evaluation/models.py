"""
Pydantic models for the evaluation stage: gold-set questions, per-question run
records, and aggregated per-variant results.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class EvalQuestion(BaseModel):
    """A single gold-set question with ground-truth annotations."""

    id: str
    question: str
    query_type: str = "general"  # expected route: single_party/comparison/topic_exploration/general
    expected_parties: List[str] = Field(default_factory=list)
    expected_topics: List[str] = Field(default_factory=list)
    gold_chunk_keys: List[str] = Field(default_factory=list)  # sha1: content keys
    reference_answer: str = ""
    source_party: str = ""
    source_section: str = ""
    curated: bool = False  # True once a human has validated this question


class EvalDataset(BaseModel):
    """A gold set of evaluation questions."""

    format_version: int = 1
    created_at: str = ""
    questions: List[EvalQuestion] = Field(default_factory=list)

    def curated_only(self) -> "EvalDataset":
        return EvalDataset(
            format_version=self.format_version,
            created_at=self.created_at,
            questions=[q for q in self.questions if q.curated],
        )


class QuestionRun(BaseModel):
    """The outcome of running one variant on one question, plus its metric scores."""

    question_id: str
    variant: str

    # What retrieval produced
    retrieved_keys: List[str] = Field(default_factory=list)  # content keys in rank order
    retrieved_parties: List[str] = Field(default_factory=list)

    # What query analysis predicted (for routing metrics)
    predicted_query_type: str = "general"
    predicted_parties: List[str] = Field(default_factory=list)
    predicted_topics: List[str] = Field(default_factory=list)

    # What generation produced
    answer: str = ""
    context: str = ""  # concatenated retrieved content the judge sees

    latency_s: float = 0.0
    error: Optional[str] = None

    metrics: Dict[str, float] = Field(default_factory=dict)


class VariantResult(BaseModel):
    """Aggregated evaluation results for one variant over the whole dataset."""

    variant: str
    config: Dict = Field(default_factory=dict)
    created_at: str = ""
    dataset_size: int = 0
    aggregate: Dict[str, float] = Field(default_factory=dict)
    per_question: List[QuestionRun] = Field(default_factory=list)
