"""
The declarative ladder of RAG implementation steps.

Each entry is a ``RetrievalConfig`` preset. Running the harness over several
variants isolates the contribution of each feature (multi-query, RRF, routing,
…) because they all flow through the *same* production code paths — only the
flags differ.

This registry is the canonical, in-repo list of "implementation steps"; add a
new rung here (and, for reranker/hybrid, implement the flag in the searcher) to
put a future upgrade on the leaderboard.
"""

from __future__ import annotations

from typing import Dict, List

from src.rag.retrieval.config import RetrievalConfig
from src.utils.config_loader import config

VARIANTS: Dict[str, RetrievalConfig] = {
    # Rung 0 – naive RAG: single query → single similarity search → direct answer.
    "naive": RetrievalConfig(
        name="naive",
        use_query_analysis=False,
        use_routing=False,
        use_multi_query=False,
        use_hybrid=False,
    ),
    # Rung 1 – add multi-query expansion + RRF fusion (Parts 5 & 6), still no routing.
    "multiquery": RetrievalConfig(
        name="multiquery",
        use_query_analysis=False,
        use_routing=False,
        use_multi_query=True,
        use_hybrid=False,
    ),
    # Rung 2 – add structured query analysis + logical routing (Part 10), single query.
    "routed": RetrievalConfig(
        name="routed",
        use_query_analysis=True,
        use_routing=True,
        use_multi_query=False,
        use_hybrid=False,
    ),
    # Rung 3 – analysis + routing + multi-query + RRF, over dense retrieval only.
    "dense_only": RetrievalConfig(name="dense_only", use_hybrid=False),
    # Rung 4 – the current production system: rung 3 plus the lexical half (BM25
    # fused by the same RRF pass), the default since it raised dev nDCG by 0.064.
    "current": RetrievalConfig(name="current"),
    # Isolates hybrid's contribution against `naive`, holding expansion/routing off
    # so the only difference from rung 0 is the added lexical retrieval.
    "hybrid_only": RetrievalConfig(
        name="hybrid_only",
        use_query_analysis=False,
        use_routing=False,
        use_multi_query=False,
        use_hybrid=True,
    ),

    # Rung 5 – add the cross-encoder precision pass on top of the full pipeline.
    # Differs from `current` by exactly one flag, so the delta is the reranker's.
    "reranked": RetrievalConfig(name="reranked", use_reranker=True),
    # Isolates reranking against `naive`, the same way `hybrid_only` isolates the
    # lexical half: no expansion, no routing, so the only addition is the
    # cross-encoder re-ordering a wide single-query candidate set.
    "reranked_only": RetrievalConfig(
        name="reranked_only",
        use_query_analysis=False,
        use_routing=False,
        use_multi_query=False,
        use_hybrid=False,
        use_reranker=True,
    ),

    # Dense-retrieval ablations (dissertation/DECISIONS.md, 2026-10-09), each one
    # flag away from `current`. Run on the dev split before any becomes a default.
    "party_stripped": RetrievalConfig(name="party_stripped", strip_party_names=True),
    "no_topic_filter": RetrievalConfig(name="no_topic_filter", use_topic_filter=False),
    "instructed": RetrievalConfig(
        name="instructed", query_instruction=config.get("embeddings.task_instruction"),
    ),
    # Needs the index built first:
    #   main.py index --from-classified <ckpt> --contextual-headers --table <indexing.contextual_table>
    "contextual": RetrievalConfig(name="contextual", table=config.get("indexing.contextual_table")),
}


def get_variant(name: str) -> RetrievalConfig:
    """Look up a variant preset by name (raises KeyError with a helpful message)."""
    try:
        return VARIANTS[name]
    except KeyError:
        raise KeyError(
            f"Unknown variant '{name}'. Available: {', '.join(sorted(VARIANTS))}"
        )


def resolve_variants(names: List[str]) -> List[RetrievalConfig]:
    """Resolve a list of variant names to their configs, preserving order."""
    return [get_variant(n) for n in names]
