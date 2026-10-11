"""Unit tests for cross-encoder reranking.

The cross-encoder itself is stubbed: these tests are about the wiring (what gets
scored, how far retrieval widens, what the trim returns), not about the quality
of any particular model, and a unit run must not download 568M parameters.
"""

from typing import List, Optional


from src.rag.common.models import ScoreType, SearchResult
from src.rag.retrieval.config import RetrievalConfig
from src.rag.retrieval.reranker import Reranker
from src.rag.retrieval.searcher import Searcher


class FakeCrossEncoder:
    """Scores a pair by how many words it shares with the query — deterministic,
    order-sensitive, and enough to prove the ranking is actually applied."""

    def __init__(self):
        self.seen_pairs: List[tuple] = []

    def predict(self, pairs, batch_size=32, show_progress_bar=False):
        self.seen_pairs.extend(pairs)
        scores = []
        for query, passage in pairs:
            overlap = set(query.lower().split()) & set(passage.lower().split())
            scores.append(float(len(overlap)))
        return scores


def _reranker_with(fake: FakeCrossEncoder) -> Reranker:
    """Build a Reranker around the fake, bypassing model loading."""
    rr = Reranker.__new__(Reranker)
    rr.model_name = "fake-cross-encoder"
    rr.model = fake
    return rr


def _result(doc_id: str, content: str, similarity: float = 0.5) -> SearchResult:
    return SearchResult(id=doc_id, content=content, similarity=similarity)


# ---------------------------------------------------------------------------
# Reranker unit behavior
# ---------------------------------------------------------------------------


def test_rerank_reorders_by_cross_encoder_score():
    """A weak dense hit that the cross-encoder likes must overtake a strong one."""
    fake = FakeCrossEncoder()
    results = [
        _result("a", "orcamento do estado", similarity=0.99),
        _result("b", "propostas para a educacao publica", similarity=0.10),
    ]

    out = _reranker_with(fake).rerank("educacao publica", results, top_k=2)

    assert [r.id for r in out] == ["b", "a"]
    assert out[0].similarity == 2.0  # both query words matched
    assert all(r.score_type is ScoreType.RERANK for r in out)


def test_rerank_scores_the_child_not_the_parent():
    """Small-to-big siblings share a parent; scoring it would tie them all.

    The reranker must read ``content`` (the embedded child) so that siblings can
    be told apart, while generation keeps reading ``parent_content``.
    """
    fake = FakeCrossEncoder()
    parent = "seccao inteira sobre varios temas"
    results = [
        SearchResult(id="child-1", content="habitacao jovem", parent_content=parent),
        SearchResult(id="child-2", content="transportes urbanos", parent_content=parent),
    ]

    out = _reranker_with(fake).rerank("habitacao jovem", results, top_k=2)

    assert [p[1] for p in fake.seen_pairs] == ["habitacao jovem", "transportes urbanos"]
    assert out[0].id == "child-1"
    # Generation context is untouched by reranking.
    assert out[0].context_text == parent

# ---------------------------------------------------------------------------
# Searcher integration: over-fetch, then trim
# ---------------------------------------------------------------------------


class StubStore:
    def connect(self):
        pass

    def close(self):
        pass


class RecordingSearcher(Searcher):
    """Searcher with the vector store and embedder replaced by counters."""

    def __init__(self, corpus_size: int = 50):
        self.store = StubStore()
        self.corpus_size = corpus_size
        self.requested_top_k: List[int] = []

    def search(
        self,
        query: str,
        top_k: int = 5,
        party_name: Optional[str] = None,
        topics: Optional[List[str]] = None,
        instruction: Optional[str] = None,
    ) -> List[SearchResult]:
        self.requested_top_k.append(top_k)
        return [
            _result(f"doc-{i}", f"documento {i} sobre educacao")
            for i in range(min(top_k, self.corpus_size))
        ]


def test_multi_query_search_widens_the_fetch_when_reranking(monkeypatch):
    """Reranking a list of exactly top_k could only reshuffle it, never improve
    it — so retrieval must fetch rerank_candidates first."""
    fake = FakeCrossEncoder()
    monkeypatch.setattr(
        "src.rag.retrieval.reranker.get_reranker", lambda: _reranker_with(fake)
    )
    searcher = RecordingSearcher()

    out = searcher.multi_query_search(
        ["educacao"],
        RetrievalConfig(use_reranker=True, rerank_candidates=30, use_hybrid=False),
        top_k=5,
        rerank_query="educacao",
    )

    assert searcher.requested_top_k == [30], "sub-query should fetch the wide set"
    assert len(fake.seen_pairs) == 30, "every candidate should be scored"
    assert len(out) == 5, "and the answer trimmed back to top_k"
