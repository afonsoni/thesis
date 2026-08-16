# Evaluation Methodology

This document describes how the RAG system is evaluated. The goal is to measure
each **implementation step** (naive baseline → current system → future upgrades)
on the same gold set, so improvements can be attributed to specific techniques.

Code lives in [`src/rag/evaluation/`](../src/rag/evaluation/); results are
persisted under [`data/eval/`](../data/eval/).

## 1. Implementation steps (variants)

Every variant is a `RetrievalConfig` preset in
[`variants.py`](../src/rag/evaluation/variants.py). Because all variants run
through the **same production code** (only feature flags differ), a difference in
scores isolates the contribution of a single feature.

| Variant          | analysis | routing | multi-query | RRF | hybrid | rerank | Notes |
| ---------------- | :------: | :-----: | :---------: | :-: | :----: | :----: | ----- |
| `naive`          | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | Single query → single similarity search → direct answer |
| `multiquery`     | ✗ | ✗ | ✓ | ✓ | ✗ | ✗ | + multi-query expansion (Part 5) & RRF fusion (Part 6) |
| `routed`         | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | + structured query analysis & logical routing (Part 10) |
| `current`        | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | The full production pipeline |
| `hybrid`         | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | + Portuguese full-text lists fused in the same RRF pass |
| `hybrid_only`    | ✗ | ✗ | ✗ | ✓ | ✓ | ✗ | Isolates the lexical half against `naive` |
| `reranked`       | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | + cross-encoder precision pass over a wide candidate set |
| `reranked_only`  | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | Isolates reranking against `naive` |

Each of the last four differs from a baseline by exactly one flag, which is what
makes the delta attributable: `hybrid` − `current` is the lexical half,
`reranked` − `current` is the cross-encoder, and the `*_only` rungs measure the
same two techniques against `naive` without expansion or routing in the way.

### The reranked rung

Reranking is the one rung that changes *how much* is retrieved, not just how it
is ordered. With `use_reranker` on, every sub-query fetches `rerank_candidates`
(default 30) instead of `top_k`, the fused list keeps that many, and a
cross-encoder scores each `(question, chunk)` pair before the trim back to
`top_k`. Widening is the point: a reranker can only promote what retrieval
already surfaced, so `rerank_candidates` is the real recall ceiling of the
variant — and reranking a list of exactly `top_k` items would reshuffle the
answer without ever improving its contents.

Two details worth knowing when reading the numbers:

- The cross-encoder scores the **original question**, not the multi-query
  expansions, and scores each chunk's **`content`** (the embedded child) rather
  than its parent section — under `small_to_big` every sibling shares one parent,
  so scoring the parent would tie them all and erase the ordering.
- Reranked results carry `score_type=rerank`: raw relevance logits, unbounded
  and **not** comparable to cosine or RRF scores. Rank-based metrics
  (`hit@k`, `MRR`, `nDCG`) are unaffected; anything that reads raw score values
  is not comparable across variants.

Reranking is also the slowest rung — one forward pass per candidate — so expect
`avg_latency_s` to rise. That trade-off is the point of measuring it.

`RetrievalConfig()` with no arguments reproduces `current` exactly, so adding the
config layer changed no default behavior.

## 2. Gold set (synthetic-anchored + curated)

Ground truth is built by
[`dataset.build_dataset`](../src/rag/evaluation/dataset.py):

1. Sample indexed chunks from pgvector (`VectorStore.sample_chunks`).
2. Ask a strong LLM to write a natural question **answerable from that chunk**,
   plus a short reference answer.
3. The construction method fixes the expected `query_type`, `parties`, and
   `topics` — reliable routing ground truth without extra labeling.
4. Coverage spans all four query types: `single_party`, `comparison`,
   `topic_exploration`, `general`.

**Retrieval ground truth is matched by content hash, not database UUID.**
`insert_chunks` mints a new UUID on every insert and `--drop` re-mints them, so
ids are unstable across re-indexing. Each question stores
`gold_chunk_keys = ["sha1:<normalized content>"]`
([`keys.py`](../src/rag/evaluation/keys.py)); at eval time each retrieved chunk's
content is hashed and checked for membership. This survives re-indexing as long
as chunking parameters are unchanged.

**Curation.** Generated questions start with `curated=false`. Hand-validate a
~30–50 question subset (fix wording, drop bad ones, set `curated=true`) into
`data/eval/questions/golden.json`. Run headline numbers with `--curated-only`.

## 3. Metrics

All metrics implement the `Metric` protocol
([`metrics/base.py`](../src/rag/evaluation/metrics/base.py)), so a standardized
backend (e.g. RAGAS) can be added later without touching the runner.

**Retrieval** ([`retrieval.py`](../src/rag/evaluation/metrics/retrieval.py),
pure-Python, needs `gold_chunk_keys`):

- `hit@k` — any gold chunk in the top-k.
- `recall@k` — fraction of gold chunks in the top-k.
- `mrr` — reciprocal rank of the first gold chunk.
- `ndcg@k` — binary-relevance normalized discounted cumulative gain.

**Routing** ([`routing.py`](../src/rag/evaluation/metrics/routing.py)):

- `query_type_acc` — predicted vs expected route.
- `party_f1`, `topic_f1` — set F1 of extracted parties/topics.

**Generation** ([`generation.py`](../src/rag/evaluation/metrics/generation.py),
LLM-as-judge, 1–5 → [0, 1]):

- `faithfulness` — answer grounded in retrieved context (reference-free).
- `answer_relevance` — answer addresses the question (reference-free).
- `correctness` — answer agrees with the reference answer (reference-based).

Failed judge calls are **omitted** from the average (not scored 0), so a
transient API error doesn't depress the result. `avg_latency_s` and `error_rate`
are recorded for a quality-vs-cost view.

## 4. Running it

```bash
# 0. Prereqs: DB up and corpus indexed
docker compose up -d
python main.py index --all            # or: --from-classified data/2_processed/<file>.json

# 1. Build a synthetic gold set, then curate a golden.json by hand
python main.py eval-dataset --sample-size 60 --out data/eval/questions/synthetic.json

# 2. Run the harness and refresh the leaderboard
python main.py eval --variants naive,current --curated-only
```

Outputs:

- `data/eval/results/<variant>-<timestamp>.json` — full per-question records (run history).
- `data/eval/reports/leaderboard.md` + `leaderboard.csv` — the comparison table (committed).

## 5. Adding a new step

1. Add a `RetrievalConfig` preset to `VARIANTS` in `variants.py`.
2. If it needs new retrieval behavior (e.g. a reranker), implement it in the
   searcher gated behind the config flag.
3. Re-run `python main.py eval --variants <old>,<new>` — the leaderboard now
   compares them on the same gold set.

## Reproducibility notes

- Set `OPENROUTER_API_KEY` in the environment / `.env`.
- Confirm `llm.openrouter.model`, `indexing.classification_model`, and
  `evaluation.judge_model` in `config/config.yaml` are **valid OpenRouter ids**
  before a live run — a wrong id makes every LLM call fail.
- Regenerate the gold set (or at least re-verify `gold_chunk_keys`) if chunking
  parameters change, since content keys depend on chunk text.
