"""
Run one variant over the gold set and score every question.

The heavy pipeline imports (``retrieve``/``generate``) are done lazily inside the
default callables so that pure-metric unit tests can import this module without
pulling in sentence-transformers / psycopg2. Tests can also inject
``retrieve_fn`` / ``generate_fn`` to run fully offline.
"""

from __future__ import annotations

import logging
import time
from datetime import datetime
from typing import Callable, Dict, List, Optional

from src.rag.common.models import RetrievalResult, SearchResult
from src.rag.evaluation.keys import chunk_key
from src.rag.evaluation.metrics.base import Metric
from src.rag.evaluation.models import EvalDataset, EvalQuestion, QuestionRun, VariantResult
from src.rag.retrieval.config import RetrievalConfig

logger = logging.getLogger(__name__)

RetrieveFn = Callable[[str, RetrievalConfig], RetrievalResult]
GenerateFn = Callable[[RetrievalResult], object]


def _default_retrieve(question: str, config: RetrievalConfig) -> RetrievalResult:
    from src.rag.retrieval.pipeline import retrieve
    return retrieve(question, config=config)


def _default_generate(result: RetrievalResult):
    from src.rag.generation.pipeline import generate
    return generate(result)


def _flatten_results(result: RetrievalResult) -> List[SearchResult]:
    """Prefer the flat list; fall back to flattening grouped comparison results."""
    if result.results:
        return result.results
    return [r for rs in result.results_by_party.values() for r in rs]


def _build_context(results: List[SearchResult], k: int) -> str:
    return "\n\n".join(f"[{r.party_name}] {r.content}" for r in results[:k])


def run_question(
    question: EvalQuestion,
    config: RetrievalConfig,
    metrics: List[Metric],
    k: int,
    retrieve_fn: RetrieveFn,
    generate_fn: GenerateFn,
) -> QuestionRun:
    """Run the pipeline on one question and apply all metrics."""
    run = QuestionRun(question_id=question.id, variant=config.name)
    start = time.perf_counter()
    try:
        result = retrieve_fn(question.question, config)
        results = _flatten_results(result)

        run.retrieved_keys = [chunk_key(r.content) for r in results]
        run.retrieved_parties = list(dict.fromkeys(r.party_name for r in results))
        run.predicted_query_type = result.query.query_type.value
        run.predicted_coverage = result.query.coverage.value
        run.predicted_parties = result.query.parties
        run.predicted_topics = result.query.topics
        run.context = _build_context(results, k)

        answer = generate_fn(result)
        run.answer = getattr(answer, "answer", "") or ""
    except Exception as exc:  # noqa: BLE001 - one bad question shouldn't kill the run
        run.error = str(exc)
        logger.warning("Question %s failed: %s", question.id, exc)
    finally:
        run.latency_s = round(time.perf_counter() - start, 3)

    if run.error is None:
        for metric in metrics:
            try:
                run.metrics.update(metric.score(run, question))
            except Exception as exc:  # noqa: BLE001
                logger.warning("Metric %s failed on %s: %s", getattr(metric, "name", metric), question.id, exc)

    return run


def _aggregate(runs: List[QuestionRun]) -> Dict[str, float]:
    """Mean of each metric across questions where it was produced, plus run stats."""
    sums: Dict[str, float] = {}
    counts: Dict[str, int] = {}
    for run in runs:
        for key, value in run.metrics.items():
            sums[key] = sums.get(key, 0.0) + value
            counts[key] = counts.get(key, 0) + 1

    aggregate = {key: round(sums[key] / counts[key], 4) for key in sums}
    n_errors = sum(1 for r in runs if r.error is not None)
    latencies = [r.latency_s for r in runs if r.error is None]
    aggregate["avg_latency_s"] = round(sum(latencies) / len(latencies), 3) if latencies else 0.0
    aggregate["error_rate"] = round(n_errors / len(runs), 4) if runs else 0.0
    return aggregate


def run_variant(
    config: RetrievalConfig,
    dataset: EvalDataset,
    metrics: List[Metric],
    k: int = 5,
    retrieve_fn: Optional[RetrieveFn] = None,
    generate_fn: Optional[GenerateFn] = None,
) -> VariantResult:
    """Run *config* over the whole *dataset* and return aggregated results."""
    retrieve_fn = retrieve_fn or _default_retrieve
    generate_fn = generate_fn or _default_generate

    logger.info("Evaluating variant '%s' over %d questions ...", config.name, len(dataset.questions))
    runs: List[QuestionRun] = []
    for i, question in enumerate(dataset.questions, start=1):
        runs.append(run_question(question, config, metrics, k, retrieve_fn, generate_fn))
        if i % 10 == 0 or i == len(dataset.questions):
            logger.info("  [%s] %d / %d done", config.name, i, len(dataset.questions))

    return VariantResult(
        variant=config.name,
        config=config.model_dump(),
        created_at=datetime.now().isoformat(timespec="seconds"),
        dataset_size=len(dataset.questions),
        aggregate=_aggregate(runs),
        per_question=runs,
    )
