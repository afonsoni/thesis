from typing import Dict, List, Optional

import pytest

from src.rag.common.models import AnalyzedQuery, QueryType, SearchResult
from src.rag.retrieval.config import RetrievalConfig
from src.rag.retrieval.router import route
from src.rag.retrieval.searcher import Searcher


def _no_expand(**overrides) -> RetrievalConfig:
    """Config mirroring the old ``expand_queries=False`` call style."""
    return RetrievalConfig(use_multi_query=False, **overrides)


class StubSearcher(Searcher):
    def __init__(self):
        self.multi_query_calls = []
        self.batch_calls = []

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
            }
        )
        return [
            SearchResult(
                id="doc-1",
                content="conteudo",
                party_name=party_name or "Partido Socialista",
                topics=topics or ["educacao"],
                similarity=0.8,
            )
        ]

    def multi_query_batch_search_by_party(
        self,
        queries: List[str],
        parties: List[str],
        top_k_per_party: int = 3,
        topics: Optional[List[str]] = None,
        rrf_k: int = 60,
        use_rrf: bool = True,
    ) -> Dict[str, List[SearchResult]]:
        self.batch_calls.append(
            {
                "queries": queries,
                "parties": parties,
                "top_k_per_party": top_k_per_party,
                "topics": topics,
                "rrf_k": rrf_k,
                "use_rrf": use_rrf,
            }
        )
        return {
            party: [
                SearchResult(
                    id=f"{party}-1",
                    content=f"conteudo {party}",
                    party_name=party,
                    topics=topics or ["educacao"],
                    similarity=0.7,
                )
            ]
            for party in parties
        }


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
def test_route_comparison_uses_batch_by_party():
    searcher = StubSearcher()
    analyzed = AnalyzedQuery(
        original_query="Comparar PS e AD na saude",
        reformulated_query="comparacao saude",
        query_type=QueryType.COMPARISON,
        parties=["Partido Socialista", "Aliança Democrática"],
        topics=["saude"],
    )

    retrieval = route(analyzed, searcher, config=_no_expand(top_k=5))

    assert retrieval.results_by_party
    assert set(retrieval.results_by_party.keys()) == {"Partido Socialista", "Aliança Democrática"}
    assert searcher.batch_calls[0]["topics"] == ["saude"]


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
    assert not searcher.batch_calls
