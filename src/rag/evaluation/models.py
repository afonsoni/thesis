"""
Pydantic models for the evaluation stage: gold-set questions, per-question run
records, and aggregated per-variant results.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, Field, model_validator

from src.rag.common.models import AnalyzedQuery, Coverage


class EvalQuestion(BaseModel):
    """A single gold-set question with ground-truth annotations.

    Annotations describe the *question*, never a retrieval plan, so the same
    labels stay valid for every variant in the ladder. Encoding a plan here
    (how many chunks, which filters) would make the gold set specific to one
    configuration, and the arms could no longer be compared on it.
    """

    id: str
    question: str
    query_type: str = "general"  # expected route: single_party/comparison/topic_exploration/general
    # Whether answering requires every party in scope to be represented, or
    # only the best-matching passages. Annotated separately from ``query_type``
    # because that label cannot express it: "o que defende cada partido sobre
    # X" and "quais as propostas sobre X" both read as topic questions, and
    # only the first is wrong when a party is missing.
    coverage: str = "best_match"  # exhaustive | best_match
    # Parties *named or unambiguously implied by the question text* — not the
    # parties a run ought to search. An exhaustive question names none and
    # still searches all eight; scoring it against a list of eight would
    # penalise the analyzer for correctly reporting that none were named.
    expected_parties: List[str] = Field(default_factory=list)
    expected_topics: List[str] = Field(default_factory=list)
    gold_chunk_keys: List[str] = Field(default_factory=list)  # sha1: content keys
    reference_answer: str = ""
    source_party: str = ""
    source_section: str = ""
    curated: bool = False  # True once a human has validated this question

    @model_validator(mode="after")
    def _query_type_agrees_with_the_other_labels(self) -> "EvalQuestion":
        """Reject gold rows whose route label contradicts parties/coverage.

        ``AnalyzedQuery`` derives ``query_type`` from exactly these two fields,
        so an annotation that disagrees describes a route the pipeline cannot
        produce: the question would score zero however well it was analysed.
        Catching it here beats debugging it as a mysteriously failing arm.
        """
        derived = AnalyzedQuery(
            original_query=self.question,
            parties=self.expected_parties,
            coverage=Coverage(self.coverage),
            topics=self.expected_topics,
        ).query_type.value
        if self.query_type != derived:
            raise ValueError(
                f"question {self.id}: query_type={self.query_type!r} contradicts "
                f"expected_parties={self.expected_parties} and coverage="
                f"{self.coverage!r}, which derive {derived!r}"
            )
        return self


class EvalDataset(BaseModel):
    """A gold set of evaluation questions."""

    # 2 adds the ``coverage`` annotation. Version 1 files still load: their
    # questions default to best_match, which is what every route they could
    # express already meant.
    format_version: int = 2
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
    predicted_coverage: str = "best_match"
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
