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
from src.rag.evaluation.metrics import (
    GenerationJudgeMetric,
    RetrievalMetric,
    RoutingMetric,
)
from src.rag.evaluation.metrics.base import Metric
from src.rag.evaluation.models import VariantResult
from src.rag.evaluation.report import save_result, write_leaderboard
from src.rag.evaluation.runner import run_variant
from src.rag.evaluation.variants import DEFAULT_VARIANTS, resolve_variants
from src.utils.config_loader import config

logger = logging.getLogger(__name__)


def _build_metrics(k: int, use_judge: bool, judge_model: Optional[str]) -> List[Metric]:
    metrics: List[Metric] = [RetrievalMetric(k=k), RoutingMetric()]
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
        k: Cut-off for retrieval metrics and judge context.
        use_judge: Whether to run the (LLM) generation-judge metrics.
        judge_model: Override judge model id.
        results_dir / reports_dir: Output locations.

    Returns:
        One ``VariantResult`` per variant.
    """
    variant_names = variant_names or list(config.get("evaluation.variants", DEFAULT_VARIANTS))
    dataset_path = dataset_path or str(
        config.get("evaluation.dataset_path", "data/eval/questions/golden.json")
    )
    results_dir = results_dir or str(config.get("evaluation.results_dir", "data/eval/results"))
    reports_dir = reports_dir or str(config.get("evaluation.reports_dir", "data/eval/reports"))
    k = int(k or config.get("evaluation.top_k", config.get("retrieval.default_top_k", 5)))

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

    configs = resolve_variants(variant_names)
    metrics = _build_metrics(k, use_judge, judge_model)

    logger.info(
        "Evaluating variants %s over %d questions (k=%d, judge=%s).",
        variant_names, len(dataset.questions), k, use_judge,
    )

    results: List[VariantResult] = []
    for cfg in configs:
        before = Counter(MODEL_USAGE)
        result = run_variant(cfg, dataset, metrics, k=k)
        result.models_used = dict(MODEL_USAGE - before)
        save_result(result, results_dir)
        results.append(result)

    write_leaderboard(results, reports_dir)
    return results
