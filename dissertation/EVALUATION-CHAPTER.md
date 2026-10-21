# Evaluation chapter: proposed structure

Claude's proposal of 2026-10-16. The split itself is settled (2026-10-21,
`DECISIONS.md`): this is now the plan for `chapters/Results.tex`, whose last
section is PoliRAG in practice. The section contents below are still proposals.

The chapter's job is a RAGAS-style report card of PoliRAG. Comparisons support
the card; they are not the point.

## Protocol

- **Choose on dev, report on test.** Gold set: 61 questions. Test: 36 (32
  answerable, 4 unanswerable). Dev: 25 (22 + 3). Every design decision so far
  was taken on dev or on all 61.
- **The test run is done** (2026-10-20, code `0293a0b`, tag `code-freeze`):
  every reported rung judged once on the 36 test questions. Tables:
  `data/eval/reports/leaderboard-test.md` (everything, paired against `naive`)
  and `data/eval/extras/headline-analysis.md` (RQ5 against `current`, the
  results card by question type, cost per answer). Runs over all 61 include
  the dev questions the system was tuned on; if one is quoted, say so.

## Sections

1. **Setup.** Gold set and split, the judge (`qwen/qwen3.8-27b`, a different
   family from the Gemma generator), the metric table below, and the
   judge–human agreement result (claim-level kappa, answer-level Spearman).

   | RAGAS | PoliRAG | Difference |
   |---|---|---|
   | Faithfulness | `faithfulness` | Same method: claims checked against the context |
   | Answer relevancy | `answer_relevance` | 1–5 judge instead of generated questions |
   | Context precision | MRR, nDCG | Human-picked gold chunks instead of LLM guesses |
   | Context recall | recall@k, `aspect_recall` | Same |
   | Answer correctness | `correctness`, `correctness_recall` | Claim-level F1 against the reference |
   | — | `abstention`, `false_refusal` | Manifesto-specific: saying "the programmes don't say" |

2. **Results card (RQ3).** `current` on test: every metric above, overall, by
   question type (single party, comparison, topic, general) and for the
   unanswerable questions. This table is the headline.

3. **Retrieval versus scale (RQ5).** `current` against `no_retrieval` (same
   Gemma, from memory), `no_retrieval_strong` (GPT-5.4 from memory),
   `current_strong` (GPT-5.4 with retrieval) and `assistant_*` (ChatGPT,
   Gemini and Claude with web search). Correctness, abstention and cost per
   answer. Faithfulness and retrieval metrics do not apply to closed-book
   rungs. Likely the most quotable result: a small model with the manifestos
   against big models without them, and who admits not knowing.

4. **Where the quality comes from (RQ1, RQ2).** A short ladder, one change per
   step:
   - `naive` → `dense_only` → `hybrid` → `current` (retrieval and generation
     metrics);
   - representation, for RQ1: plain index (`hybrid`) → section headers
     (`contextual`) → LLM context (`current`);
   - `reranked` as a negative result: recall −0.055 at twice the latency.

   Everything else (`shallow`, `topic_filter`, `budget_64k`, `lexical_wide`)
   goes to the appendix or is left out.

5. **Cost (RQ4).** Not a section of its own: latency, tokens and USD per answer
   as columns in the tables of 3 and 4. Every eval run records each call's
   tokens and cost.

6. **Limitations.** Existence questions (top-k retrieval cannot prove absence);
   faithfulness is not neutrality (framing passes the faithfulness check); a
   single judge model, mitigated by the human agreement check; chunk
   granularity and encoders were not compared; 61 questions give wide
   intervals (report the bootstrap CIs).

## Research questions

Done 2026-10-21: RQ1 reworded to representation (granularity and the encoder
are future work), RQ2's `multiquery` and `routed` rungs ran on test, and RQ5
names commercial assistants with web search.

## Findings from the test run (2026-10-21)

Paired differences per question with 95% bootstrap intervals; `*` means the
interval excludes zero. n = 36 (32 answerable, 4 unanswerable).

**1. The judge's `correctness` penalises true extra detail. Read RQ5 with this.**
`correctness` is an F1 whose precision half marks a claim unsupported when it
adds anything the reference lacks. q-02, `assistant_gpt`: "PCP… 1 000 euros
mensais em 2024" is right, but the claim failed because the reference does not
say "mensais" or "programa eleitoral de 2024", so `correctness` = 0.0 while
`correctness_recall` = 0.33. Long and web-sourced answers lose most:
`deep_research_claude` matches `current` on `correctness_recall` (−0.005) but
trails by −0.236* on `correctness`. So lead comparisons across systems with
`correctness_recall` (and `correctness_grounded` for PoliRAG's own rungs),
report the F1 second, and put assistant and deep-research answers in the
judge–human rating sample so the agreement figure covers this case.

**2. The ladder: routing and hybrid search carry the gains.** One step at a time:

| Step | recall | nDCG | correctness_recall |
|---|---|---|---|
| + multi-query (`naive` → `multiquery`) | +0.042 | +0.053 | −0.005 |
| + analysis and routing (`naive` → `routed`) | **+0.209*** | **+0.092*** | **+0.113*** |
| + multi-query on top of routing (`routed` → `dense_only`) | +0.046 | +0.013 | −0.003 |
| + lexical BM25 (`dense_only` → `hybrid`) | **+0.121*** | **+0.140*** | **+0.102*** |
| + section headers in the index (`hybrid` → `contextual`) | +0.008 | +0.007 | +0.020 |
| + LLM context in the index (`contextual` → `current`) | +0.035 | **+0.040*** | −0.012 |

Multi-query expansion did nothing measurable on test, alone or after routing.
Headers alone did nothing. The LLM context improves ranking (nDCG) but not the
answers: `current` against `hybrid` is recall +0.043*, nDCG +0.047*, but
`correctness` +0.004 and `correctness_recall` +0.008. Dev had suggested more
(recall +0.046 for contextual retrieval); test shrinks it. Say so.

**3. The reranker lost again.** On top of `current`: recall −0.111*,
`correctness_recall` −0.074 (interval reaches 0), latency 9.5 s against 3.5 s.
Consistent with dev (−0.055). A clean negative result.

**4. RQ5: retrieval beats scale, and the assistants do not beat PoliRAG.**
- Closed book is hopeless on manifesto detail: `correctness_recall` −0.550*
  for the same Gemma, −0.508* for GPT-5.4 without retrieval.
- A stronger model with the same retrieval helps: `current_strong` +0.111*
  `correctness_recall`, at 37× the pipeline cost ($0.041 against $0.0011 per
  answer) and 3.6× the latency.
- GPT and Gemini assistants with web search: `correctness_recall` −0.084 and
  −0.078, both intervals crossing zero, so "no better than PoliRAG" at roughly
  60–80× the cost ($0.07–0.09 per answer) and 7–26× the latency.
- The Claude assistant trails clearly (−0.283*). Its answers often say it
  could not reach the programme and fall back on press and parliamentary
  sources (q-04, q-12). That is honest behaviour that scores badly here; worth
  one sentence.

**5. Results card (`current`, test).** Recall 0.870, nDCG 0.767, faithfulness
0.952, `correctness_recall` 0.634, `correctness_grounded` 0.720, relevance
0.922, false refusal 6% (2 of 32). Strongest on comparisons (`correctness_recall`
0.709), weakest on topic explorations (0.296, n = 4) and general questions
(0.438, n = 4, faithfulness 0.75). Per-type groups are small, so their
intervals are wide.

**6. Abstention rests on four questions.** `current` refused all 4
unanswerable ones. With n = 4 one miss moves the rate by 0.25, and the
assistants' 0.750 has an interval of [0.25, 1]. Report counts ("4 of 4"), not
rates.

**7. Truncated answers.** The 3,000-token answer cap cut 3 `current_strong`,
2 `assistant_gemini` and 5 `assistant_claude` answers, which may lower their
recall-type scores slightly. One line in the limitations.

**8. Judging costs more than answering.** `current` costs $0.0011 per answer
to run and $0.0084 to judge. Relevant if RQ4 discusses the cost of evaluation
itself.

**9. Two tables, two denominators.** `leaderboard-test.md` (and the appendix)
averages every variant over the questions *all* variants were scored on;
`headline-analysis.md` averages each variant over its *own* scored questions.
After re-judging (DECISIONS.md, 2026-10-22) only two judge omissions remain,
`naive` q-41 (correctness) and `reranked` q-31 (faithfulness), so the two
differ by a question at most, e.g. `assistant_gpt` correctness 0.510 over 31
against 0.518 over 32. Results card: per-run means (n = 32). Comparisons:
paired differences, which drop a question only when one of the two sides
lacks it.

