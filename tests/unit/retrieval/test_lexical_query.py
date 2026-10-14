"""The lexical query of a party-filtered search drops the party's name.

Left in, "ps" or "chega" is a rare, heavily weighted BM25 term that ranks a
party's self-references above the topic the question is about.
"""

from typing import List

import pytest

from src.rag.retrieval.config import RetrievalConfig
from src.rag.retrieval.query_analyzer import strip_party_mentions
from src.rag.retrieval.searcher import Searcher


def test_strip_party_mentions_blanks_names_and_keeps_accents():
    assert strip_party_mentions("Propostas do PS para a saúde?").split() == ["Propostas", "do", "para", "a", "saúde?"]
    assert "Aliança" not in strip_party_mentions("A Aliança Democrática e o CDS-PP sobre habitação")
    assert "habitação" in strip_party_mentions("A Aliança Democrática e o CDS-PP sobre habitação")
    # Word-anchored: "ps" inside another word is not a party.
    assert strip_party_mentions("lapso") == "lapso"


class LexicalRecorder:
    def __init__(self):
        self.queries: List[str] = []

    def lexical_search(self, query, **kwargs):
        self.queries.append(query)
        return []


class DenseStub(Searcher):
    def __init__(self):
        self.store = LexicalRecorder()

    def search(self, query, **kwargs):
        return []


@pytest.mark.parametrize("party, expected", [
    ("Partido Socialista", "O que propõe o   para a saúde?"),  # BM25 lowercases on its side
    (None, "O que propõe o PS para a saúde?"),  # no filter: the name is the only party signal
])


def test_hybrid_search_strips_party_only_under_a_party_filter(party, expected):
    searcher = DenseStub()
    searcher.multi_query_search(["O que propõe o PS para a saúde?"], RetrievalConfig(use_hybrid=True), 5, "q",
                                party_name=party)
    assert searcher.store.queries == [expected]
