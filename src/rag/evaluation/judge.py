"""
LLM-as-judge calls, on the project's transport (``generate_structured``).

Two kinds:

- **Claim-level** (faithfulness, correctness), following RAGAS (Es et al., EACL
  2024): :func:`extract_claims` splits a text into atomic claims and
  :func:`verify_claims` checks each one against an evidence text. Scores are the
  share of claims supported, computed by the metric, not by the model.
- **Holistic** (answer relevance): a single 1-5 judgement with a rationale.

Every call waits out free-tier failures (``call_with_wait_out``) and then
returns ``None`` instead of raising, so the metric omits the score rather than
recording a zero for an API outage.
"""

from __future__ import annotations

import logging
from typing import Any, Callable, List, Optional

from pydantic import BaseModel, Field

from src.rag.common.llm_client import call_with_wait_out, generate_structured
from src.rag.evaluation.prompts import (
    CLAIMS_EXTRACTION_PROMPT,
    CLAIMS_SYSTEM_PROMPT,
    CLAIMS_VERIFICATION_PROMPT,
    JUDGE_RELEVANCE_PROMPT,
    JUDGE_SYSTEM_PROMPT,
)
from src.utils.config_loader import config

logger = logging.getLogger(__name__)


class JudgeScore(BaseModel):
    score: int = Field(ge=1, le=5)
    rationale: str = ""
    # Whether the answer declines (says the manifestos do not say, or rejects the
    # question's premise) instead of answering. Read off the relevance call so
    # abstention costs no extra judge call.
    abstained: bool = False

    @property
    def normalized(self) -> float:
        """Score mapped to [0, 1] for averaging across metrics."""
        return (self.score - 1) / 4.0


class _Claims(BaseModel):
    claims: List[str] = Field(default_factory=list)


class ClaimVerdict(BaseModel):
    index: int = 0
    supported: bool = False
    reason: str = ""


class _Verdicts(BaseModel):
    verdicts: List[ClaimVerdict] = Field(default_factory=list)


def _judge_model(model: Optional[str]) -> str:
    return str(model or config.get("evaluation.judge_model"))


def _call(prompt: str, schema: type, system: str, model: Optional[str], label: str, max_tokens: int,
          check: Optional[Callable[[Any], Any]] = None):
    """One structured judge call with wait-out; ``None`` once attempts run out.

    *check* validates/transforms the reply inside the retried call, so a reply
    it rejects (by raising) is retried like a transport failure.
    """
    def attempt():
        out = generate_structured(
            prompt=prompt,
            response_schema=schema,
            system_prompt=system,
            model=_judge_model(model),
            temperature=float(config.get("evaluation.judge_temperature")),
            max_tokens=max_tokens,
            label=f"judge: {label}",
        )
        return check(out) if check else out

    try:
        return call_with_wait_out(
            attempt, label=label, attempts=int(config.get("evaluation.wait_out_attempts")),
        )
    except Exception as exc:  # noqa: BLE001 - judge failures are omitted, not fatal
        logger.warning("%s failed: %s", label, exc)
        return None


def extract_claims(question: str, text: str, model: Optional[str] = None) -> Optional[List[str]]:
    """Atomic, self-contained claims made by *text* (an answer or a reference)."""
    out = _call(
        CLAIMS_EXTRACTION_PROMPT.format(question=question, text=text),
        _Claims, CLAIMS_SYSTEM_PROMPT, model, "claim extraction", 4000,
    )
    if out is None:
        return None
    return [c.strip() for c in out.claims if c and c.strip()]


def verify_claims(
    claims: List[str], evidence: str, model: Optional[str] = None
) -> Optional[List[ClaimVerdict]]:
    """One verdict per claim, in order: is it supported by *evidence*?

    A reply with the wrong number of verdicts is retried like any other failure,
    since scoring a misaligned list would attribute verdicts to the wrong claims.
    """
    if not claims:
        return []
    numbered = "\n".join(f"{i}. {c}" for i, c in enumerate(claims, 1))
    prompt = CLAIMS_VERIFICATION_PROMPT.format(evidence=evidence, claims=numbered)

    def aligned(out: _Verdicts) -> List[ClaimVerdict]:
        if len(out.verdicts) != len(claims):
            raise ValueError(f"expected {len(claims)} verdicts, got {len(out.verdicts)}")
        return sorted(out.verdicts, key=lambda v: v.index) if all(v.index for v in out.verdicts) else out.verdicts

    return _call(prompt, _Verdicts, CLAIMS_SYSTEM_PROMPT, model, "claim verification",
                 200 + 200 * len(claims), check=aligned)


def judge_answer_relevance(
    question: str, answer: str, model: Optional[str] = None
) -> Optional[JudgeScore]:
    """Does the answer address the question (reference-free, 1-5)?"""
    out = _call(
        JUDGE_RELEVANCE_PROMPT.format(question=question, answer=answer),
        JudgeScore, JUDGE_SYSTEM_PROMPT, model, "relevance judge", 400,
    )
    if out is None:
        return None
    return JudgeScore(
        score=max(1, min(5, int(out.score))),
        rationale=(out.rationale or "")[:500],
        abstained=bool(out.abstained),
    )
