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
- `chunker.py`: header-aware markdown splitting + recursive windowing.
- `classifier.py`: Gemini structured multi-label topic classification with keyword fallback and rate-limit retries.
- `embedder.py`: SentenceTransformer embeddings with optional summary-based multi-representation indexing.
- `store.py`: PostgreSQL + pgvector storage, HNSW index, metadata-filtered similarity search.
- `pipeline.py`: end-to-end indexing orchestrator.

#### Retrieval (`src/rag/retrieval/`)

- `query_analyzer.py`: structured query analysis into `single_party`, `comparison`, `topic_exploration`, `general` (+ heuristic fallback).
- `query_expander.py`: multi-query expansion.
- `searcher.py`: similarity search + Reciprocal Rank Fusion (RRF).
- `router.py`: route-specific search logic (single-party, comparison, topic, general).
- `pipeline.py`: retrieval entry point using a singleton `Searcher`.

#### Generation (`src/rag/generation/`)

- `llm_client.py`: Gemini primary, OpenRouter fallback.
- `prompts.py`: centralized Portuguese prompts.
- `synthesizer.py`: direct, comparison, and decomposition-based synthesis strategies.
- `pipeline.py`: generation entry point.

#### Shared models

- `src/rag/common/models.py` defines:
  - canonical topic list (`TOPIC_CATEGORIES`),
  - party mapping (`PARTY_MAP`),
  - all Pydantic schemas used across indexing/retrieval/generation.

### Testing status

- Existing test file: `tests/test_rag_pipeline.py`.
- Coverage currently focuses on:
  - chunking behavior,
  - keyword classifier fallback,
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

1. Formal evaluation of retrieval and answer quality.
2. Retrieval upgrades beyond current baseline (hybrid search, stronger reranking, improved query planning).
3. Better robustness/reproducibility (tests, experiment scripts, clearer dependency management).
4. Optional user-facing feature exploration (e.g., quiz-oriented interaction over manifesto positions).

## Contributor Guide for LLM Agents

### Priority when making changes

1. Preserve the modular boundary between indexing, retrieval, generation.
2. Keep configuration centralized in `config/config.yaml`.
3. Keep schemas in `common/models.py` as the single source of truth.
4. Add or update tests when behavior changes.

### Safe defaults

- Prefer fallback-safe behavior (no hard failure when one LLM provider is unavailable).
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
4. What is the offline fallback behavior when APIs are unavailable?
5. What test should prove the change is correct?

## Out of Scope for This Repository (for now)

- Full production deployment hardening.
- Long-term political timeline beyond current manifesto corpus.
- General-purpose political opinion classification outside manifesto-grounded retrieval.

## One-Line Summary

This repository is a research-focused, modular Portuguese RAG system that already performs end-to-end manifesto QA and is now moving toward stronger retrieval quality, rigorous evaluation, and more robust experimentation.
