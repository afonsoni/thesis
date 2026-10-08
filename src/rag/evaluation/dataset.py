"""
Load and save the gold set.

The gold set is hand-written (``data/eval/questions/CANDIDATES.md``) and anchored
to indexed chunks by ``scripts/anchor_gold.py``; this module only does the I/O.
"""

from __future__ import annotations

import json
import logging
import os

from src.rag.evaluation.models import EvalDataset

logger = logging.getLogger(__name__)


def save_dataset(dataset: EvalDataset, path: str) -> str:
    out_dir = os.path.dirname(path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(dataset.model_dump(), fh, ensure_ascii=False, indent=2)
    logger.info("Saved %d questions to %s", len(dataset.questions), path)
    return path


def load_dataset(path: str) -> EvalDataset:
    with open(path, "r", encoding="utf-8") as fh:
        return EvalDataset.model_validate(json.load(fh))
