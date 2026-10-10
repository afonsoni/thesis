from typing import List, Optional

import pytest

from src.rag.common.models import AnalyzedQuery, QueryType, SearchResult
from src.rag.retrieval.config import RetrievalConfig
from src.rag.retrieval.router import route
from src.rag.retrieval.searcher import Searcher


def _no_expand(**overrides) -> RetrievalConfig:
    """Config mirroring the old ``expand_queries=False`` call style."""
    return RetrievalConfig(use_multi_query=False, **overrides)


class StubSearcher(Searcher):
    def __init__(self, empty_when_topics: bool = False):
        self.multi_query_calls = []
        # Simulates an index where no chunk carries the requested topic, e.g. one
        # built with --no-classify, or a topic outside the classifier's vocabulary.
        self.empty_when_topics = empty_when_topics

    def multi_query_search(
        self,
        queries: List[str],
        config: RetrievalConfig,
        top_k: int,
        rerank_query: str,
        party_name: Optional[str] = None,
        topics: Optional[List[str]] = None,
    ) -> List[SearchResult]:
        self.multi_query_calls.append(
            {
                "queries": queries,
                "top_k": top_k,
                "party_name": party_name,
                "topics": topics,
                "use_reranker": config.use_reranker,
                "rerank_query": rerank_query,
                "rerank_candidates": config.rerank_candidates,
            }
        )
        if topics and self.empty_when_topics:
            return []
        return [
            SearchResult(
                id="doc-1",
                content="conteudo",
                party_name=party_name or "Partido Socialista",
                topics=topics or ["educacao"],
                similarity=0.8,
            )
        ]


@pytest.mark.parametrize(
    "parties, topics, expected_type",
    [
        (["Partido Socialista"], ["educacao"], QueryType.SINGLE_PARTY),
        ([], ["habitacao"], QueryType.TOPIC_EXPLORATION),
        ([], [], QueryType.GENERAL),
    ],
)
def test_non_comparison_routes_are_one_filtered_search(parties, topics, expected_type):
    searcher = StubSearcher()
    analyzed = AnalyzedQuery(original_query="Pergunta?", parties=parties, topics=topics)
    assert analyzed.query_type == expected_type

    retrieval = route(analyzed, searcher, config=_no_expand(top_k=5))

    assert retrieval.results
    assert len(searcher.multi_query_calls) == 1
    assert searcher.multi_query_calls[0]["party_name"] == (parties[0] if parties else None)
    assert searcher.multi_query_calls[0]["topics"] == (topics or None)


def test_route_comparison_searches_each_party_separately():
    searcher = StubSearcher()
    analyzed = AnalyzedQuery(
        original_query="Comparar PS e AD na saude",
        reformulated_query="comparacao saude",
        parties=["Partido Socialista", "Aliança Democrática"],
        topics=["saude"],
    )

    retrieval = route(analyzed, searcher, config=_no_expand(top_k=5, top_k_per_party=3))

    assert retrieval.results_by_party
    assert set(retrieval.results_by_party.keys()) == {"Partido Socialista", "Aliança Democrática"}
    # One filtered search per party, each sized by top_k_per_party rather than
    # top_k, so every party contests the same number of slots.
    assert [c["party_name"] for c in searcher.multi_query_calls] == [
        "Partido Socialista",
        "Aliança Democrática",
    ]
    assert all(c["topics"] == ["saude"] for c in searcher.multi_query_calls)
    assert all(c["top_k"] == 3 for c in searcher.multi_query_calls)


def test_route_single_party_relaxes_topics_when_nothing_matches():
    """A topic no chunk carries must not turn a good question into zero results."""
    searcher = StubSearcher(empty_when_topics=True)
    analyzed = AnalyzedQuery(
        original_query="PS e educacao",
        reformulated_query="partido socialista educacao",
        parties=["Partido Socialista"],
        topics=["educacao"],
    )

    retrieval = route(analyzed, searcher, config=_no_expand(top_k=5))

    assert retrieval.results, "expected the unfiltered retry to return results"
    assert len(searcher.multi_query_calls) == 2
    # Narrow first, then relax only the topics — the party filter must survive.
    assert searcher.multi_query_calls[0]["topics"] == ["educacao"]
    assert searcher.multi_query_calls[1]["topics"] is None
    assert all(c["party_name"] == "Partido Socialista" for c in searcher.multi_query_calls)


def test_route_comparison_relaxes_topics_per_party():
    """One party missing a topic must not strip the filter from the others."""
    searcher = StubSearcher(empty_when_topics=True)
    analyzed = AnalyzedQuery(
        original_query="Comparar PS e AD na saude",
        reformulated_query="comparacao saude",
        parties=["Partido Socialista", "Aliança Democrática"],
        topics=["saude"],
    )

    retrieval = route(analyzed, searcher, config=_no_expand(top_k=5, top_k_per_party=3))

    assert set(retrieval.results_by_party) == {"Partido Socialista", "Aliança Democrática"}
    # Two parties, each narrowing then relaxing independently.
    assert len(searcher.multi_query_calls) == 4
    for party in ("Partido Socialista", "Aliança Democrática"):
        calls = [c for c in searcher.multi_query_calls if c["party_name"] == party]
        assert [c["topics"] for c in calls] == [["saude"], None]


def test_route_naive_config_disables_routing():
    """Naive baseline: no routing (always general)."""
    searcher = StubSearcher()
    analyzed = AnalyzedQuery(
        original_query="PS e educacao",
        reformulated_query="partido socialista educacao",
        parties=["Partido Socialista"],
        topics=["educacao"],
    )

    naive = RetrievalConfig(
        name="naive",
        use_query_analysis=False,
        use_routing=False,
        use_multi_query=False,
        top_k=5,
    )
    retrieval = route(analyzed, searcher, config=naive)

    assert retrieval.results
    # Routing disabled → general path → no party/topic filters applied.
    assert searcher.multi_query_calls[0]["party_name"] is None
    assert searcher.multi_query_calls[0]["topics"] is None
    # Routing off means the comparison strategy never runs, so exactly one
    # unfiltered search is issued rather than one per party.
    assert len(searcher.multi_query_calls) == 1


def test_route_passes_original_question_to_the_reranker():
    """The cross-encoder must score the question the user asked, not a rewrite.

    ``reformulated_query`` is what gets embedded, but reranking is a pairwise
    judgement about the real information need, so the two must not be conflated.
    """
    searcher = StubSearcher()
    analyzed = AnalyzedQuery(
        original_query="O que propoe o PS para a educacao?",
        reformulated_query="partido socialista educacao propostas",
        parties=["Partido Socialista"],
    )

    route(analyzed, searcher, config=_no_expand(use_reranker=True, rerank_candidates=25))

    call = searcher.multi_query_calls[0]
    assert call["use_reranker"] is True
    assert call["rerank_query"] == "O que propoe o PS para a educacao?"
    assert call["rerank_candidates"] == 25
