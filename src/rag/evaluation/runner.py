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
from typing import Any, Callable, Dict, List, Optional, Protocol

from src.rag.common.llm_client import CALL_LOG, call_with_wait_out
from src.rag.common.models import RetrievalResult, SearchResult
from src.rag.evaluation.keys import chunk_key
from src.rag.evaluation.models import EvalDataset, EvalQuestion, QuestionRun, VariantResult
from src.rag.retrieval.config import RetrievalConfig

logger = logging.getLogger(__name__)

class Metric(Protocol):
    """Anything with a ``name`` and ``score(run, question) -> {metric: value in [0, 1]}``."""
    name: str

    def score(self, run: QuestionRun, question: EvalQuestion) -> Dict[str, float]: ...


RetrieveFn = Callable[[str, RetrievalConfig], RetrievalResult]
GenerateFn = Callable[[RetrievalResult], object]


def _default_retrieve(question: str, config: RetrievalConfig) -> RetrievalResult:
    from src.rag.retrieval.pipeline import retrieve
    return retrieve(question, config=config)


def _default_generate(result: RetrievalResult):
    from src.rag.generation.pipeline import generate
    return generate(result)


def _flatten_results(result: RetrievalResult) -> List[SearchResult]:
    """The ranked list retrieval hands to generation, which is what gets scored.

    A per-party fan-out is scored on every party's list, interleaved by rank
    (each party's best, then each party's second, ...), because that is what the
    generator reads. Its flat ``results`` is a cross-party top_k whose RRF ties
    break in PARTY_MAP order, so scoring it cut PAN, PCP and PS out of
    comparisons they were retrieved for.
    """
    if not result.results_by_party:
        return result.results
    lists = list(result.results_by_party.values())
    interleaved: List[SearchResult] = []
    for rank in range(max((len(rs) for rs in lists), default=0)):
        tier = [rs[rank] for rs in lists if rank < len(rs)]
        interleaved.extend(sorted(tier, key=lambda r: r.similarity, reverse=True))
    return interleaved


def _build_context(results: List[SearchResult], k: int) -> str:
    return "\n\n".join(f"[{r.party_name}] {r.content}" for r in results[:k])


def run_question(
    question: EvalQuestion,
    config: RetrievalConfig,
    metrics: List[Metric],
    k: int,
    retrieve_fn: RetrieveFn,
    generate_fn: Optional[GenerateFn],
    wait_out_attempts: int = 1,
) -> QuestionRun:
    """Run the pipeline on one question and apply all metrics.

    Retrieval and generation fail separately: a generation failure is recorded
    as the run's error but keeps the retrieval and routing scores, which do not
    depend on it. Each stage waits out free-tier failures *wait_out_attempts*
    times. ``strict`` is forced on, so an LLM step that still fails raises here
    instead of quietly running a degraded pipeline under this variant's name.
    """
    config = config.model_copy(update={"strict": True})
    run = QuestionRun(question_id=question.id, variant=config.name)
    first_call = len(CALL_LOG)
    start = time.perf_counter()
    try:
        result = call_with_wait_out(
            lambda: retrieve_fn(question.question, config),
            f"[{config.name}] {question.id} retrieval",
            attempts=wait_out_attempts,
        )
    except Exception as exc:  # noqa: BLE001 - one bad question shouldn't kill the run
        run.error = f"retrieval: {exc}"
        run.latency_s = round(time.perf_counter() - start, 3)
        run.llm_calls = _calls_since(first_call)
        logger.warning("Question %s failed: %s", question.id, run.error)
        return run

    results = _flatten_results(result)
    run.retrieved_keys = [chunk_key(r.content) for r in results]
    run.retrieved_parties = list(dict.fromkeys(r.party_name for r in results))
    run.predicted_query_type = result.query.query_type.value
    run.predicted_coverage = result.query.coverage.value
    run.predicted_parties = result.query.parties
    run.predicted_topics = result.query.topics

    if generate_fn is not None:
        try:
            answer = call_with_wait_out(
                lambda: generate_fn(result),
                f"[{config.name}] {question.id} generation",
                attempts=wait_out_attempts,
            )
            run.answer = getattr(answer, "answer", "") or ""
            # Judge against what the generator read (parent sections, trimmed to
            # the prompt budget); the top-k child chunks are only a fallback for
            # generators that do not report their context.
            run.context = getattr(answer, "context", "") or _build_context(results, k)
        except Exception as exc:  # noqa: BLE001
            run.error = f"generation: {exc}"
            logger.warning("Question %s failed: %s", question.id, run.error)
    run.latency_s = round(time.perf_counter() - start, 3)

    # An empty answer (generation failed or skipped) yields no judge scores.
    for metric in metrics:
        try:
            run.metrics.update(metric.score(run, question))
        except Exception as exc:  # noqa: BLE001
            logger.warning("Metric %s failed on %s: %s", metric.name, question.id, exc)

    run.llm_calls = _calls_since(first_call)
    return run


def _calls_since(first: int) -> List[Dict[str, Any]]:
    return CALL_LOG[first:]


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
    generate: bool = True,
    wait_out_attempts: int = 1,
) -> VariantResult:
    """Run *config* over the whole *dataset* and return aggregated results.

    ``generate=False`` skips answer generation (retrieval and routing scores
    only), so a ``--no-judge`` run spends no LLM calls on answers nobody scores.
    """
    retrieve_fn = retrieve_fn or _default_retrieve
    generate_fn = (generate_fn or _default_generate) if generate else None

    logger.info("Evaluating variant '%s' over %d questions ...", config.name, len(dataset.questions))
    runs: List[QuestionRun] = []
    for i, question in enumerate(dataset.questions, start=1):
        runs.append(run_question(question, config, metrics, k, retrieve_fn, generate_fn, wait_out_attempts))
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
