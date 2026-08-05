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
        top_k: int = 5,
        party_name: Optional[str] = None,
        ideology: Optional[str] = None,
        topics: Optional[List[str]] = None,
        year: Optional[int] = None,
        rrf_k: int = 60,
        use_rrf: bool = True,
        use_hybrid: bool = False,
    ) -> List[SearchResult]:
        self.multi_query_calls.append(
            {
                "queries": queries,
                "top_k": top_k,
                "party_name": party_name,
                "ideology": ideology,
                "topics": topics,
                "year": year,
                "rrf_k": rrf_k,
                "use_rrf": use_rrf,
                "use_hybrid": use_hybrid,
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


@pytest.mark.unit
def test_route_single_party_uses_party_filter():
    searcher = StubSearcher()
    analyzed = AnalyzedQuery(
        original_query="PS e educacao",
        reformulated_query="partido socialista educacao",
        query_type=QueryType.SINGLE_PARTY,
        parties=["Partido Socialista"],
        topics=["educacao"],
    )

    retrieval = route(analyzed, searcher, config=_no_expand(top_k=5))

    assert retrieval.results
    assert searcher.multi_query_calls[0]["party_name"] == "Partido Socialista"
    assert searcher.multi_query_calls[0]["topics"] == ["educacao"]


@pytest.mark.unit
def test_route_comparison_searches_each_party_separately():
    searcher = StubSearcher()
    analyzed = AnalyzedQuery(
        original_query="Comparar PS e AD na saude",
        reformulated_query="comparacao saude",
        query_type=QueryType.COMPARISON,
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


@pytest.mark.unit
def test_route_general_uses_multi_query_without_filters():
    searcher = StubSearcher()
    analyzed = AnalyzedQuery(
        original_query="Qual a visao economica geral?",
        reformulated_query="visao economica geral",
        query_type=QueryType.GENERAL,
    )

    retrieval = route(analyzed, searcher, config=_no_expand(top_k=4))

    assert retrieval.results
    assert searcher.multi_query_calls[0]["party_name"] is None
    assert searcher.multi_query_calls[0]["ideology"] is None
    assert searcher.multi_query_calls[0]["topics"] is None


@pytest.mark.unit
def test_route_single_party_relaxes_topics_when_nothing_matches():
    """A topic no chunk carries must not turn a good question into zero results."""
    searcher = StubSearcher(empty_when_topics=True)
    analyzed = AnalyzedQuery(
        original_query="PS e educacao",
        reformulated_query="partido socialista educacao",
        query_type=QueryType.SINGLE_PARTY,
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


@pytest.mark.unit
def test_route_does_not_retry_when_no_topics_were_requested():
    """Without a topic filter an empty result is genuine, so there is nothing to relax."""
    searcher = StubSearcher(empty_when_topics=True)
    analyzed = AnalyzedQuery(
        original_query="visao economica geral",
        reformulated_query="visao economica geral",
        query_type=QueryType.GENERAL,
    )

    route(analyzed, searcher, config=_no_expand(top_k=5))

    assert len(searcher.multi_query_calls) == 1


@pytest.mark.unit
def test_route_comparison_relaxes_topics_per_party():
    """One party missing a topic must not strip the filter from the others."""
    searcher = StubSearcher(empty_when_topics=True)
    analyzed = AnalyzedQuery(
        original_query="Comparar PS e AD na saude",
        reformulated_query="comparacao saude",
        query_type=QueryType.COMPARISON,
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


@pytest.mark.unit
def test_route_naive_config_disables_routing_and_rrf():
    """Naive baseline: no routing (always general) and no RRF fusion."""
    searcher = StubSearcher()
    analyzed = AnalyzedQuery(
        original_query="PS e educacao",
        reformulated_query="partido socialista educacao",
        query_type=QueryType.SINGLE_PARTY,
        parties=["Partido Socialista"],
        topics=["educacao"],
    )

    naive = RetrievalConfig(
        name="naive",
        use_query_analysis=False,
        use_routing=False,
        use_multi_query=False,
        use_rrf=False,
        top_k=5,
    )
    retrieval = route(analyzed, searcher, config=naive)

    assert retrieval.results
    # Routing disabled → general path → no party/topic filters applied.
    assert searcher.multi_query_calls[0]["party_name"] is None
    assert searcher.multi_query_calls[0]["topics"] is None
    assert searcher.multi_query_calls[0]["use_rrf"] is False
    # Routing off means the comparison strategy never runs, so exactly one
    # unfiltered search is issued rather than one per party.
    assert len(searcher.multi_query_calls) == 1
