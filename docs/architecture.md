# System Architecture

This document explains how the RAG system works, stage by stage, with Mermaid
diagrams. The system has three parts:

1. **Indexing** (offline) — turns the manifesto PDFs into a searchable vector store.
2. **Retrieval + Generation** (online) — answers a user question with grounded citations.
3. **Evaluation** (offline) — replays the *same* retrieval code as a ladder of
   feature-flagged variants to measure what each technique contributes.

Each retrieval/generation technique maps to a specific method from the
*RAG-from-Scratch* series (noted as "Part N" below).

---

## 1. Overview

```mermaid
flowchart LR
    subgraph ING["Indexing (offline)"]
        direction TB
        PDF["8 manifesto PDFs"] --> MD["Markdown"] --> CH["Chunks"] --> CL["Topic labels"] --> EMB["Embeddings"]
    end

    VS[("PostgreSQL + pgvector<br/>HNSW index + metadata")]
    EMB --> VS

    subgraph SERVE["Query time (online)"]
        direction TB
        Q["User question (pt-PT)"] --> R["Retrieval<br/>analyze → route → search"]
        R --> G["Generation<br/>grounded synthesis"]
        G --> A["Answer + source citations"]
    end
    VS --> R

    subgraph EVAL["Evaluation (offline)"]
        direction TB
        GOLD["Curated gold set"] --> RUN["Variant ladder<br/>naive → current"]
        RUN --> LB["Leaderboard"]
    end
    VS -.-> RUN
    R -.-> RUN
```

The dotted arrows into the evaluation box mean the harness reuses the production
retrieval code and the same vector store — variants differ only by feature
flags, so score differences isolate the contribution of one technique.

---

## 2. Indexing pipeline

`PDF → Markdown → chunk → classify → embed → store`. Orchestrated by
[`indexing/pipeline.py`](../src/rag/indexing/pipeline.py).

```mermaid
flowchart TD
    A["Raw PDF<br/>data/0_raw/*.pdf"] -->|marker_single| B["Clean Markdown<br/>data/1_markdown/{party}/"]
    B --> C["Header-aware chunking<br/>+ recursive windowing"]
    C --> D["Topic classification<br/>OpenRouter · 18 categories · multi-label<br/>checkpoint/resume · fail-fast"]
    D --> E["Embedding<br/>Serafim 900M · 1536d<br/>optional summary-based multi-representation"]
    E --> F[("PostgreSQL + pgvector<br/>HNSW index + metadata")]

    D -.->|"--classify-only"| G["Classified JSON<br/>data/2_processed/*.json"]
    G -.->|"--from-classified"| E
```

- **Parse** — [`parser.py`](../src/rag/indexing/parser.py) wraps the `marker_single` CLI.
- **Chunk** — [`chunker.py`](../src/rag/indexing/chunker.py) splits on markdown headers, then windows recursively.
- **Classify** — [`classifier.py`](../src/rag/indexing/classifier.py) assigns topics via a structured LLM call; results can be checkpointed to JSON so re-indexing spends no classification tokens.
- **Embed** — [`embedder.py`](../src/rag/indexing/embedder.py) uses the Portuguese-specific Serafim encoder.
- **Store** — [`store.py`](../src/rag/indexing/store.py) writes vectors + metadata to pgvector with an HNSW index (Part 11 metadata filtering, Part 12 multi-representation).

---

## 3. Retrieval pipeline

`analyze → expand → route → search`. Entry point:
[`retrieval/pipeline.py`](../src/rag/retrieval/pipeline.py). Every step is gated
by a flag on [`RetrievalConfig`](../src/rag/retrieval/config.py), which is how a
single code path can act as any rung of the variant ladder.

```mermaid
flowchart TD
    Q["User question"] --> AQ{"use_query_analysis?"}
    AQ -->|yes| AN["analyze_query()<br/>structured LLM → query_type,<br/>parties, topics, ideology<br/>(heuristic fallback)"]
    AQ -->|no| GEN0["treat as GENERAL"]

    AN --> MQ{"use_multi_query?"}
    GEN0 --> MQ
    MQ -->|yes| EX["expand_query()<br/>+4 reformulations (Part 5)"]
    MQ -->|no| ONE["single query"]

    EX --> RT{"use_routing?"}
    ONE --> RT
    RT -->|no| G["GENERAL route"]
    RT -->|yes| TYPE{"query_type?"}

    TYPE -->|single_party| SP["party-filtered search"]
    TYPE -->|comparison| CMP["per-party parallel search<br/>→ grouped results"]
    TYPE -->|topic_exploration| TP["topic / ideology filtered"]
    TYPE -->|general| G

    SP --> S["Searcher<br/>pgvector similarity per query"]
    CMP --> S
    TP --> S
    G --> S

    S --> RRF{"use_rrf?"}
    RRF -->|yes| FUSE["Reciprocal Rank Fusion (Part 6)"]
    RRF -->|no| ORDER["first-occurrence merge"]
    FUSE --> RES["RetrievalResult (top_k)"]
    ORDER --> RES
```

Routing logic lives in [`router.py`](../src/rag/retrieval/router.py); the
similarity search + RRF live in [`searcher.py`](../src/rag/retrieval/searcher.py).

---

## 4. Generation (answer synthesis)

The synthesizer picks a strategy from the query type and result shape, then
produces an answer with source citations.
[`synthesizer.py`](../src/rag/generation/synthesizer.py).

```mermaid
flowchart TD
    RES["RetrievalResult"] --> D{"synthesize() dispatcher"}
    D -->|"comparison + grouped results"| CMPA["comparison_answer()<br/>grouped-by-party prompt"]
    D -->|"comparison, no groups"| DEC["decomposed_answer()<br/>sub-questions → synthesis (Part 7)"]
    D -->|"topic_exploration & >8 results"| DEC
    D -->|"otherwise"| DIR["direct_answer()<br/>single-pass"]
    CMPA --> OUT["GeneratedAnswer<br/>+ source citations"]
    DEC --> OUT
    DIR --> OUT
```

---

## 5. Evaluation harness

The harness measures each **implementation step** on the same gold set. Because
every variant runs the production retrieval code with only different flags, a
score delta is attributable to one technique. Code:
[`src/rag/evaluation/`](../src/rag/evaluation/); methodology:
[`evaluation.md`](evaluation.md).

```mermaid
flowchart LR
    subgraph BUILD["Gold-set construction"]
        direction TB
        SAMP["sample_chunks() from pgvector"] --> QGEN["LLM writes a question<br/>answerable from that chunk"]
        QGEN --> SYN["synthetic.json<br/>(curated=false)"]
        SYN --> CUR["hand-curate → golden.json<br/>~30-50 Q (curated=true)"]
    end

    subgraph LADDER["Variant ladder — same code, flags differ"]
        direction TB
        V0["naive"] --> V1["multiquery"] --> V2["routed"] --> V3["current"] --> V4["reranked / hybrid<br/>(reserved)"]
    end

    CUR --> RUN["runner<br/>run each variant over the gold set"]
    LADDER --> RUN
    RUN --> M{"metrics"}
    M -->|retrieval| MR["hit@k · recall@k · MRR · nDCG@k"]
    M -->|routing| MO["query-type acc · party F1 · topic F1"]
    M -->|"generation (LLM-judge)"| MG["faithfulness · relevance · correctness"]
    MR --> LB["leaderboard.md / .csv"]
    MO --> LB
    MG --> LB
```

Retrieval ground truth is matched by **content hash**, not database UUID, so the
gold set survives re-indexing as long as chunking parameters are unchanged (see
[`keys.py`](../src/rag/evaluation/keys.py)).
