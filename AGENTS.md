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
  replaced by `Qwen/Qwen3-Embedding-0.6B` (32k window, retrieval-trained).
- `classifier.py`: OpenRouter-based structured multi-label topic classification with rate-limit retries.
- `embedder.py`: SentenceTransformer embeddings with optional summary-based multi-representation
  indexing. Handles asymmetric retrieval models: use `encode_query()` at search time so the
  model's query instruction prefix is applied, and `encode()`/`encode_batch()` for documents.
  Left padding is set automatically for last-token-pooling (decoder) encoders — getting that
  wrong silently corrupts every batched embedding.
- `store.py`: PostgreSQL + pgvector storage, HNSW index, metadata-filtered similarity
  search, plus `lexical_search()` over a generated Portuguese `tsvector` column
  (the lexical half of hybrid retrieval).
- `pipeline.py`: end-to-end indexing orchestrator.

#### Retrieval (`src/rag/retrieval/`)

- `query_analyzer.py`: structured query analysis into `single_party`, `comparison`, `topic_exploration`, `general` (+ heuristic fallback).
- `query_expander.py`: multi-query expansion.
- `searcher.py`: similarity search + Reciprocal Rank Fusion (RRF). With
  `use_hybrid`, each query also contributes a lexical ranked list and all
  `2 * len(queries)` lists are fused in a single RRF pass.
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
  presets (`naive`, `multiquery`, `routed`, `current`; reserved `reranked`/`hybrid`).
- `dataset.py`: synthetic-anchored gold-set generation + load/save (content-hash keys).
- `metrics/`: retrieval (hit@k/recall@k/MRR/nDCG), routing (type acc, party/topic F1),
  and LLM-judge generation (faithfulness/relevance/correctness) behind a `Metric` protocol.
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
2. Retrieval upgrades beyond current baseline (hybrid search, stronger reranking, improved query planning).
   The `use_reranker`/`use_hybrid` flags and `VARIANTS` slots are reserved for exactly this.
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
