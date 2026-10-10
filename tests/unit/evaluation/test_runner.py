from src.rag.common.models import AnalyzedQuery, GeneratedAnswer, RetrievalResult, SearchResult
from src.rag.evaluation.keys import chunk_key
from src.rag.evaluation.metrics.retrieval import RetrievalMetric
from src.rag.evaluation.models import EvalQuestion
from src.rag.evaluation.runner import run_question
from src.rag.retrieval.config import RetrievalConfig

Q = EvalQuestion(id="q-01", question="Q?", gold_chunk_keys=[chunk_key("gold")])


def _hit(content, party="AD", score=0.5):
    return SearchResult(id=content, content=content, party_name=party, similarity=score)


def _fail(*_):
    raise RuntimeError("429")


def test_generation_failure_keeps_the_retrieval_scores():
    result = RetrievalResult(query=AnalyzedQuery(original_query="Q?"), results=[_hit("gold")])
    run = run_question(Q, RetrievalConfig(name="v"), [RetrievalMetric()], 5,
                       retrieve_fn=lambda q, c: result, generate_fn=_fail)
    assert run.error.startswith("generation:")
    assert run.metrics["hit"] == 1.0


def test_retrieval_runs_strict_so_a_fallback_cannot_pass_as_the_variant():
    seen = {}
    run_question(Q, RetrievalConfig(name="v"), [], 5,
                 retrieve_fn=lambda q, c: seen.setdefault("strict", c.strict) and _fail(),
                 generate_fn=None)
    assert seen["strict"] is True


def test_fan_out_is_scored_on_every_party_not_the_flat_top_k():
    # Equal RRF scores: the router's flat top-k keeps AD and BE and drops PS.
    grouped = {"AD": [_hit("a1", "AD")], "BE": [_hit("b1", "BE")], "PS": [_hit("gold", "PS")]}
    result = RetrievalResult(query=AnalyzedQuery(original_query="Q?", parties=list(grouped)),
                             results=[_hit("a1", "AD"), _hit("b1", "BE")], results_by_party=grouped)
    run = run_question(Q, RetrievalConfig(name="v"), [RetrievalMetric()], 2,
                       retrieve_fn=lambda q, c: result,
                       generate_fn=lambda r: GeneratedAnswer(answer="A", context="C"))
    assert run.error is None
    assert run.retrieved_parties == ["AD", "BE", "PS"]
    assert run.metrics["hit"] == 1.0


def test_each_question_records_its_llm_calls():
    from src.rag.common.llm_client import CALL_LOG

    def retrieve(q, c):
        CALL_LOG.append(("query analysis", "google/gemma-4-26b-a4b-it:free"))
        return RetrievalResult(query=AnalyzedQuery(original_query=q), results=[_hit("gold")])

    def generate(r):
        CALL_LOG.append(("answer", "nvidia/nemotron-3-ultra-550b-a55b:free"))
        return GeneratedAnswer(answer="A", context="C")

    run = run_question(Q, RetrievalConfig(name="v"), [], 5, retrieve_fn=retrieve, generate_fn=generate)
    assert run.llm_calls == [
        {"step": "query analysis", "model": "google/gemma-4-26b-a4b-it:free"},
        {"step": "answer", "model": "nvidia/nemotron-3-ultra-550b-a55b:free"},
    ]
