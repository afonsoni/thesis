"""
Okapi BM25 over PostgreSQL ``tsvector`` lexemes — the lexical half of hybrid search.

Tokenisation, Portuguese stemming and stop-word removal stay in PostgreSQL (the
stored ``content_tsv`` column and ``to_tsvector('portuguese', query)``); this
module only does the ranking, which PostgreSQL's ``ts_rank`` cannot: it has no
inverse document frequency, so a common word ("é", "posição") counts as much as
the rare one ("tourada") that the question is really about.

Matching is OR over the query lexemes. Requiring all of them (what
``websearch_to_tsquery`` does) matched almost no chunk for a natural-language
question, which silently turned hybrid search into dense search.
"""

from __future__ import annotations

import math
import re
from collections import defaultdict
from typing import Dict, Iterable, List, Optional, Set, Tuple

# Standard Okapi constants (Robertson & Zaragoza, 2009).
K1 = 1.2
B = 0.75

_LEXEME_RE = re.compile(r"'((?:[^']|'')+)'(?::([0-9A-D,]+))?")


def parse_tsvector(text: str) -> Dict[str, int]:
    """``"'lexeme':1,5 'outro':3"`` -> ``{"lexeme": 2, "outro": 1}`` (term frequencies)."""
    out: Dict[str, int] = {}
    for m in _LEXEME_RE.finditer(text or ""):
        lexeme = m.group(1).replace("''", "'")
        out[lexeme] = len(m.group(2).split(",")) if m.group(2) else 1
    return out


class Bm25Index:
    """Inverted index of ``{doc_id: {lexeme: tf}}`` with BM25 scoring."""

    def __init__(self, docs: Iterable[Tuple[str, Dict[str, int]]]):
        self.postings: Dict[str, Dict[str, int]] = defaultdict(dict)
        self.length: Dict[str, int] = {}
        for doc_id, tfs in docs:
            self.length[doc_id] = sum(tfs.values())
            for lexeme, tf in tfs.items():
                self.postings[lexeme][doc_id] = tf
        self.n = len(self.length)
        self.avg_len = (sum(self.length.values()) / self.n) if self.n else 0.0

    def idf(self, lexeme: str) -> float:
        df = len(self.postings.get(lexeme, ()))
        # Lucene's variant: never negative, so very common terms add ~nothing
        # instead of subtracting from a document's score.
        return math.log(1 + (self.n - df + 0.5) / (df + 0.5))

    def top_k(self, terms: Iterable[str], k: int, allowed: Optional[Set[str]] = None) -> List[Tuple[str, float]]:
        """Best *k* ``(doc_id, score)`` for the query *terms*, restricted to *allowed* ids."""
        scores: Dict[str, float] = defaultdict(float)
        for term in set(terms):
            postings = self.postings.get(term)
            if not postings:
                continue
            idf = self.idf(term)
            for doc_id, tf in postings.items():
                if allowed is not None and doc_id not in allowed:
                    continue
                norm = K1 * (1 - B + B * self.length[doc_id] / self.avg_len)
                scores[doc_id] += idf * tf * (K1 + 1) / (tf + norm)
        return sorted(scores.items(), key=lambda kv: kv[1], reverse=True)[:k]
