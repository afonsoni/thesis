# System Architecture

This document explains how the RAG system works, stage by stage, with Mermaid
diagrams. The system has three parts:

1. **Indexing** (offline) — turns the manifesto PDFs into a searchable vector store.
2. **Query time** (online) — answers a user question with grounded citations.
3. **Evaluation** (offline) — replays the *same* retrieval code as a ladder of
  feature-flagged variants to measure what each technique contributes.

Each retrieval/generation technique maps to a specific method from the
*RAG-from-Scratch* series (noted as "Part N" below).

The diagrams are also the dissertation's figures:
`[scripts/render_diagrams.sh](../scripts/render_diagrams.sh)` renders every
block below, in order, to `dissertation/images/architecture-*.pdf`. Keep the
labels conceptual (code links go in the prose) and re-run the script after
editing a diagram.

---



## 1. Overview

```mermaid
flowchart LR
    subgraph IDX["Indexing"]
        direction TB
        I1[/"Manifesto PDFs"/] --> I2["Parsing"] --> I3["Cleaning"] --> I4["Chunking"] --> I5["Topic classification"] --> I6["Embedding"]
    end

    VS[("Vector store<br/>PostgreSQL + pgvector")]

    subgraph QT["Retrieval"]
        direction TB
        Q1(["Question"]) --> Q2["Query analysis"] --> Q3["Multi-query expansion"] --> Q4["Routing"] --> Q5["Search and fusion"] --> Q6["Answer synthesis"] --> Q7(["Answer + sources"])
    end

    subgraph EV["Evaluation"]
        direction TB
        E1[/"Gold set"/] --> E2["Variant ladder"] --> E3["Metrics"] --> E4[/"Leaderboard"/]
    end

    IDX --> VS --> QT
    QT -.-> EV
```



The dotted arrow into evaluation means the harness reuses the production
retrieval code and the same vector store — variants differ only by feature
flags, so score differences isolate the contribution of one technique.

---



## 2. Indexing pipeline

`PDF → Markdown → clean → chunk → classify → embed → store`. Parsing and
cleaning are separate commands (`main.py parse`, `main.py clean`); the rest is
orchestrated by `[indexing/pipeline.py](../src/rag/indexing/pipeline.py)`.

```mermaid
flowchart TD
    subgraph PREP["Document preparation"]
        direction LR
        PDF[/"8 manifesto PDFs"/] --> PARSE["<b>Parsing</b><br/>Marker<br/>PDF to Markdown"] --> CLEAN["<b>Cleaning</b><br/>layout residue, heading tree<br/>by hand, or LLM + review"]
    end

    subgraph IDX["Indexing pipeline"]
        direction LR
        CHUNK["<b>Chunking</b><br/>split on headings<br/>400-token windows<br/>parents ≤ 1,500 tokens"] --> CLS["<b>Topic classification</b><br/>LLM, structured output<br/>18 topics, ≤ 3 per chunk<br/>checkpointed to JSON"] --> EMB["<b>Embedding</b><br/>Qwen3-Embedding-0.6B<br/>1,024 dimensions"]
    end

    VS[("<b>Vector store</b><br/>PostgreSQL 17 + pgvector<br/>HNSW on cosine, GIN on topics,<br/>Portuguese full-text column")]

    PREP --> IDX --> VS
```



- **Parse** — `[parser.py](../src/rag/indexing/parser.py)` wraps the `marker_single` CLI; raw output goes to `data/1_markdown/_raw/`.
- **Clean** — `[cleaner.py](../src/rag/indexing/cleaner.py)` runs a deterministic residue pass, then an LLM pass that may only keep, demote or drop heading candidates (any output word absent from the input is rejected). AD, LIVRE, PCP and PS were corrected by hand instead.
- **Chunk** — `[chunker.py](../src/rag/indexing/chunker.py)` splits on headings, then windows recursively in tokens of the embedding model's own tokenizer (`small_to_big`). The window is embedded; its parent section (capped at `indexing.max_parent_tokens`) is what generation reads.
- **Classify** — `[classifier.py](../src/rag/indexing/classifier.py)` assigns topics via a structured LLM call, fail-fast. Results are checkpointed to `data/2_processed/*-classified.json` (`--classify-only`), so re-indexing from them (`--from-classified`) spends no classification tokens.
- **Embed** — `[embedder.py](../src/rag/indexing/embedder.py)` uses `Qwen/Qwen3-Embedding-0.6B` (32k-token window); queries get the model's instruction prefix, documents do not. Optional summary-based multi-representation (Part 12) exists but is off.
- **Store** — `[store.py](../src/rag/indexing/store.py)` writes vectors + metadata to pgvector: HNSW for similarity, GIN on the topic array for filters (Part 11), and a generated Portuguese `tsvector` whose lexemes [`bm25.py`](../src/rag/indexing/bm25.py) ranks for lexical search.

---



## 3. Retrieval pipeline

`analyze → expand → route → search → fuse → rerank`. Entry point:
`[retrieval/pipeline.py](../src/rag/retrieval/pipeline.py)`. Dashed stages are
gated by a flag on `[RetrievalConfig](../src/rag/retrieval/config.py)` (named
in brackets), which is how a single code path can act as any rung of the
variant ladder.

```mermaid
flowchart TD
    Q(["Question (pt-PT)"])
    AN["<b>Query analysis</b> [use_query_analysis]<br/>LLM, structured output: parties, coverage, topics,<br/>answer shape and a reformulated query"]
    EX["<b>Multi-query expansion</b> [use_multi_query]<br/>reformulated query + 4 rewrites"]
    RT["<b>Routing</b> [use_routing]<br/>query type derived from parties and coverage"]
    SP["<b>Single party</b><br/>one party named<br/>party filter"]
    CMP["<b>Comparison</b><br/>two or more, or every party<br/>one search per party"]
    TOP["<b>Topic exploration</b><br/>no party, topics only<br/>topic filter"]
    GEN["<b>General</b><br/>anything else<br/>no filter"]
    SE["<b>Search</b>, for every query<br/>dense: pgvector cosine similarity<br/>+ lexical: BM25 on Portuguese lexemes [use_hybrid]"]
    FU["<b>Fusion</b> [use_rrf]<br/>Reciprocal Rank Fusion, k = 60"]
    RR["<b>Reranking</b> [use_reranker]<br/>cross-encoder over 30 candidates"]
    OUT(["Top-5 chunks, or top-3 per party"])

    Q --> AN --> EX --> RT
    RT --> SP & CMP & TOP & GEN
    SP & CMP & TOP & GEN --> SE
    SE --> FU --> RR --> OUT

    classDef flag stroke-dasharray: 5 4
    class AN,EX,RT,FU,RR flag
```



Routing logic lives in `[router.py](../src/rag/retrieval/router.py)`; the
similarity search, lexical search and RRF live in
`[searcher.py](../src/rag/retrieval/searcher.py)`; the cross-encoder pass lives
in `[reranker.py](../src/rag/retrieval/reranker.py)`.

With a flag off, each stage degrades instead of disappearing:


| Flag off             | Behaviour                                                       |
| -------------------- | --------------------------------------------------------------- |
| `use_query_analysis` | no LLM call; question treated as GENERAL (no parties or topics) |
| `use_multi_query`    | one query: the reformulated question                            |
| `use_routing`        | every query takes the GENERAL route                             |
| `use_hybrid`         | dense lists only (`dense_only` and the first three rungs)       |
| `use_rrf`            | lists merged by first occurrence                                |
| `use_reranker`       | fused list trimmed straight to `top_k` (the default)            |


Details the diagram compresses:

- **Query analysis fallback.** If the LLM call fails, an exact party-alias scan
sets the parties and coverage falls to *exhaustive*, so the router fans out
rather than silently omitting parties.
- **Topic filters are a preference.** Single-party and comparison searches also
apply the analysed topics. Any topic-filtered search that matches nothing is
retried without the filter (per party, for comparisons).
- **Comparison** searches every named party, or all eight when the question
asks for exhaustive coverage without naming any.
- **Hybrid** adds a lexical list per query, so `2 × len(queries)` lists are
fused in one RRF pass.
- **Reranking** widens before it narrows: each sub-query retrieves
`rerank_candidates` (default 30) rather than `top_k`, and the cross-encoder
scores the *original* question against each chunk before the trim. A
reranker can only promote what retrieval surfaced, so the wide fetch is what
gives it room to work.

---



## 4. Generation (answer synthesis)

The synthesizer prepares the context, then picks a strategy from the requested
`answer_shape` and the result shape, and answers with source citations.
`[synthesizer.py](../src/rag/generation/synthesizer.py)`.

```mermaid
flowchart TD
    IN(["Retrieved chunks"])
    CTX["<b>Context preparation</b><br/>expand chunks to parent sections, deduplicate<br/>trim lowest-ranked to an 8,000-token budget,<br/>never dropping a whole party"]
    D{"Answer<br/>shape"}
    CMP["<b>Comparison</b><br/>per party, grouped results<br/>one context block per party"]
    DEC["<b>Decomposition</b><br/>per party, flat results<br/>sub-questions, then synthesis"]
    DIR["<b>Direct</b><br/>narrative<br/>single pass over the context"]
    OUT(["Answer (pt-PT) + source citations"])

    IN --> CTX --> D
    D --> CMP & DEC & DIR
    CMP & DEC & DIR --> OUT
```



Shape rather than route, because the two cross: *"que partido propõe mais sobre
habitação?"* needs every party retrieved but answered as one verdict. A
narrative answer over a fan-out reads the whole grouped set rather than
`RetrievalResult.results`, which the router truncates to `top_k`. Decomposition
(Part 7) is kept for the one case it addresses: a per-party question whose
results arrived flat.

Context size is bounded by `llm.openrouter.max_prompt_tokens` rather than by a
result count. Retrieval can hand generation `top_k_per_party` × 8 parties, so
over-budget contexts are trimmed lowest-ranked first, and a grouped context is
trimmed from whichever party contributes most so that no party is dropped
outright. Citations follow the trimmed context — a source the model never read
is one it cannot have used. An empty retrieval returns a fixed "no documents
found" reply without calling the LLM.

---



## 5. Evaluation harness

The harness measures each **implementation step** on the same gold set. Because
every variant runs the production retrieval code with only different flags, a
score delta is attributable to one technique. Code:
`[src/rag/evaluation/](../src/rag/evaluation/)`; methodology:
`[evaluation.md](evaluation.md)`.

```mermaid
flowchart TD
    subgraph GS["Gold set construction"]
        direction LR
        C["<b>Questions</b><br/>hand-drafted,<br/>checked in corpus"] --> A["<b>Anchoring</b><br/>dense + lexical<br/>candidate chunks"] --> R["<b>Human review</b><br/>gold chunks and<br/>reference answers"]
    end

    G[/"<b>Gold set</b><br/>dev / test split"/]

    RUN["<b>Variant ladder</b><br/>every variant over every question<br/>same code, feature flags differ"]
    MR["<b>Retrieval</b><br/>hit@k, recall@k,<br/>MRR, nDCG@k"]
    MO["<b>Routing</b><br/>query-type and coverage<br/>accuracy, party/topic F1"]
    MG["<b>Generation</b>, LLM judge<br/>faithfulness, relevance,<br/>correctness"]
    LB[/"Leaderboard"/]

    GS --> G --> RUN
    RUN --> MR & MO & MG
    MR & MO & MG --> LB
```



Gold questions are anchored by
`[scripts/anchor_gold.py](../scripts/anchor_gold.py)`: it retrieves candidate
chunks into `anchoring/ANCHORING.md`, a human ticks the gold chunks and writes
the reference answer, and `compile` writes `golden.json`. Tune on `dev`, report
headline numbers on `test` (`main.py eval --split test --curated-only`). A
synthetic path (`main.py eval-dataset`, LLM questions anchored to sampled
chunks) also exists, for smoke tests.

Retrieval ground truth is matched by **content hash**, not database UUID, so the
gold set survives re-indexing as long as chunking parameters are unchanged (see
`[keys.py](../src/rag/evaluation/keys.py)`).