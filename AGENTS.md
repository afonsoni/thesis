# AGENTS.md

## Purpose

This repository contains a modular Retrieval-Augmented Generation (RAG) system for analyzing Portuguese political party manifestos from the 2024 legislative elections.

The project goal is to help users ask questions about party proposals and receive grounded answers with source context.

This file is written for coding agents and LLM contributors so they can quickly understand:

1. What currently exists and works.
2. What is still experimental or incomplete.
3. Where the project is headed for the dissertation.

## Current Reality (Verified in Repository)

### Data currently present

- Raw PDFs: `data/0_raw/` contains 8 manifesto files (`ad`, `be`, `chega`, `il`, `livre`, `pan`, `pcp`, `ps`).
- Markdown corpus: `data/1_markdown/` has party subfolders for all 8 parties.
- Manual markdown variants currently exist for: `ad`, `livre`, `pcp`, `ps`.
- Processed outputs: `data/2_processed/` currently includes `livre-2024-classified.json`.

### Implemented CLI

Entry point: `main.py`

- `parse`: PDF -> markdown using `marker_single`.
- `index`: chunk -> classify -> (optional summaries) -> embed -> store.
- `query`: retrieve -> generate final answer.

### Implemented architecture

#### Indexing (`src/rag/indexing/`)

- `parser.py`: wraps `marker_single` subprocess and removes generated images.
- `chunker.py`: header-aware markdown splitting + recursive windowing. Windowing is
  sized in **tokens** (via the embedding model's own tokenizer) under the `token` /
  `small_to_big` strategies; `char` is the legacy character-sized baseline retained
  only for ablations. See `indexing.chunk_strategy` and the README — sizing in
  characters overran `serafim-900m`'s 128-token window and silently truncated ~89%
  of chunks (62.7% of the corpus never embedded), which is why the encoder was
  replaced by `Qwen/Qwen3-Embedding-0.6B` (32k window). The serafim variant used
  was the retrieval-tuned `...-sentence-encoder-ir`, so the reason for the swap
  is the window, not the training task. Do not cite MTEB-PT's serafim scores
  (STS 86.7 / retrieval 54.9) for it: they are for the general sentence encoder.
  Under `small_to_big`, a child's `parent_content` (what generation reads) is its
  header section, capped at `indexing.max_parent_tokens`: an oversized section
  gives each child a window of its neighbours instead. `scripts/rebuild_parents.py`
  re-chunks and carries topics over from the classified checkpoints by content
  hash, so parent-only changes need no reclassification.
- `classifier.py`: OpenRouter-based structured multi-label topic classification with rate-limit retries.
- `embedder.py`: SentenceTransformer embeddings with optional summary-based multi-representation
  indexing. Handles asymmetric retrieval models: use `encode_query()` at search time so the
  model's query instruction prefix is applied, and `encode()`/`encode_batch()` for documents.
  Left padding is set automatically for last-token-pooling (decoder) encoders, matching
  Qwen3-Embedding's model card. This is defensive, not load-bearing: sentence-transformers
  5.x locates the last *unmasked* token via the attention mask, so it pools correctly with
  either padding side. Do not cite it as a correctness requirement.
- `store.py`: PostgreSQL + pgvector storage, HNSW index, metadata-filtered similarity
  search, plus `lexical_search()`: BM25 (`bm25.py`) over the lexemes of a generated
  Portuguese `tsvector` column (the lexical half of hybrid retrieval). Any query term
  can match and rare terms weigh more; `websearch_to_tsquery`/`ts_rank_cd`, used
  before, ANDed every word and so matched almost nothing for a natural question.
  Lexemes are accent-folded after stemming (so "saude" finds "saúde"), and a
  party-filtered lexical query drops party names (`strip_party_mentions`), which
  otherwise outweigh the topic as rare BM25 terms.
- `pipeline.py`: end-to-end indexing orchestrator.

#### Retrieval (`src/rag/retrieval/`)

- `query_analyzer.py`: structured query analysis into `single_party`, `comparison`, `topic_exploration`, `general` (+ heuristic fallback).
- `query_expander.py`: multi-query expansion.
- `searcher.py`: similarity search + Reciprocal Rank Fusion (RRF). With
  `use_hybrid`, each query also contributes a lexical ranked list and all
  `2 * len(queries)` lists are fused in a single RRF pass. With `use_reranker`,
  each sub-query fetches `rerank_candidates` instead of `top_k` and the fused
  shortlist goes through the cross-encoder before the trim.
- `reranker.py`: cross-encoder precision pass (`Reranker`, process-wide singleton
  via `get_reranker()`). Scores the *original question* against each chunk's
  `content` (not `parent_content`: small-to-big siblings share a parent, so
  scoring it would tie them). Results carry `ScoreType.RERANK` — raw logits, not
  comparable to cosine/RRF. Model-load failures raise rather than degrade to
  un-reranked results, so a `reranked` run cannot silently report baseline numbers.
- `router.py`: route-specific search logic (single-party, comparison, topic, general).
- `pipeline.py`: retrieval entry point using a singleton `Searcher`.

#### Generation (`src/rag/generation/`)

- `llm_client.py`: unified OpenRouter transport for text + structured outputs.
- `prompts.py`: centralized Portuguese prompts.
- `synthesizer.py`: direct, comparison, and decomposition-based synthesis strategies.
- `pipeline.py`: generation entry point.

#### Shared models

- `src/rag/common/models.py` defines:
  - canonical topic list (`TOPIC_CATEGORIES`),
  - party mapping (`PARTY_MAP`),
  - all Pydantic schemas used across indexing/retrieval/generation.

#### Evaluation (`src/rag/evaluation/`)

- `variants.py`: the declarative ladder of implementation steps as `RetrievalConfig`
  presets (`naive`, `multiquery`, `routed`, `current`, `hybrid`, `hybrid_only`,
  `reranked`, `reranked_only`), plus three dense-retrieval ablations one flag away
  from `current`: `party_stripped` (`strip_party_names`), `instructed`
  (`query_instruction` = `embeddings.task_instruction`) and `contextual` (searches
  `indexing.contextual_table`, built with `main.py index --contextual-headers --table`).
- `dataset.py`: gold-set load/save (content-hash keys).
- `metrics/`: retrieval (hit/recall/MRR/nDCG over the full list handed to generation,
  against human-picked gold chunks),
  routing (type acc, coverage, party/topic F1), and generation: claim-level
  faithfulness and correctness (RAGAS-style, `judge.py`) plus a 1-5 relevance judge
  whose `abstained` flag gives `abstention` (on `answerable: false` questions) and
  `false_refusal` (on the rest),
  behind a `Metric` protocol. `stats.py` adds bootstrap CIs and paired differences to
  the leaderboard; `scripts/judge_validation.py` measures judge-human agreement.
- Gold set: `data/eval/questions/CANDIDATES.md` -> `scripts/anchor_gold.py` ->
  `anchoring/ANCHORING.md` (human review, `reviewed: yes`) -> `golden.json`, with a
  `dev`/`test` split (`eval --split test` for headline numbers).
- `runner.py` / `report.py` / `pipeline.py`: run a variant, persist results, refresh
  `data/eval/reports/leaderboard.md`.
- Retrieval is now feature-flagged via `src/rag/retrieval/config.py::RetrievalConfig`;
  `RetrievalConfig()` defaults reproduce the historical behavior, so `retrieve()` is
  backward-compatible. See `docs/evaluation.md`.

### Testing status

- Existing test file: `tests/test_rag_pipeline.py`.
- Coverage currently focuses on:
  - chunking behavior,
  - classifier batching and fail-fast behavior,
  - model defaults,
  - RRF utility,
  - fallback query analysis.
- There is no comprehensive integration test suite for live DB + live LLM flows yet.

### Infrastructure and config

- Docker setup: `docker-compose.yml` runs PostgreSQL 17 + pgvector.
- Config source: `config/config.yaml` (paths, retrieval settings, models, DB settings).
- Config loader: `src/utils/config_loader.py` singleton.
- No dependency lockfile or `requirements.txt` currently tracked in repo.

## What This Project Is (For Agents)

This is an academic RAG prototype with production-style modularity, not yet a finished product.

The key research idea is to improve question-answering over political manifestos by combining:

1. Better retrieval (multi-query + routing + metadata filters + RRF), and
2. Grounded generation (prompted synthesis with context and source metadata).

Primary language is Portuguese (pt-PT), and outputs should remain in Portuguese unless explicitly requested otherwise.

## What Is Stable vs Experimental

### Relatively stable

- Command structure in `main.py`.
- 3-stage pipeline separation (indexing/retrieval/generation).
- Party/topic metadata schema in `common/models.py`.
- PostgreSQL + pgvector storage backend.

### Experimental / evolving

- Prompt quality and synthesis strategy selection.
- Topic classification quality under API/rate-limit constraints.
- Chunk-size choices and retrieval tuning.
- Evaluation methodology and benchmark automation.
- Processed-data artifacts in `data/2_processed/`.

## Project Direction (Where It Is Headed)

Based on the dissertation draft and repository structure, near-term direction is:

1. Formal evaluation of retrieval and answer quality. **(In progress — the evaluation
   harness now exists in `src/rag/evaluation/`; next is curating `golden.json` and
   running the variant ladder to produce headline numbers.)**
2. Retrieval upgrades beyond current baseline. Hybrid search and cross-encoder
   reranking are **implemented** (`use_hybrid`, `use_reranker`, with `hybrid`,
   `hybrid_only`, `reranked`, `reranked_only` on the ladder); both still need
   leaderboard numbers over a curated gold set to earn their place. Improved
   query planning remains open.
3. Better robustness/reproducibility (tests, experiment scripts, clearer dependency management).
4. Optional user-facing feature exploration (e.g., quiz-oriented interaction over manifesto positions).

## Contributor Guide for LLM Agents

### Priority when making changes

1. Preserve the modular boundary between indexing, retrieval, generation.
2. Keep configuration centralized in `config/config.yaml`.
3. Keep schemas in `common/models.py` as the single source of truth.
4. Add or update tests when behavior changes.

### Safe defaults

- Prefer fallback-safe behavior where appropriate (retrieval/generation paths); indexing classification is intentionally fail-fast.
- Preserve source transparency in generated answers.
- Avoid introducing party bias in prompts or transformations.

### If you change these, also update related parts

- `TOPIC_CATEGORIES` -> update classifier logic/tests and prompt assumptions.
- `PARTY_MAP` -> update routing assumptions/tests and dataset expectations.
- retrieval strategy -> verify synthesis still handles grouped/flat results correctly.

## Typical Local Workflow

1. Start DB:
   - `docker compose up -d`
2. Parse PDFs:
   - `python main.py parse --input-dir data/0_raw --output-dir data/1_markdown`
3. Index documents:
   - `python main.py index --all`
4. Query system:
   - `python main.py query "Quais são as propostas do PS para a educação?"`

## Decision Checklist for Future Work

Before implementing a new feature, decide:

1. Is this for retrieval quality, generation quality, or evaluation quality?
2. Does it require schema changes in `common/models.py`?
3. Does it require new config keys in `config/config.yaml`?
4. What is the expected fail-fast behavior when APIs are unavailable?
5. What test should prove the change is correct?

## Out of Scope for This Repository (for now)

- Full production deployment hardening.
- Long-term political timeline beyond current manifesto corpus.
- General-purpose political opinion classification outside manifesto-grounded retrieval.

## One-Line Summary

This repository is a research-focused, modular Portuguese RAG system that already performs end-to-end manifesto QA and is now moving toward stronger retrieval quality, rigorous evaluation, and more robust experimentation.
