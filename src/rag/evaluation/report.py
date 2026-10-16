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
from typing import Dict, List, Optional, Set

from src.rag.evaluation.models import VariantResult
from src.utils.config_loader import config
from src.rag.evaluation.stats import bootstrap_ci, paired_diff, per_question

logger = logging.getLogger(__name__)

# Preferred left-to-right ordering for metric columns; unknown keys go last (sorted).
_COLUMN_PRIORITY = [
    "hit", "recall", "aspect_recall", "mrr", "ndcg",
    "query_type_acc", "coverage_acc", "party_f1", "topic_f1",
    "faithfulness", "correctness", "correctness_recall", "answer_relevance",
    "abstention", "false_refusal",
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


def _shared_scores(results: List[VariantResult], metric: str) -> Dict[str, Dict[str, float]]:
    """Per variant, *metric*'s scores on the questions every variant scored.

    A question that errored or went unjudged in one arm drops out of all of
    them, so each row of the table is a mean over the same questions. Variants
    that never produce *metric* (e.g. no judge) do not shrink the set.
    """
    scored = {r.variant: per_question(r, metric) for r in results}
    having = [qs for qs in scored.values() if qs]
    shared = set.intersection(*(set(qs) for qs in having)) if having else set()
    return {v: {q: qs[q] for q in shared} for v, qs in scored.items() if qs}


def _table(results: List[VariantResult], columns: List[str]) -> Dict[str, Dict[str, tuple]]:
    """{variant: {column: (value, ci)}}: shared-question means, run stats as recorded."""
    cells: Dict[str, Dict[str, tuple]] = {r.variant: {} for r in results}
    for col in columns:
        if col in _RUN_STATS:
            for r in results:
                if col in r.aggregate:
                    cells[r.variant][col] = (r.aggregate[col], None)
            continue
        for variant, qs in _shared_scores(results, col).items():
            if qs:
                values = list(qs.values())
                cells[variant][col] = (round(sum(values) / len(values), 4), bootstrap_ci(values))
    return cells


def _table_lines(results: List[VariantResult], columns: List[str]) -> List[str]:
    table = _table(results, columns)
    lines = ["| variant | " + " | ".join(columns) + " |", "| --- | " + " | ".join("---" for _ in columns) + " |"]
    for r in results:
        cells = [_format_cell(*table[r.variant].get(col, (float("nan"), None))) for col in columns]
        lines.append(f"| {r.variant} | " + " | ".join(cells) + " |")
    return lines


def _broad_section(results: List[VariantResult], columns: List[str], broad_ids: Set[str]) -> List[str]:
    """The same table over the broad questions only (run stats left out: they are whole-run)."""
    sub = [r.model_copy(update={"per_question": [q for q in r.per_question if q.question_id in broad_ids]})
           for r in results]
    n = len({q.question_id for r in sub for q in r.per_question})
    if not n:
        return []
    metrics = [c for c in columns if c not in _RUN_STATS]
    lines = [
        "## Broad questions",
        "",
        f"The {n} questions with more gold chunks than a flat retrieval returns at the",
        "production depth, so plain `recall` cannot reach 1 on them. Read `recall_capped`,",
        "`aspect_recall` and `correctness_grounded` here: the reference answers are",
        "aspect-level, which makes `correctness` precision count true detail as error.",
        "",
        *_table_lines(sub, metrics),
        "",
    ]
    if len(sub) > 1:
        delta = _delta_table(sub, metrics)
        lines.extend(["#" + delta[0], *delta[1:]])  # a subsection of this one
    return lines


def _leaderboard_stem(results: List[VariantResult]) -> str:
    """``leaderboard``, suffixed by split and curation so a dev run cannot
    overwrite the held-out table."""
    first = results[0] if results else VariantResult(variant="")
    return "leaderboard" + (f"-{first.split}" if first.split else "") + ("-curated" if first.curated_only else "")


def _format_cell(value: float, ci=None) -> str:
    if isinstance(value, float) and value != value:  # nan: the variant never produced this metric
        return ""
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


def write_leaderboard(results: List[VariantResult], reports_dir: str,
                      broad_ids: Optional[Set[str]] = None) -> str:
    """(Over)write leaderboard[-split][-curated].md + .csv comparing the given variants.

    *broad_ids* adds a second table restricted to those questions.
    """
    os.makedirs(reports_dir, exist_ok=True)
    columns = _ordered_columns(results)
    table = _table(results, columns)
    stem = _leaderboard_stem(results)
    md_path = os.path.join(reports_dir, f"{stem}.md")
    csv_path = os.path.join(reports_dir, f"{stem}.csv")
    first = results[0] if results else VariantResult(variant="")

    # Markdown
    lines = [
        "# RAG Evaluation Leaderboard",
        "",
        f"_Generated: {datetime.now().isoformat(timespec='seconds')}_  ",
        f"_Dataset: `{first.dataset_path or '?'}`, split `{first.split or 'all'}`, "
        f"{'curated only' if first.curated_only else 'curated and uncurated'}, "
        f"{first.dataset_size} questions_  ",
        f"_Code: `{', '.join(sorted({r.code_version or '?' for r in results}))}`_",
        "",
        *_table_lines(results, columns),
    ]
    lines.extend([
        "",
        "Higher is better for all metrics except `false_refusal`, `avg_latency_s` and `error_rate`.",
        "Cells are means over the questions every variant scored on that metric, with a",
        "95% bootstrap interval over questions; `error_rate` counts the rest.",
        "Retrieval metrics score the full list handed to generation: `top_k` chunks, or",
        "`top_k_per_party` per party on a per-party fan-out. `recall_capped` divides by",
        "min(gold, slots) instead of gold; `aspect_recall` is the share of the gold",
        "set's manifesto sections with a gold chunk retrieved.",
        "`faithfulness` and `correctness*` are claim-level (RAGAS-style);",
        "`correctness_grounded` is the F1 of `faithfulness` and `correctness_recall`;",
        "`answer_relevance` is a 1-5 judgement mapped to [0, 1].",
        "`abstention` is the share of unanswerable questions the system declined;",
        "`false_refusal` the share of answerable ones it declined.",
        "",
    ])
    # A model outside the ones this run was configured with answered a call,
    # i.e. the transport fell back. The judge and a variant's own generator
    # are expected, not fallbacks.
    expected = {str(config.get("llm.openrouter.model")), str(config.get("evaluation.judge_model"))}
    used = {
        r.variant: {m: n for m, n in r.models_used.items()
                    if m not in expected | {str(r.config.get("generation_model") or "")}}
        for r in results
    }
    used = {v: c for v, c in used.items() if c}
    if used:
        lines.append("**Fallback models answered some LLM calls** (calls per model): " + "; ".join(
            f"`{v}`: " + ", ".join(f"{m} {n}" for m, n in sorted(c.items(), key=lambda kv: -kv[1]))
            for v, c in used.items()))
        lines.append("")
    if len(results) > 1:
        lines.extend(_delta_table(results, columns))
    if broad_ids:
        lines.extend(_broad_section(results, columns, broad_ids))
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    # CSV
    with open(csv_path, "w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["variant", *columns])
        for r in results:
            writer.writerow([r.variant, *[table[r.variant].get(col, ("",))[0] for col in columns]])

    logger.info("Wrote leaderboard → %s", md_path)
    return md_path
