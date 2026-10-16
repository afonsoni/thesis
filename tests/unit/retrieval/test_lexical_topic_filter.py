"""``lexical_topic_filter`` drops the topic filter from the BM25 list only."""

import pytest

from src.rag.retrieval.config import RetrievalConfig
from src.rag.retrieval.searcher import Searcher


class NoHitsEmbedder:
    def encode_query(self, text):
        return [0.0]


class RecordingStore:
    def __init__(self):
        self.lexical_topics = []

    def similarity_search(self, **kwargs):
        return []

    def lexical_search(self, query, top_k, party_name=None, topics=None):
        self.lexical_topics.append(topics)
        return []


@pytest.mark.parametrize("flag, expected", [(True, ["cultura"]), (False, None)])
def test_lexical_topic_filter_only_drops_topics_from_the_lexical_list(flag, expected):
    s = Searcher.__new__(Searcher)
    s.embedder, s.store = NoHitsEmbedder(), RecordingStore()
    s.multi_query_search(["q"], RetrievalConfig(lexical_topic_filter=flag), 5, "q", topics=["cultura"])
    assert s.store.lexical_topics == [expected]
