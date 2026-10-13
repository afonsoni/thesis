"""
Evaluation orchestrator – the single entry point for the evaluation stage.

``evaluate(...)`` resolves the requested variants, runs each over the gold set,
persists per-variant results, and refreshes the comparison leaderboard.
"""

from __future__ import annotations

import logging
from collections import Counter
from typing import List, Optional

from src.rag.common.llm_transport import MODEL_USAGE
from src.rag.evaluation.dataset import load_dataset
from src.rag.evaluation.metrics.generation import GenerationJudgeMetric
from src.rag.evaluation.metrics.retrieval import RetrievalMetric
from src.rag.evaluation.metrics.routing import RoutingMetric
from src.rag.evaluation.models import VariantResult
from src.rag.evaluation.report import save_result, write_leaderboard
from src.rag.evaluation.runner import Metric, run_variant
from src.rag.evaluation.variants import resolve_variants
from src.utils.config_loader import config

logger = logging.getLogger(__name__)


def _build_metrics(use_judge: bool, judge_model: Optional[str]) -> List[Metric]:
    metrics: List[Metric] = [RetrievalMetric(), RoutingMetric()]
    if use_judge:
        metrics.append(GenerationJudgeMetric(model=judge_model))
    return metrics


def evaluate(
    variant_names: Optional[List[str]] = None,
    dataset_path: Optional[str] = None,
    curated_only: bool = False,
    split: Optional[str] = None,
    k: Optional[int] = None,
    use_judge: bool = True,
    judge_model: Optional[str] = None,
    results_dir: Optional[str] = None,
    reports_dir: Optional[str] = None,
) -> List[VariantResult]:
    """
    Run the evaluation harness.

    Args:
        variant_names: Variant preset names (see ``variants.VARIANTS``).
        dataset_path: Gold set JSON path.
        curated_only: Restrict to human-validated questions.
        split: Restrict to one split (``dev`` while tuning, ``test`` for headline numbers).
        k: Chunks retrieved on a flat route (``RetrievalConfig.top_k``), forced on
            every variant; None keeps each variant's own. A per-party fan-out
            keeps ``top_k_per_party``.
        use_judge: Whether to run the (LLM) generation-judge metrics.
        judge_model: Override judge model id.
        results_dir / reports_dir: Output locations.

    Returns:
        One ``VariantResult`` per variant.
    """
    variant_names = variant_names or list(config.get("evaluation.variants"))
    dataset_path = dataset_path or str(
        config.get("evaluation.dataset_path")
    )
    results_dir = results_dir or str(config.get("evaluation.results_dir"))
    reports_dir = reports_dir or str(config.get("evaluation.reports_dir"))

    dataset = load_dataset(dataset_path)
    if curated_only:
        dataset = dataset.curated_only()
    if split:
        dataset = dataset.with_split(split)
    if not dataset.questions:
        raise ValueError(
            f"No questions to evaluate in {dataset_path}"
            f" (curated_only={curated_only}, split={split!r})"
        )

    # -k overrides every variant's top_k; without it each keeps its own (a variant
    # may retrieve more on purpose, e.g. `wide`).
    configs = [c.model_copy(update={"top_k": k}) if k else c for c in resolve_variants(variant_names)]
    metrics = _build_metrics(use_judge, judge_model)
    wait_out_attempts = int(config.get("evaluation.wait_out_attempts"))

    logger.info(
        "Evaluating variants %s over %d questions (k=%s, judge=%s).",
        variant_names, len(dataset.questions), k or "per variant", use_judge,
    )

    results: List[VariantResult] = []
    for cfg in configs:
        before = Counter(MODEL_USAGE)
        result = run_variant(cfg, dataset, metrics, k=cfg.top_k, generate=use_judge,
                             wait_out_attempts=wait_out_attempts)
        result.models_used = dict(MODEL_USAGE - before)
        calls = [c for run in result.per_question for c in run.llm_calls]
        logger.info(
            "[%s] %d LLM calls, %d tokens in / %d out, $%.4f.", cfg.name, len(calls),
            sum(c["prompt_tokens"] for c in calls), sum(c["completion_tokens"] for c in calls),
            sum(c["cost"] for c in calls),
        )
        result.dataset_path = dataset_path
        result.split = split or ""
        result.curated_only = curated_only
        save_result(result, results_dir)
        results.append(result)

    write_leaderboard(results, reports_dir)
    return results
