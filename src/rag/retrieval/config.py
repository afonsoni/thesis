"""
Retrieval configuration – feature flags that make each RAG "implementation step"
a declarative variant.

The default ``RetrievalConfig()`` reproduces the *current* production behavior
exactly (query analysis → routing → multi-query expansion → RRF). Turning flags
off degrades the pipeline down towards a naive baseline, which is what lets the
evaluation harness compare implementation steps apples-to-apples over the same
dataset and the same code paths.

See ``src/rag/evaluation/variants.py`` for the named preset ladder.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class RetrievalConfig(BaseModel):
    """Declarative switches for the retrieval pipeline.

    Defaults intentionally mirror the historical hard-coded behavior so that
    ``retrieve(question)`` with no config behaves identically to before.
    """

    name: str = Field(default="current", description="Human-readable variant name.")

    # Query understanding
    use_query_analysis: bool = Field(
        default=True,
        description="Run the structured LLM query analysis. When False the query "
        "is treated as GENERAL with no party/topic/ideology extraction.",
    )
    use_routing: bool = Field(
        default=True,
        description="Dispatch to type-specific search strategies. When False every "
        "query goes through the broad GENERAL route.",
    )

    # Multi-query expansion (Part 5)
    use_multi_query: bool = Field(
        default=True,
        description="Expand the query into multiple reformulations before search.",
    )
    multi_query_count: int = Field(
        default=4, ge=1, description="Number of expanded queries (excludes the original)."
    )

    # Reciprocal Rank Fusion (Part 6)
    use_rrf: bool = Field(
        default=True,
        description="Fuse multi-query result lists with RRF. When False, results are "
        "merged by first-occurrence order instead.",
    )
    rrf_k: int = Field(default=60, ge=1, description="RRF constant.")

    # Hybrid retrieval – dense + Portuguese full-text, fused by the same RRF pass
    use_hybrid: bool = Field(
        default=False,
        description="Also retrieve a PostgreSQL full-text ranked list per query and "
        "fuse it with the dense lists. Recovers rare exact tokens (acronyms, "
        "programme names) that dense embeddings under-weight.",
    )

    # Future rungs – flags reserved so the implementations drop in later.
    use_reranker: bool = Field(
        default=False, description="Apply a cross-encoder reranker (not yet implemented)."
    )

    # Result sizing
    top_k: int = Field(default=5, ge=1, description="Results returned to generation.")
    top_k_per_party: int = Field(
        default=3, ge=1, description="Per-party results for comparison queries."
    )
