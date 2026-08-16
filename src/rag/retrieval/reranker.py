"""
Cross-encoder reranking – the precision half of retrieval.

Bi-encoder retrieval (what the vector store does) embeds the query and every
chunk *independently*, so a chunk's vector cannot depend on the question being
asked. That is what makes it fast enough to search a whole corpus, and also what
caps its precision: the top-k comes back ordered by a similarity that never saw
the two texts together.

A cross-encoder scores the pair jointly — query and chunk in one forward pass,
with full attention between them — which is far more accurate and far too slow
to run over a corpus. The standard resolution is to use both: retrieve a wide
candidate set cheaply, then re-order it with the expensive model and keep the
top few. This module is the second stage.

Scores are the model's raw relevance logits: unbounded, and NOT comparable to
cosine similarities or RRF scores, which is why reranked results carry
``ScoreType.RERANK``.
"""

from __future__ import annotations

import logging
from typing import List, Optional

from src.rag.common.models import ScoreType, SearchResult
from src.utils.config_loader import config

logger = logging.getLogger(__name__)

# Multilingual by construction: trained on mMARCO, which includes Portuguese.
# A Portuguese query against Portuguese passages needs a model that was trained
# on pairs in the language, not an English reranker applied hopefully.
DEFAULT_RERANKER_MODEL = "BAAI/bge-reranker-v2-m3"


class Reranker:
    """Wraps a CrossEncoder to re-order retrieved candidates by joint relevance."""

    def __init__(self, model_name: Optional[str] = None):
        # Imported lazily: loading sentence_transformers' CrossEncoder pulls in
        # torch, and a run with the reranker disabled should not pay for it.
        from sentence_transformers import CrossEncoder

        self.model_name = model_name or str(
            config.get("retrieval.reranker_model", DEFAULT_RERANKER_MODEL)
        )
        logger.info("Loading reranker model: %s", self.model_name)
        # Deliberately unguarded: a failure here raises rather than degrading to
        # un-reranked results. A variant named `reranked` that quietly skipped
        # reranking would report the baseline's scores under the new name and
        # silently corrupt the leaderboard — the same class of silent failure
        # that the encoder-truncation bug taught this project to refuse.
        self.model = CrossEncoder(self.model_name)

    def rerank(
        self,
        query: str,
        results: List[SearchResult],
        top_k: int,
        batch_size: int = 32,
    ) -> List[SearchResult]:
        """Score every candidate against *query* and return the best *top_k*.

        Scoring uses ``content`` — the text that was actually embedded — rather
        than ``context_text``. Under the small-to-big strategy many children
        share one parent section, so scoring the parent would hand every sibling
        an identical score and erase exactly the ordering this stage exists to
        produce. Generation still reads the parent, unchanged.
        """
        if not results:
            return []

        pairs = [(query, r.content) for r in results]
        scores = self.model.predict(pairs, batch_size=batch_size, show_progress_bar=False)

        rescored: List[SearchResult] = []
        for sr, score in zip(results, scores):
            copy = sr.model_copy()
            copy.similarity = float(score)
            copy.score_type = ScoreType.RERANK
            rescored.append(copy)

        rescored.sort(key=lambda r: r.similarity, reverse=True)
        logger.info(
            "Reranked %d candidates → top %d (model=%s).",
            len(results), min(top_k, len(rescored)), self.model_name,
        )
        return rescored[:top_k]


# ---------------------------------------------------------------------------
# Module-level singleton – mirrors the Searcher singleton in pipeline.py so the
# cross-encoder is loaded once per process, not once per query.
# ---------------------------------------------------------------------------

_reranker: Optional[Reranker] = None


def get_reranker() -> Reranker:
    """Return the process-wide reranker, loading it on first use."""
    global _reranker
    if _reranker is None:
        _reranker = Reranker()
    return _reranker
