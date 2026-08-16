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

logger = logging.getLogger(__name__)

# Preferred left-to-right ordering for metric columns; unknown keys go last (sorted).
_COLUMN_PRIORITY = [
    "hit@", "recall@", "mrr", "ndcg@",
    "query_type_acc", "coverage_acc", "party_f1", "topic_f1",
    "faithfulness", "answer_relevance", "correctness",
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


def _format_cell(value: float) -> str:
    return f"{value:.3f}" if isinstance(value, float) else str(value)


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
        cells = [_format_cell(r.aggregate.get(col, float("nan"))) for col in columns]
        lines.append(f"| {r.variant} | " + " | ".join(cells) + " |")
    lines.extend([
        "",
        "Higher is better for all metrics except `avg_latency_s` and `error_rate`.",
        "Scores are means over the dataset; generation metrics are LLM-judge scores mapped to [0, 1].",
        "",
    ])
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
