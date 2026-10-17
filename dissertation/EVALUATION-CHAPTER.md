# Evaluation chapter: proposed structure

Claude's proposal of 2026-10-16, for reference. Not a decision until it moves to
`DECISIONS.md` → Settled.

The chapter's job is a RAGAS-style report card of PoliRAG. Comparisons support
the card; they are not the point.

## Protocol

- **Choose on dev, report on test.** Gold set: 61 questions. Test: 36 (32
  answerable, 4 unanswerable). Dev: 25 (22 + 3). Every design decision so far
  was taken on dev or on all 61.
- **No run on the test split exists yet.** The headline numbers need one judged
  test run per reported rung. Runs over all 61 include the dev questions the
  system was tuned on; if one is quoted, say so.
- `eval` estimates a run's cost before paying for it.

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

## Research questions to reword

- **RQ1** promises parsing fidelity, chunk granularity, the size unit and the
  embedding model. The evidence covers the unit (character-sized chunks left
  62.7% of the corpus unembedded) and representation (plain, headers, LLM
  context). Suggested: *How do representation choices (measuring chunk size in
  the encoder's own tokens, and enriching each chunk with its section path and
  an LLM-written context) affect retrieval quality over Portuguese electoral
  manifestos?* Granularity and the encoder go to future work.
- **RQ2** names routing and multi-query expansion. The rungs exist
  (`multiquery`, `routed`) but have never been run. Either run them (no code
  needed) or drop them from the wording.
- **RQ3, RQ4, RQ5** stand as written.
