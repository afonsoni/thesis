"""
Pydantic models for the evaluation stage: gold-set questions, per-question run
records, and aggregated per-variant results.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

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
    # Gold key -> "party > header path" of the manifesto section it sits in.
    # Each distinct section is one aspect of the answer, so a broad question can
    # be scored on how many aspects it reached, not only how many chunks.
    gold_aspects: Dict[str, str] = Field(default_factory=dict)
    reference_answer: str = ""
    # False when the manifestos do not answer the question (topic never raised,
    # false premise, party not in the corpus). Such a question has no gold
    # chunks, and the only right answer is to say so: it is scored on
    # abstention, not on faithfulness or correctness.
    answerable: bool = True
    source_party: str = ""
    source_section: str = ""
    curated: bool = False  # True once a human has validated this question
    # "dev" questions may be looked at while tuning; "test" ones are held out
    # for headline numbers, so the reported scores are not tuned to them.
    split: str = ""  # dev | test | "" (unsplit)

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

    def with_split(self, split: str) -> "EvalDataset":
        return EvalDataset(
            format_version=self.format_version,
            created_at=self.created_at,
            questions=[q for q in self.questions if q.split == split],
        )

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
    # Every LLM call this question made, in order: {"step", "model",
    # "prompt_tokens", "completion_tokens", "cost", "secs"}, the model being the one that
    # answered, so a fallback is visible per question and per step (pipeline and
    # judge alike). Runs before token accounting carry only step and model.
    llm_calls: List[Dict[str, Any]] = Field(default_factory=list)

    metrics: Dict[str, float] = Field(default_factory=dict)
    # Per-metric working: extracted claims and the judge's verdict on each, so a
    # score can be audited and a sample can be rated by hand against it.
    judgements: Dict[str, Any] = Field(default_factory=dict)


class VariantResult(BaseModel):
    """Aggregated evaluation results for one variant over the whole dataset."""

    variant: str
    config: Dict = Field(default_factory=dict)
    created_at: str = ""
    dataset_size: int = 0
    aggregate: Dict[str, float] = Field(default_factory=dict)
    per_question: List[QuestionRun] = Field(default_factory=list)
    # LLM calls per answering model during this run (generation, analysis and
    # judge alike); more than one entry means OpenRouter fallbacks were used.
    models_used: Dict[str, int] = Field(default_factory=dict)
    # Which questions were scored, so a result can be tied to its gold set and
    # a dev-split number cannot pass for a held-out one.
    dataset_path: str = ""
    split: str = ""  # dev | test | "" (all)
    curated_only: bool = False
