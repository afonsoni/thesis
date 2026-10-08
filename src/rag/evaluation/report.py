"""
Persist evaluation results to the repo.

- One timestamped JSON per variant under ``results_dir`` (full run history,
  including per-question records).
- A refreshed ``leaderboard.md`` + ``leaderboard.csv`` under ``reports_dir``
  comparing all variants from the latest run — the living, committed comparison
  the dissertation can cite.
"""

from __future__ import annotations

import csv
import json
import logging
import os
from datetime import datetime
from typing import Dict, List

from src.rag.evaluation.models import VariantResult
from src.rag.evaluation.stats import metric_cis, paired_diff, per_question

logger = logging.getLogger(__name__)

# Preferred left-to-right ordering for metric columns; unknown keys go last (sorted).
_COLUMN_PRIORITY = [
    "hit@", "recall@", "mrr", "ndcg@",
    "query_type_acc", "coverage_acc", "party_f1", "topic_f1",
    "faithfulness", "correctness", "correctness_recall", "answer_relevance",
    "avg_latency_s", "error_rate",
]


def _priority(key: str) -> tuple:
    for i, prefix in enumerate(_COLUMN_PRIORITY):
        if key == prefix or key.startswith(prefix):
            return (i, key)
    return (len(_COLUMN_PRIORITY), key)


def _ordered_columns(results: List[VariantResult]) -> List[str]:
    keys = set()
    for r in results:
        keys.update(r.aggregate.keys())
    return sorted(keys, key=_priority)


def _safe_ts(iso_ts: str) -> str:
    return (iso_ts or datetime.now().isoformat(timespec="seconds")).replace(":", "").replace("-", "")


def save_result(result: VariantResult, results_dir: str) -> str:
    """Write one variant's full result (with per-question records) to JSON."""
    os.makedirs(results_dir, exist_ok=True)
    path = os.path.join(results_dir, f"{result.variant}-{_safe_ts(result.created_at)}.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(result.model_dump(), fh, ensure_ascii=False, indent=2)
    logger.info("Saved result for '%s' → %s", result.variant, path)
    return path


_RUN_STATS = {"avg_latency_s", "error_rate"}  # not per-question scores: no interval


def _format_cell(value: float, ci=None) -> str:
    cell = f"{value:.3f}" if isinstance(value, float) else str(value)
    return f"{cell} [{ci[0]:.2f}, {ci[1]:.2f}]" if ci else cell


def _delta_table(results: List[VariantResult], columns: List[str]) -> List[str]:
    """Paired differences of every variant against the first one, with 95% CIs."""
    base = results[0]
    metrics = [c for c in columns if c not in _RUN_STATS]
    lines = [
        f"## Paired difference vs `{base.variant}`",
        "",
        "Mean of (variant − baseline) over the questions both scored, with a 95% paired",
        "bootstrap interval. **Bold** = the interval excludes 0.",
        "",
        "| variant | " + " | ".join(metrics) + " |",
        "| --- | " + " | ".join("---" for _ in metrics) + " |",
    ]
    for r in results[1:]:
        cells = []
        for m in metrics:
            d = paired_diff(per_question(base, m), per_question(r, m))
            if d is None or d[1] is None:
                cells.append("")
                continue
            mean, (lo, hi), _n = d
            cell = f"{mean:+.3f} [{lo:+.2f}, {hi:+.2f}]"
            cells.append(f"**{cell}**" if lo > 0 or hi < 0 else cell)
        lines.append(f"| {r.variant} | " + " | ".join(cells) + " |")
    return lines + [""]


def write_leaderboard(results: List[VariantResult], reports_dir: str) -> str:
    """(Over)write leaderboard.md + leaderboard.csv comparing the given variants."""
    os.makedirs(reports_dir, exist_ok=True)
    columns = _ordered_columns(results)
    md_path = os.path.join(reports_dir, "leaderboard.md")
    csv_path = os.path.join(reports_dir, "leaderboard.csv")

    # Markdown
    header = "| variant | " + " | ".join(columns) + " |"
    sep = "| --- | " + " | ".join("---" for _ in columns) + " |"
    lines = [
        "# RAG Evaluation Leaderboard",
        "",
        f"_Generated: {datetime.now().isoformat(timespec='seconds')}_  ",
        f"_Dataset size: {results[0].dataset_size if results else 0} questions_",
        "",
        header,
        sep,
    ]
    for r in results:
        cis = metric_cis(r, [c for c in columns if c not in _RUN_STATS])
        cells = [_format_cell(r.aggregate.get(col, float("nan")), cis.get(col)) for col in columns]
        lines.append(f"| {r.variant} | " + " | ".join(cells) + " |")
    lines.extend([
        "",
        "Higher is better for all metrics except `avg_latency_s` and `error_rate`.",
        "Cells are means over the questions scored, with a 95% bootstrap interval over",
        "questions. `faithfulness` and `correctness*` are claim-level (RAGAS-style);",
        "`answer_relevance` is a 1-5 judgement mapped to [0, 1].",
        "",
    ])
    used = {r.variant: r.models_used for r in results if len(r.models_used) > 1}
    if used:
        lines.append("**Fallback models answered some LLM calls** (calls per model): " + "; ".join(
            f"`{v}`: " + ", ".join(f"{m} {n}" for m, n in sorted(c.items(), key=lambda kv: -kv[1]))
            for v, c in used.items()))
        lines.append("")
    if len(results) > 1:
        lines.extend(_delta_table(results, columns))
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    # CSV
    with open(csv_path, "w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["variant", *columns])
        for r in results:
            writer.writerow([r.variant, *[r.aggregate.get(col, "") for col in columns]])

    logger.info("Wrote leaderboard → %s", md_path)
    return md_path


def summarize(results: List[VariantResult]) -> Dict[str, Dict[str, float]]:
    """Return {variant: aggregate} for quick programmatic inspection."""
    return {r.variant: r.aggregate for r in results}
