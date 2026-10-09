"""
Uncertainty for leaderboard numbers: percentile bootstrap over questions.

A mean over ~30 questions moves by several points when one question flips, so a
difference between two rungs is only reported as real when its paired bootstrap
interval excludes zero. Pairing (resampling the same questions for both arms)
removes the between-question variance that both arms share, which is what makes
rung-to-rung differences on one gold set detectable at all.
"""

from __future__ import annotations

from typing import Dict, Optional, Sequence, Tuple

import numpy as np

from src.rag.evaluation.models import VariantResult

Interval = Tuple[float, float]


def bootstrap_ci(values: Sequence[float], n: int = 2000, alpha: float = 0.05, seed: int = 0) -> Optional[Interval]:
    """Percentile bootstrap CI of the mean; ``None`` for fewer than two values."""
    x = np.asarray(values, dtype=float)
    if x.size < 2:
        return None
    rng = np.random.default_rng(seed)
    means = x[rng.integers(0, x.size, size=(n, x.size))].mean(axis=1)
    lo, hi = np.quantile(means, [alpha / 2, 1 - alpha / 2])
    return float(lo), float(hi)


def paired_diff(a: Dict[str, float], b: Dict[str, float], n: int = 2000, alpha: float = 0.05,
                seed: int = 0) -> Optional[Tuple[float, Interval, int]]:
    """Mean of (b - a) over questions scored in both, with its bootstrap CI and n."""
    shared = sorted(set(a) & set(b))
    if len(shared) < 2:
        return None
    d = np.array([b[q] - a[q] for q in shared])
    ci = bootstrap_ci(d, n=n, alpha=alpha, seed=seed)
    return float(d.mean()), ci, len(shared)


def per_question(result: VariantResult, metric: str) -> Dict[str, float]:
    return {r.question_id: r.metrics[metric] for r in result.per_question if metric in r.metrics}
