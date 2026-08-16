"""
Synthetic-anchored + curated gold-set construction.

A strong LLM generates questions *anchored to sampled indexed chunks*, so the
source chunk(s) become the ground-truth relevant context automatically (via a
stable content key — see ``keys.py``). The construction method itself fixes the
expected ``query_type`` / parties / topics, giving reliable routing ground truth.

Questions start with ``curated=False``; you hand-validate a subset into a
``golden.json`` (setting ``curated=True``) for headline numbers.
"""

from __future__ import annotations

import json
import logging
import os
from collections import defaultdict
from datetime import datetime
from typing import TYPE_CHECKING, Dict, List, Optional

from pydantic import BaseModel

from src.rag.common.llm_client import generate_structured
from src.rag.common.models import SearchResult, VALID_TOPICS
from src.rag.evaluation.keys import chunk_key
from src.rag.evaluation.models import EvalDataset, EvalQuestion
from src.rag.evaluation.prompts import (
    GEN_COMPARISON_PROMPT,
    GEN_GENERAL_PROMPT,
    GEN_SINGLE_PROMPT,
    GEN_TOPIC_PROMPT,
)
from src.utils.config_loader import config

if TYPE_CHECKING:  # avoid importing psycopg2 just to load/save a dataset
    from src.rag.indexing.store import VectorStore

logger = logging.getLogger(__name__)

DEFAULT_TYPES = ["single_party", "comparison", "topic_exploration", "general"]
_MAX_CONTENT_CHARS = 1500


class _GenQA(BaseModel):
    question: str
    reference_answer: str = ""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _section(chunk: SearchResult) -> str:
    return chunk.section_path


def _clip(text: str) -> str:
    return text[:_MAX_CONTENT_CHARS]


def _gen_model(model: Optional[str]) -> str:
    return str(model or config.get("llm.openrouter.model", "meta-llama/llama-3.3-70b-instruct"))


def _llm_qa(prompt: str, model: str) -> Optional[_GenQA]:
    """Generate one {question, reference_answer}; skip (return None) on failure."""
    try:
        qa = generate_structured(
            prompt=prompt, response_schema=_GenQA, model=model,
            temperature=0.4, max_tokens=500,
        )
        if not qa.question.strip():
            return None
        return qa
    except Exception as exc:  # noqa: BLE001 - dataset gen is best-effort, not fail-fast
        logger.warning("Question generation failed: %s", exc)
        return None


def _topic_groups(store: VectorStore, topic: str, max_chunks: int = 8) -> Dict[str, List[SearchResult]]:
    """Sample chunks tagged with *topic* and group them by party."""
    chunks = store.sample_chunks(n=max_chunks, topic=topic)
    grouped: Dict[str, List[SearchResult]] = defaultdict(list)
    for c in chunks:
        grouped[c.party_name].append(c)
    return grouped


def _allocate(total: int, types: List[str]) -> Dict[str, int]:
    """Split *total* questions roughly evenly across *types*."""
    if not types:
        return {}
    base, extra = divmod(total, len(types))
    return {t: base + (1 if i < extra else 0) for i, t in enumerate(types)}


# ---------------------------------------------------------------------------
# Per-type generation
# ---------------------------------------------------------------------------

def _gen_single(store: VectorStore, count: int, model: str, start_id: int) -> List[EvalQuestion]:
    out: List[EvalQuestion] = []
    chunks = store.sample_chunks(n=count * 2)  # oversample to absorb LLM failures
    for chunk in chunks:
        if len(out) >= count:
            break
        qa = _llm_qa(GEN_SINGLE_PROMPT.format(party=chunk.party_name, content=_clip(chunk.content)), model)
        if not qa:
            continue
        out.append(EvalQuestion(
            id=f"q-{start_id + len(out):04d}",
            question=qa.question.strip(),
            query_type="single_party",
            coverage="best_match",
            expected_parties=[chunk.party_name],
            expected_topics=chunk.topics[:3],
            gold_chunk_keys=[chunk_key(chunk.content)],
            reference_answer=qa.reference_answer.strip(),
            source_party=chunk.party_name,
            source_section=_section(chunk),
        ))
    return out


def _gen_general(store: VectorStore, count: int, model: str, start_id: int) -> List[EvalQuestion]:
    out: List[EvalQuestion] = []
    chunks = store.sample_chunks(n=count * 2)
    for chunk in chunks:
        if len(out) >= count:
            break
        qa = _llm_qa(GEN_GENERAL_PROMPT.format(content=_clip(chunk.content)), model)
        if not qa:
            continue
        out.append(EvalQuestion(
            id=f"q-{start_id + len(out):04d}",
            question=qa.question.strip(),
            query_type="general",
            coverage="best_match",
            gold_chunk_keys=[chunk_key(chunk.content)],
            reference_answer=qa.reference_answer.strip(),
            source_party=chunk.party_name,
            source_section=_section(chunk),
        ))
    return out


def _gen_topic(store: VectorStore, count: int, model: str, start_id: int) -> List[EvalQuestion]:
    out: List[EvalQuestion] = []
    topics = [t for t in VALID_TOPICS if t != "outros"]
    ti = 0
    attempts = 0
    while len(out) < count and attempts < count * 4:
        attempts += 1
        topic = topics[ti % len(topics)]
        ti += 1
        groups = _topic_groups(store, topic)
        chunks = [c for cs in groups.values() for c in cs]
        if len(chunks) < 2 or len(groups) < 2:
            continue
        chunks = chunks[:5]
        joined = "\n\n---\n\n".join(f"[{c.party_name}] {_clip(c.content)}" for c in chunks)
        qa = _llm_qa(GEN_TOPIC_PROMPT.format(topic=topic, content=joined), model)
        if not qa:
            continue
        out.append(EvalQuestion(
            id=f"q-{start_id + len(out):04d}",
            question=qa.question.strip(),
            query_type="topic_exploration",
            coverage="best_match",
            expected_topics=[topic],
            gold_chunk_keys=[chunk_key(c.content) for c in chunks],
            reference_answer=qa.reference_answer.strip(),
            source_section=topic,
        ))
    return out


def _gen_comparison(store: VectorStore, count: int, model: str, start_id: int) -> List[EvalQuestion]:
    out: List[EvalQuestion] = []
    topics = [t for t in VALID_TOPICS if t != "outros"]
    ti = 0
    attempts = 0
    while len(out) < count and attempts < count * 4:
        attempts += 1
        topic = topics[ti % len(topics)]
        ti += 1
        groups = _topic_groups(store, topic)
        parties = [p for p, cs in groups.items() if cs]
        if len(parties) < 2:
            continue
        pa, pb = parties[0], parties[1]
        ca, cb = groups[pa][0], groups[pb][0]
        qa = _llm_qa(
            GEN_COMPARISON_PROMPT.format(
                party_a=pa, party_b=pb, topic=topic,
                content_a=_clip(ca.content), content_b=_clip(cb.content),
            ),
            model,
        )
        if not qa:
            continue
        out.append(EvalQuestion(
            id=f"q-{start_id + len(out):04d}",
            question=qa.question.strip(),
            query_type="comparison",
            coverage="exhaustive",
            expected_parties=[pa, pb],
            expected_topics=[topic],
            gold_chunk_keys=[chunk_key(ca.content), chunk_key(cb.content)],
            reference_answer=qa.reference_answer.strip(),
            source_section=topic,
        ))
    return out


_GENERATORS = {
    "single_party": _gen_single,
    "comparison": _gen_comparison,
    "topic_exploration": _gen_topic,
    "general": _gen_general,
}


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def build_dataset(
    sample_size: int = 60,
    types: Optional[List[str]] = None,
    model: Optional[str] = None,
    store: Optional[VectorStore] = None,
) -> EvalDataset:
    """
    Build a synthetic gold set by sampling indexed chunks and generating
    anchored questions across the requested query types.
    """
    types = types or DEFAULT_TYPES
    model = _gen_model(model)
    allocation = _allocate(sample_size, types)

    owns_store = store is None
    if store is None:
        from src.rag.indexing.store import VectorStore
        store = VectorStore()
        store.connect()

    try:
        questions: List[EvalQuestion] = []
        for qtype, count in allocation.items():
            if count <= 0:
                continue
            gen = _GENERATORS.get(qtype)
            if gen is None:
                logger.warning("Unknown query type '%s' – skipping.", qtype)
                continue
            logger.info("Generating %d '%s' questions ...", count, qtype)
            questions.extend(gen(store, count, model, start_id=len(questions)))

        logger.info("Generated %d / %d requested questions.", len(questions), sample_size)
        return EvalDataset(
            created_at=datetime.now().isoformat(timespec="seconds"),
            questions=questions,
        )
    finally:
        if owns_store:
            store.close()


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
