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

# The index before contextual retrieval: the rungs below `current` search it, so
# each rung still adds exactly one technique.
PLAIN = config.get("indexing.plain_table")

VARIANTS: Dict[str, RetrievalConfig] = {
    # Rung 0 – naive RAG: single query → single similarity search → direct answer.
    "naive": RetrievalConfig(
        name="naive",
        table=PLAIN,
        use_query_analysis=False,
        use_routing=False,
        use_multi_query=False,
        use_hybrid=False,
    ),
    # Rung 1 – add multi-query expansion + RRF fusion (Parts 5 & 6), still no routing.
    "multiquery": RetrievalConfig(
        name="multiquery",
        table=PLAIN,
        use_query_analysis=False,
        use_routing=False,
        use_multi_query=True,
        use_hybrid=False,
    ),
    # Rung 2 – add structured query analysis + logical routing (Part 10), single query.
    "routed": RetrievalConfig(
        name="routed",
        table=PLAIN,
        use_query_analysis=True,
        use_routing=True,
        use_multi_query=False,
        use_hybrid=False,
    ),
    # Rung 3 – analysis + routing + multi-query + RRF, over dense retrieval only.
    "dense_only": RetrievalConfig(name="dense_only", use_hybrid=False, table=PLAIN),
    # Rung 4 – plus the lexical half (BM25 fused by the same RRF pass): dev nDCG
    # +0.064 over dense-only.
    "hybrid": RetrievalConfig(name="hybrid", table=PLAIN),
    # Rung 5 – the current production system: rung 4 over the contextual index,
    # each chunk embedded and BM25-indexed with its headers and an LLM-written
    # context (61 questions, two passes: recall +0.046, nDCG +0.057 over rung 4).
    "current": RetrievalConfig(name="current"),
    # Isolates hybrid's contribution against `naive`, holding expansion/routing off
    # so the only difference from rung 0 is the added lexical retrieval.
    "hybrid_only": RetrievalConfig(
        name="hybrid_only",
        table=PLAIN,
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
        table=PLAIN,
        use_query_analysis=False,
        use_routing=False,
        use_multi_query=False,
        use_hybrid=False,
        use_reranker=True,
    ),

    # Dense-retrieval ablations (dissertation/DECISIONS.md, 2026-10-09), each one
    # flag away from `current`. Run on the dev split before any becomes a default.
    "party_stripped": RetrievalConfig(name="party_stripped", strip_party_names=True),
    # `current` before it went deeper without the topic filter (results `wide*` of
    # 2026-10-13, judged on all 61 questions): 5 per search and per party, topics
    # filtering. `current` beat it by recall +0.123, correctness +0.041 and
    # correctness recall +0.102, faithfulness within noise.
    "shallow": RetrievalConfig(name="shallow", top_k=5, top_k_per_party=5, use_topic_filter=True),
    # One flag each: the topic filter back on (retrieval only: recall -0.028 at 5/5),
    # and a 64k prompt budget, which read no better than 32k (correctness +0.029
    # vs current's +0.041 over `shallow`) for 18% more input tokens.
    "topic_filter": RetrievalConfig(name="topic_filter", use_topic_filter=True),
    "budget_64k": RetrievalConfig(name="budget_64k", max_prompt_tokens=64000),
    # Vocabulary-mismatch fix for incidental mentions (gold q-61): the lexical
    # list skips the topic filter and expansions use manifesto wording. Two flags
    # from `current`, measured together. Dev 2026-10-11: no metric moved beyond
    # noise (recall +0.011, nDCG +0.008) and q-61 stayed unretrieved, so both
    # flags stay off. With the topic filter now off by default, only the
    # expansion flag still changes anything.
    "lexical_wide": RetrievalConfig(name="lexical_wide", lexical_topic_filter=False, expansion_synonyms=True),
    "instructed": RetrievalConfig(
        name="instructed", query_instruction=config.get("embeddings.task_instruction"),
    ),
    # Headers without the LLM context, i.e. half of `current`'s contextual index:
    # recall +0.026 over `hybrid`, against +0.046 with the context. Needs:
    #   main.py index --from-classified <ckpt> --no-llm-context --table <indexing.contextual_table>
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
