"""The dense-retrieval ablation switches reach the encoder (DECISIONS.md, 2026-10-09)."""

from typing import List, Tuple

import pytest

from src.rag.retrieval.searcher import Searcher


class RecordingEmbedder:
    def __init__(self):
        self.calls: List[Tuple[str, object]] = []

    def encode_query(self, text, instruction=None):
        self.calls.append((text, instruction))
        return [0.0]


class NoHits:
    def similarity_search(self, **kwargs):
        return []


def _searcher() -> Searcher:
    s = Searcher.__new__(Searcher)
    s.embedder, s.store = RecordingEmbedder(), NoHits()
    return s


@pytest.mark.unit
@pytest.mark.parametrize("strip, party, expected", [
    (True, "Pessoas-Animais-Natureza", "qual é a posição do   sobre as touradas?"),
    (True, None, "Qual é a posição do PAN sobre as touradas?"),   # no filter: keep the only party signal
    (False, "Pessoas-Animais-Natureza", "Qual é a posição do PAN sobre as touradas?"),
])
def test_dense_query_drops_party_names_only_when_asked_and_filtered(strip, party, expected):
    s = _searcher()
    s.multi_query_search(["Qual é a posição do PAN sobre as touradas?"], party_name=party, strip_party_names=strip)
    assert s.embedder.calls == [(expected, None)]


@pytest.mark.unit
def test_query_instruction_reaches_the_encoder():
    s = _searcher()
    s.multi_query_search(["q"], query_instruction="Given a manifesto question")
    assert s.embedder.calls == [("q", "Given a manifesto question")]
