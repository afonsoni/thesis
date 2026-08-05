"""
LLM-as-judge scoring, reusing the project's OpenRouter transport
(``generate_structured``) so the judge inherits the same retry/backoff/config.

Each judgement returns a 1–5 integer score with a short rationale. The judge
model defaults to a model *distinct* from the generation model (config
``evaluation.judge_model``) to reduce self-preference bias.
"""

from __future__ import annotations

import logging
from typing import Optional

from pydantic import BaseModel, Field

from src.rag.common.llm_client import generate_structured
from src.rag.evaluation.prompts import (
    JUDGE_CORRECTNESS_PROMPT,
    JUDGE_FAITHFULNESS_PROMPT,
    JUDGE_RELEVANCE_PROMPT,
    JUDGE_SYSTEM_PROMPT,
)
from src.utils.config_loader import config

logger = logging.getLogger(__name__)


class JudgeScore(BaseModel):
    score: int = Field(ge=1, le=5)
    rationale: str = ""

    @property
    def normalized(self) -> float:
        """Score mapped to [0, 1] for averaging across metrics."""
        return (self.score - 1) / 4.0


def _judge_model(model: Optional[str]) -> str:
    return str(
        model
        or config.get(
            "evaluation.judge_model",
            config.get("llm.openrouter.model", "meta-llama/llama-3.3-70b-instruct"),
        )
    )


def _judge_temperature() -> float:
    return float(config.get("evaluation.judge_temperature", 0.0))


def _judge(prompt: str, model: Optional[str]) -> Optional[JudgeScore]:
    """Run one judgement; return None (not fail-fast) if the judge call errors."""
    try:
        raw = generate_structured(
            prompt=prompt,
            response_schema=JudgeScore,
            system_prompt=JUDGE_SYSTEM_PROMPT,
            model=_judge_model(model),
            temperature=_judge_temperature(),
            max_tokens=400,
        )
        score = max(1, min(5, int(raw.score)))
        return JudgeScore(score=score, rationale=(raw.rationale or "")[:500])
    except Exception as exc:  # noqa: BLE001 - judge failures degrade gracefully
        logger.warning("Judge call failed: %s", exc)
        return None


def judge_faithfulness(
    question: str, answer: str, context: str, model: Optional[str] = None
) -> Optional[JudgeScore]:
    """Is the answer grounded in the retrieved context (reference-free)?"""
    return _judge(
        JUDGE_FAITHFULNESS_PROMPT.format(question=question, answer=answer, context=context),
        model,
    )


def judge_answer_relevance(
    question: str, answer: str, model: Optional[str] = None
) -> Optional[JudgeScore]:
    """Does the answer address the question (reference-free)?"""
    return _judge(
        JUDGE_RELEVANCE_PROMPT.format(question=question, answer=answer),
        model,
    )


def judge_correctness(
    question: str, answer: str, reference: str, model: Optional[str] = None
) -> Optional[JudgeScore]:
    """Does the answer agree with the reference answer (reference-based)?"""
    return _judge(
        JUDGE_CORRECTNESS_PROMPT.format(question=question, answer=answer, reference=reference),
        model,
    )
