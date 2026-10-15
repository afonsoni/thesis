# System Architecture

This document explains how the RAG system works, stage by stage, with Mermaid
diagrams. The system has four parts:

1. **Indexing** (offline) — turns the manifesto PDFs into a searchable vector store.
2. **Retrieval** (online) — turns a user question into a ranked set of manifesto passages.
3. **Generation** (online) — answers from those passages, with source citations.
4. **Evaluation** (offline) — replays the *same* retrieval and generation code as
   a ladder of feature-flagged variants to measure what each technique contributes.

Each retrieval/generation technique maps to a specific method from the
*RAG-from-Scratch* series (noted as "Part N" below).

The diagrams are also the dissertation's figures:
[`scripts/render_diagrams.sh`](../scripts/render_diagrams.sh) renders every
block below, in order, to `dissertation/images/architecture-*.pdf`. Keep the
labels conceptual (code links go in the prose) and re-run the script after
editing a diagram.

---

## 1. Overview

```mermaid
flowchart LR
    subgraph IDX["Indexing"]
        direction TB
        I1[/"Manifesto PDFs"/] --> I2["Parsing"] --> I3["Cleaning"] --> I4["Chunking"] --> I5["Topic classification"] --> I6["Contextualisation"] --> I7["Embedding"]
    end

    VS[("Vector store<br/>PostgreSQL + pgvector")]

    subgraph RET["Retrieval"]
        direction TB
        Q1(["Question"]) --> Q2["Query analysis"] --> Q3["Multi-query expansion"] --> Q4["Routing"] --> Q5["Hybrid search and fusion"]
    end

    subgraph GEN["Generation"]
        direction TB
        G1["Context preparation"] --> G2["Answer synthesis"] --> G3(["Answer + citations"])
    end

    subgraph EV["Evaluation"]
        direction TB
        E1[/"Gold set"/] --> E2["Variant ladder"] --> E3["Metrics"] --> E4[/"Leaderboard"/]
    end

    IDX --> VS --> RET --> GEN
    RET -.-> EV
```

The dotted arrow into evaluation means the harness reuses the production
retrieval and generation code and the same vector store — variants differ only
by feature flags, so score differences isolate the contribution of one
technique.

---

## 2. Indexing pipeline

`PDF → Markdown → clean → chunk → classify → contextualise → embed → store`.
Parsing and cleaning are separate commands (`main.py parse`, `main.py clean`);
the rest is orchestrated by
[`indexing/pipeline.py`](../src/rag/indexing/pipeline.py).

```mermaid
flowchart LR
    subgraph PREP["Document preparation"]
        direction TB
        PDF[/"8 manifesto PDFs"/] --> PARSE["<b>Parsing</b><br/>Marker<br/>PDF to Markdown"] --> CLEAN["<b>Cleaning</b><br/>layout residue, heading tree<br/>by hand, or LLM + review"]
    end

    subgraph IDX["Indexing pipeline"]
        direction TB
        CHUNK["<b>Chunking</b><br/>split on headings<br/>400-token windows<br/>parents ≤ 1,500 tokens"] --> CLS["<b>Topic classification</b><br/>LLM, structured output<br/>18 topics, ≤ 3 per chunk<br/>checkpointed to JSON"] --> CTXT["<b>Contextualisation</b><br/>LLM writes a short<br/>context per chunk<br/>cached by content hash"] --> EMB["<b>Embedding</b><br/>Qwen3-Embedding-0.6B<br/>1,024 dimensions<br/>with headers + context"]
    end

    VS[("<b>Vector store</b><br/>PostgreSQL 17 + pgvector<br/>HNSW on cosine, GIN on topics,<br/>BM25 over a Portuguese tsvector")]

    PREP --> IDX --> VS
```

- **Parse** — [`parser.py`](../src/rag/indexing/parser.py) wraps the `marker_single` CLI; raw output goes to `data/1_markdown/_raw/`.
- **Clean** — [`cleaner.py`](../src/rag/indexing/cleaner.py) runs a deterministic residue pass, then an LLM pass that may only keep, demote or drop heading candidates (any output word absent from the input is rejected). AD, LIVRE, PCP and PS were corrected by hand instead.
- **Chunk** — [`chunker.py`](../src/rag/indexing/chunker.py) splits on headings, then windows recursively in tokens of the embedding model's own tokenizer (`small_to_big`). The window is embedded; its parent section (capped at `indexing.max_parent_tokens`) is what generation reads.
- **Classify** — [`classifier.py`](../src/rag/indexing/classifier.py) assigns topics via a structured LLM call, fail-fast. Results are checkpointed to `data/2_processed/*-classified.json` (`--classify-only`), so re-indexing from them (`--from-classified`) spends no classification tokens.
- **Contextualise** — [`contextualizer.py`](../src/rag/indexing/contextualizer.py) has an LLM (`indexing.contextual_model`) write one or two sentences situating each chunk in its manifesto (contextual retrieval). Contexts are cached by content hash in `data/2_processed/contexts-*.json`, and the run is fail-fast like classification. On by default (`indexing.llm_context`); the stored `content` never changes.
- **Embed** — [`embedder.py`](../src/rag/indexing/embedder.py) uses `Qwen/Qwen3-Embedding-0.6B` (32k-token window). Each chunk is embedded as `party | section path`, its context, then its text (`indexing.contextual_headers`); queries get the model's instruction prefix, documents do not.
- **Store** — [`store.py`](../src/rag/indexing/store.py) writes vectors + metadata to pgvector: HNSW for similarity, GIN on the topic array for filters (Part 11), and a generated Portuguese `tsvector` over context + content whose lexemes [`bm25.py`](../src/rag/indexing/bm25.py) ranks for lexical search. The lower ladder rungs search a plain index without headers or contexts (`indexing.plain_table`).

---

## 3. Retrieval pipeline

`analyze → expand → route → search → fuse`. Entry point:
[`retrieval/pipeline.py`](../src/rag/retrieval/pipeline.py). Dashed stages are
gated by a flag on [`RetrievalConfig`](../src/rag/retrieval/config.py) (named
in brackets), which is how a single code path can act as any rung of the
variant ladder. All are on in production except the two marked *off*.

```mermaid
flowchart TD
    Q(["Question (pt-PT)"])
    AN["<b>Query analysis</b> [use_query_analysis]<br/>LLM, structured output: parties, coverage, topics,<br/>answer shape and a reformulated query"]
    EX["<b>Multi-query expansion</b> [use_multi_query]<br/>reformulated query + 4 rewrites"]
    RT["<b>Routing</b> [use_routing]<br/>query type derived from parties and coverage"]
    FAN["<b>Per-party fan-out</b><br/>comparison or topic exploration<br/>one search per party, 8 chunks each"]
    ONE["<b>Single search</b><br/>single party or general<br/>party filter if one is named, 10 chunks"]
    SE["<b>Search</b>, for every query<br/>dense: pgvector cosine similarity<br/>+ lexical: BM25 on Portuguese lexemes [use_hybrid]<br/>+ topic filter [use_topic_filter, off]"]
    FU["<b>Fusion</b><br/>Reciprocal Rank Fusion, k = 60"]
    RR["<b>Reranking</b> [use_reranker, off]<br/>cross-encoder over 30 candidates"]
    OUT(["Ranked chunks, flat or grouped by party"])

    Q --> AN --> EX --> RT
    RT --> FAN & ONE
    FAN & ONE --> SE
    SE --> FU --> RR --> OUT

    classDef flag stroke-dasharray: 5 4
    class AN,EX,RT,RR flag
```

Routing logic lives in [`router.py`](../src/rag/retrieval/router.py); the
similarity search, lexical search and RRF live in
[`searcher.py`](../src/rag/retrieval/searcher.py); the cross-encoder pass lives
in [`reranker.py`](../src/rag/retrieval/reranker.py).

With a flag off, each stage degrades instead of disappearing:

| Flag off             | Behaviour                                                        |
| -------------------- | ---------------------------------------------------------------- |
| `use_query_analysis` | no LLM call; question treated as GENERAL (no parties or topics)  |
| `use_multi_query`    | one query: the reformulated question                             |
| `use_routing`        | one unfiltered search                                            |
| `use_hybrid`         | dense lists only (`dense_only` and the first three rungs)        |
| `use_topic_filter`   | no topic filter (the default)                                    |
| `use_reranker`       | fused list trimmed straight to `top_k` (the default)             |

Fusion has no flag: it runs whenever a search produced more than one ranked
list (several queries, or dense + lexical).

Details the diagram compresses:

- **Out-of-corpus parties.** A question naming only parties outside the corpus
  (`unlisted_parties`) skips search entirely; generation answers with a fixed
  reply rather than a programme from the wrong party.
- **Query analysis fallback.** If the LLM call fails, an exact party-alias scan
  sets the parties and coverage falls to *exhaustive*, so the router fans out
  rather than silently omitting parties.
- **Fan-out** searches every named party, or all eight when none is named, so no
  party is crowded out of a global top-k (`top_k_per_party`, default 8). A single
  search returns `top_k` (default 10).
- **Topic filters are off by default** (`use_topic_filter`). When on, searches
  also apply the analysed topics (never `outros`), and any topic-filtered search
  that matches nothing is retried without the filter (per party, for fan-outs).
- **Hybrid** adds a lexical list per query, so `2 × len(queries)` lists are
  fused in one RRF pass.
- **Reranking** (off: it lost on dev) widens before it narrows: each sub-query
  retrieves `rerank_candidates` (default 30) rather than `top_k`, and the
  cross-encoder scores the *original* question against each chunk before the
  trim. A reranker can only promote what retrieval surfaced, so the wide fetch
  is what gives it room to work.

---

## 4. Generation (answer synthesis)

The synthesizer prepares the context, then picks a strategy from the requested
`answer_shape`, and answers with numbered source citations.
[`generation/pipeline.py`](../src/rag/generation/pipeline.py),
[`synthesizer.py`](../src/rag/generation/synthesizer.py).

```mermaid
flowchart TD
    IN(["Retrieval result"])
    CHK{"Passages<br/>found?"}
    FIX(["Fixed reply, no LLM call:<br/>party not in the corpus,<br/>or no passage found"])
    CTX["<b>Context preparation</b><br/>expand chunks to parent sections, merge overlaps<br/>trim lowest-ranked to a 32,000-token budget,<br/>never dropping a whole party"]
    D{"Answer<br/>shape"}
    CMP["<b>Comparison</b><br/>per-party shape<br/>one context block per party"]
    DIR["<b>Direct</b><br/>narrative shape<br/>single pass over the ranked context"]
    OUT(["Answer (pt-PT) + numbered citations"])

    IN --> CHK
    CHK -->|no| FIX
    CHK -->|yes| CTX --> D
    D --> CMP & DIR
    CMP & DIR --> OUT
```

Shape rather than route, because the two cross: *"que partido propõe mais sobre
habitação?"* needs every party retrieved but answered as one verdict. A
narrative answer over a fan-out reads the whole grouped set rather than
`RetrievalResult.results`, which the router truncates to `top_k`. A per-party
answer whose results arrived flat (a single search) is regrouped by party.

Context size is bounded by `llm.openrouter.max_prompt_tokens` rather than by a
result count. Over-budget contexts are trimmed lowest-ranked first, and a
grouped context is trimmed from whichever party contributes most so that no
party is dropped outright. Sibling windows of one section are merged into one
document. Citations follow the trimmed context — a source the model never read
is one it cannot have used.

---

## 5. Evaluation harness

The harness measures each **implementation step** on the same gold set. Because
every variant runs the production code with only different flags, a score delta
is attributable to one technique. Code:
[`src/rag/evaluation/`](../src/rag/evaluation/); methodology:
[`evaluation.md`](evaluation.md).

```mermaid
flowchart TD
    subgraph GS["Gold set construction"]
        direction LR
        C["<b>Questions</b><br/>hand-drafted, some<br/>unanswerable"] --> A["<b>Anchoring</b><br/>dense + lexical<br/>candidate chunks"] --> R["<b>Human review</b><br/>gold chunks and<br/>reference answers"]
    end

    G[/"<b>Gold set</b><br/>dev / test split"/]

    RUN["<b>Variant ladder</b><br/>every variant over every question<br/>same code, feature flags differ"]
    MR["<b>Retrieval</b><br/>hit@k, recall@k,<br/>MRR, nDCG@k"]
    MO["<b>Routing</b><br/>query-type and coverage<br/>accuracy, party/topic F1"]
    MG["<b>Generation</b>, LLM judge<br/>claim-level faithfulness<br/>and correctness, relevance,<br/>abstention"]
    LB[/"<b>Leaderboard</b><br/>bootstrap intervals"/]

    GS --> G --> RUN
    RUN --> MR & MO & MG
    MR & MO & MG --> LB
```

Gold questions are anchored by
[`scripts/anchor_gold.py`](../scripts/anchor_gold.py): it retrieves candidate
chunks into `anchoring/ANCHORING.md`, a human ticks the gold chunks and writes
the reference answer, and `compile` writes `golden.json`. Questions marked
`answerable: false` measure abstention. Tune on `dev`,
report headline numbers on `test` (`main.py eval --split test --curated-only`).
The ladder also has closed-book rungs (`use_retrieval=False`) for the
retrieval-versus-scale question; they skip the retrieval, routing and
faithfulness metrics.

Retrieval ground truth is matched by **content hash**, not database UUID, so the
gold set survives re-indexing as long as chunking parameters are unchanged (see
[`keys.py`](../src/rag/evaluation/keys.py)).
