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

from typing import Optional

from pydantic import BaseModel, Field

from src.utils.config_loader import config


def _from_config(key: str):
    """Default read from ``retrieval.<key>`` in config.yaml at construction time."""
    return lambda: int(config.get(f"retrieval.{key}"))


class RetrievalConfig(BaseModel):
    """Declarative switches for the retrieval pipeline.

    Defaults are the production (``current``) behaviour; sizes come from the
    ``retrieval`` section of config.yaml.
    """

    name: str = Field(default="current", description="Human-readable variant name.")
    use_retrieval: bool = Field(
        default=True,
        description="False is the closed-book baseline: no analysis, no search, and "
        "generation answers from the model's own knowledge. What RQ5 compares "
        "retrieval against; retrieval and routing metrics do not apply to it.",
    )
    generation_model: Optional[str] = Field(
        default=None,
        description="Model that writes the answer. None is llm.openrouter.model; set "
        "per variant to put a stronger model on the ladder, with or without retrieval.",
    )
    web_search: bool = Field(
        default=False,
        description="Let the generator search the web (OpenRouter web plugin, the "
        "provider's own search where it has one). With use_retrieval=False this is "
        "the 'regular assistant' baseline: what a citizen gets from ChatGPT, Gemini "
        "or Claude today, corpus unseen but the web open.",
    )

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
        default_factory=_from_config("multi_query_count"),
        ge=1,
        description="Number of expanded queries (excludes the original).",
    )

    # Reciprocal Rank Fusion (Part 6): applied whenever a search yields more than
    # one ranked list (multi-query and/or hybrid).
    rrf_k: int = Field(default_factory=_from_config("rrf_k"), ge=1, description="RRF constant.")

    # Hybrid retrieval – dense + Portuguese full-text, fused by the same RRF pass
    use_hybrid: bool = Field(
        default=True,
        description="Also retrieve a Portuguese BM25 ranked list per query and fuse "
        "it with the dense lists. Recovers rare exact tokens (acronyms, programme "
        "names) that dense embeddings under-weight. On by default since it raised "
        "dev nDCG by 0.064 over dense-only retrieval.",
    )

    # Cross-encoder reranking – precision pass over a wide candidate set
    use_reranker: bool = Field(
        default=False,
        description="Re-order retrieved candidates with a cross-encoder and keep "
        "the best top_k. Retrieval fetches rerank_candidates results first, so "
        "the reranker has more to choose from than the caller asked for.",
    )
    rerank_candidates: int = Field(
        default_factory=_from_config("rerank_candidates"),
        ge=1,
        description="Candidates fetched and scored before reranking trims to top_k. "
        "Reranking can only promote what retrieval surfaced, so this is the real "
        "recall ceiling of the reranked variant.",
    )

    # Failure handling
    strict: bool = Field(
        default=False,
        description="Raise when an LLM step (query analysis, expansion) fails instead "
        "of falling back to its degraded mode. The evaluation harness sets it, so a "
        "rate-limited question is recorded as an error rather than scored as a "
        "cheaper pipeline under this variant's name.",
    )

    use_topic_filter: bool = Field(
        default=False,
        description="Restrict searches to chunks sharing an analyzed topic (never "
        "the catch-all 'outros'). Off by default: 9% of gold chunks carry none of "
        "the analyzer's topics, and on the contextual index the filter cost recall "
        "(-0.028 retrieval-only, 61 questions); the contexts carry the topic words.",
    )
    lexical_topic_filter: bool = Field(
        default=True,
        description="Apply the topic filter to the lexical list too. Off, only dense "
        "search is topic-filtered: a rare exact term is precise on its own, and an "
        "incidental mention sits in a chunk classified under another topic.",
    )
    expansion_synonyms: bool = Field(
        default=False,
        description="Ask multi-query expansion to swap the question's key words for "
        "the synonyms and formal terms a manifesto would use, so the lexical lists "
        "can match wording the user did not type.",
    )
    table: Optional[str] = Field(
        default=None,
        description="Index table to search. None is postgresql.table_name; the "
        "contextual-headers index lives in indexing.contextual_table.",
    )

    # Result sizing
    max_prompt_tokens: Optional[int] = Field(
        default=None,
        ge=1,
        description="Context budget generation may fill from these results (lowest-ranked "
        "trimmed first, never a whole party). None is llm.openrouter.max_prompt_tokens; "
        "set per variant so retrieving more can be measured with room to read it.",
    )
    top_k: int = Field(
        default_factory=_from_config("default_top_k"), ge=1, description="Results returned to generation."
    )
    top_k_per_party: int = Field(
        default_factory=_from_config("top_k_per_party"),
        ge=1,
        description="Per-party results for comparison and topic-exploration queries.",
    )
