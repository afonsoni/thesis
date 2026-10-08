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

## 2. Gold set (hand-written, then anchored and reviewed)

The headline gold set is 51 questions written by hand against the eight
manifestos ([`CANDIDATES.md`](../data/eval/questions/CANDIDATES.md)), each with a
grounding note checked against the indexed text, the route it should take
(parties named, topics, `coverage`), the ladder rung it is meant to stress, and an
expected difficulty. [`scripts/anchor_gold.py`](../scripts/anchor_gold.py) turns
them into `golden.json`:

1. `candidates` retrieves candidate chunks per question (dense search plus short
   keyword queries, per expected party, or per every party when none is named).
2. Gold chunks and a reference answer are proposed per question (here by Claude
   subagents, from the candidates and the grounding note), then **reviewed by
   hand** in `anchoring/ANCHORING.md`: ticks fixed, references edited, and
   `reviewed: yes` set. Only reviewed questions are `curated`.
   `anchoring/proposed-picks.json` keeps the unreviewed proposals, so the human
   edits are visible as a diff.
3. `compile` writes `golden.json`, deriving `query_type` from parties and
   coverage exactly as the pipeline does.

Questions carry a `split`: 30 **test** questions, balanced across route, stress,
party and difficulty, are held out for headline numbers (`--split test`); 21
**dev** questions are for tuning.

**Retrieval ground truth is matched by content hash, not database UUID.**
`insert_chunks` mints a new UUID on every insert and `--drop` re-mints them, so
ids are unstable across re-indexing. Each question stores
`gold_chunk_keys = ["sha1:<normalized content>"]`
([`keys.py`](../src/rag/evaluation/keys.py)); at eval time each retrieved chunk's
content is hashed and checked for membership. This survives re-indexing as long
as chunking parameters are unchanged.

## 3. Metrics

All metrics implement the `Metric` protocol
([`metrics/base.py`](../src/rag/evaluation/metrics/base.py)), so a standardized
backend (e.g. RAGAS) can be added later without touching the runner.

**Retrieval** ([`retrieval.py`](../src/rag/evaluation/metrics/retrieval.py),
pure-Python, needs `gold_chunk_keys`):

- `hit` — any gold chunk retrieved.
- `recall` — fraction of gold chunks retrieved.
- `mrr` — reciprocal rank of the first gold chunk.
- `ndcg` — binary-relevance normalized discounted cumulative gain.

All four score the full list retrieval hands to generation, with no separate
cutoff: `top_k` chunks on a flat route (`eval -k` sets it for every variant),
`top_k_per_party` per party on a per-party fan-out. A fan-out is scored on every
party's list, interleaved by rank; scoring its flat cross-party top-k instead
would hide most parties, and its RRF ties broke in a fixed party order.

**Routing** ([`routing.py`](../src/rag/evaluation/metrics/routing.py)):

- `query_type_acc` — predicted vs expected route. Derived from the two below,
  so it is a summary of them rather than independent evidence; kept as the
  headline number and for comparability with earlier runs.
- `coverage_acc` — did the analysis require every party in scope to be
  represented? This is the one that catches the aggregative failure: "o que
  defende cada partido sobre X" can score a perfect `party_f1` (nothing was
  named) and a perfect `topic_f1` while being answered from a flat top-k that
  omits half the parties.
- `party_f1`, `topic_f1` — set F1 of extracted parties/topics. `expected_parties`
  means *named or implied by the question*, not *ought to be searched*: an
  exhaustive question names none and still searches all eight.

**Generation** ([`generation.py`](../src/rag/evaluation/metrics/generation.py),
[`judge.py`](../src/rag/evaluation/judge.py)). Faithfulness and correctness are
**claim-level**, following RAGAS (Es et al., EACL 2024): a text is split into
atomic claims and each claim is verified against evidence by the judge, and the
score is the share of claims supported. This is computed in code from the
judge's per-claim verdicts, kept on `QuestionRun.judgements` for auditing.

- `faithfulness` — share of the answer's claims supported by the context the
  generator actually read (`GeneratedAnswer.context`: parent sections after
  deduplication and budget trimming). Reference-free.
- `correctness_recall` — share of the curated reference answer's claims that the
  answer states. Does not penalise true detail the reference left out.
- `correctness` — F1 of that recall and the precision of the answer's claims
  against the reference (RAGAS "answer correctness", factual part).
- `answer_relevance` — a holistic 1–5 judgement mapped to [0, 1].

A score whose judge calls failed (after waiting out free-tier errors) or that has
nothing to score is **omitted** from the mean, not set to 0. `avg_latency_s` and
`error_rate` are recorded for a quality-vs-cost view.

**Why not RAGAS end to end.** Retrieval is scored against human-picked gold
chunks with deterministic IR metrics rather than RAGAS's LLM-judged context
precision/recall: no judge noise or cost, rank-aware, and attributable per
technique. Routing and per-party coverage have no RAGAS counterpart. The RAGAS
algorithms are reimplemented on the project transport because the judge must run
on Gemma via Google's native endpoint, which the `ragas` library cannot call.

**Uncertainty** ([`stats.py`](../src/rag/evaluation/stats.py)). Every leaderboard
cell is a mean over the questions *every* variant scored on that metric (a
question that errored in one arm drops out of all of them; `error_rate` counts
it), with a 95% percentile-bootstrap interval over questions, and a second
table gives each variant's **paired** difference from the first variant listed,
with its 95% paired bootstrap interval (bold when it excludes 0). Pairing removes
the between-question variance both arms share; on ~30 questions an unpaired
comparison would rarely detect anything.

**Judge validation** ([`scripts/judge_validation.py`](../scripts/judge_validation.py)).
The judge is Gemma, as is the generator, so self-preference is possible. To
measure it rather than assume it away: `export` samples answers from a results
file into a blind rating sheet (claims without the judge's verdicts), a human
marks each claim, and `score` reports claim-level agreement (raw %, Cohen's
kappa) and answer-level Spearman correlation per metric, plus Spearman on
relevance. The approach of calibrating an LLM judge against a small human-labelled
set follows ARES (Saad-Falcon et al., NAACL 2024).

## 4. Running it

```bash
# 0. Prereqs: DB up and corpus indexed
docker compose up -d
python main.py index --all            # or: --from-classified data/2_processed/<file>.json

# 1. Anchor the hand-written questions, review ANCHORING.md, compile golden.json
python scripts/anchor_gold.py candidates
python scripts/anchor_gold.py compile

# 2. Run the harness and refresh the leaderboard
python main.py eval --variants naive,current --curated-only --split test
```

Outputs:

- `data/eval/results/<variant>-<timestamp>.json` — full per-question records (run history).
- `data/eval/reports/leaderboard[-<split>][-curated].md` + `.csv` — the comparison
  table (committed), one per split and curation setting so a dev run cannot
  overwrite the held-out numbers. Its header names the dataset, split and
  question count.

Failures are never scored as a weaker pipeline. Each eval question runs with
`RetrievalConfig.strict`, so a query-analysis or expansion call that fails
raises instead of falling back to its degraded mode; each stage first waits out
free-tier failures `evaluation.wait_out_attempts` times. A retrieval failure is
an error with no scores; a generation failure keeps the retrieval and routing
scores. `--no-judge` skips generation entirely. A database error raises rather
than reading as an empty result.

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
