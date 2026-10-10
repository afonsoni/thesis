"""
Integration test: run a variant end-to-end over seeded pgvector.

Exercises the real Searcher + pgvector + router + metrics + report, fully
offline: the ``naive`` variant skips query-analysis (no LLM), generation is
injected, and the LLM-judge is not used.
"""

import os


from src.rag.evaluation.keys import chunk_key
from src.rag.evaluation.metrics.retrieval import RetrievalMetric
from src.rag.evaluation.metrics.routing import RoutingMetric
from src.rag.evaluation.models import EvalDataset, EvalQuestion
from src.rag.evaluation.report import write_leaderboard
from src.rag.evaluation.runner import run_variant
from src.rag.evaluation.variants import get_variant
from src.rag.common.models import GeneratedAnswer
from src.rag.retrieval.query_analyzer import analyze_query
from src.rag.retrieval.router import route

_PS_EDU = "O Partido Socialista reforca o investimento em educacao publica."


def test_run_variant_on_seeded_store(seeded_searcher, tmp_path):
    # naive variant: no query analysis / routing / expansion / RRF → fully offline
    naive = get_variant("naive")

    def retrieve_fn(question, cfg):
        analyzed = analyze_query(question, config=cfg)
        return route(analyzed, seeded_searcher, config=cfg)

    def generate_fn(result):
        return GeneratedAnswer(answer="Resposta simulada sobre educacao.")

    dataset = EvalDataset(questions=[
        EvalQuestion(
            id="q-0001",
            question="O que propõe o PS para a educacao publica?",
            query_type="general",
            gold_chunk_keys=[chunk_key(_PS_EDU)],
        )
    ])

    result = run_variant(
        naive, dataset,
        metrics=[RetrievalMetric(), RoutingMetric()],
        k=5,
        retrieve_fn=retrieve_fn,
        generate_fn=generate_fn,
    )

    assert result.dataset_size == 1
    assert result.per_question[0].error is None
    # The seeded PS education chunk should be retrieved for an education query.
    assert result.aggregate["hit"] == 1.0
    assert result.aggregate["error_rate"] == 0.0
    # naive skips analysis → predicted type is general, matching the gold type.
    assert result.aggregate["query_type_acc"] == 1.0

    md_path = write_leaderboard([result], str(tmp_path))
    assert os.path.exists(md_path)
    assert "| naive |" in open(md_path, encoding="utf-8").read()
