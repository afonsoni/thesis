# Questions to be ready for

Not part of the dissertation. This is preparation for the defence and for
supervisor meetings: questions worth having a considered answer to, including
ones the thesis deliberately does not try to answer.

Each entry records where (if anywhere) the thesis addresses it, and notes
toward an answer. Fill in the notes as results land — an examiner will press
on the ones where the honest answer is "we did not measure that".

---

## 1. Can a system like this be built entirely from open source, and still be good?

**Where in the thesis:** design constraint in the Proposition; revisit in the
discussion. Becomes RQ-worthy only if a proprietary comparison is actually run.

**Notes toward an answer.** The built stack is already almost entirely open:
Marker for parsing, Qwen3-Embedding for encoding, PostgreSQL with pgvector for
storage, a BAAI cross-encoder for reranking, sentence-transformers throughout.
The generation and judging calls go through a hosted API, but to open-weight
models. Two distinct claims are available and they should not be conflated:
open *weights* (anyone can run it) versus open *service* (no dependency on a
vendor). Worth deciding which is being claimed before being asked.

**Open:** has any comparison against a proprietary encoder or generator been
run? If not, the honest answer is that the constraint was a design choice, not
a measured trade-off.

## 2. How does European Portuguese compare with English here?

**Where in the thesis:** Limitations; a survey note in the State of the Art.

**Notes toward an answer.** This work cannot measure it — that needs a
parallel English corpus with its own gold set, which does not exist here. What
*can* be said rests on published multilingual benchmark figures for the
encoder, and on the reason the encoder was swapped in the first place: a
Portuguese-specific sentence encoder scored well on similarity and poorly on
retrieval, which is a statement about task fit, not about the language.

Distinguish two things when answering: European Portuguese versus Brazilian
Portuguese (a real corpus and tokenizer concern) and Portuguese versus English
(mostly a matter of training data volume). Conflating them invites a follow-up
that is harder to answer.

## 3. Is RAG actually better than just calling a strong model?

**Where in the thesis:** RQ5, answered by the evaluation chapter.

**Notes toward an answer.** This is the sharpest question in the list and it
is answerable, which is why it became RQ5. It needs a no-retrieval rung on the
variant ladder — the same gold set, the same judge, retrieval disabled — and
ideally a second run against a stronger model without retrieval. The
interesting result is the crossover: whether a small model with grounded
context beats a large one working from memory, and what that costs.

Have the numbers ready in two currencies: quality (faithfulness, correctness)
and resources (latency, tokens). Expect a follow-up on citations: a
no-retrieval answer cannot cite a manifesto passage at all, which is a
qualitative difference that no metric in the harness captures. Say so first,
rather than being told.

## 4. How much more precise is RAG, in numbers?

**Where in the thesis:** the quality half of RQ5, plus the per-technique
deltas in the evaluation chapter.

**Notes toward an answer.** Give the measured delta and the gold-set size in
the same breath — a large improvement over thirty curated questions is a
weaker claim than the number alone suggests, and an examiner who knows
evaluation will ask about the denominator. Be ready to say what the judge
model was and why judging with the same model that generated the answer is a
known bias, and what was done about it.

## 5. What is this worth politically? Could it help political literacy?

**Where in the thesis:** Motivation, and an Implications section in the
conclusions.

**Notes toward an answer.** Argue it, do not claim it: no user study was run,
so public interest and literacy effects are outside what this work
establishes. What can be defended is narrower and still substantial — the
system grounds every claim in a citable passage, which is precisely what
existing voting-advice tools and election-period quizzes tend not to do.

On the "parties change their positions" objection: the corpus is a snapshot of
the 2024 manifestos, so the system answers what those documents say. That is a
genuine limitation and also, arguably, the point — a manifesto is a matter of
record, and a stable, checkable record of what a party committed to has value
precisely when public statements drift from it. Re-indexing per cycle, or
carrying temporal metadata, is the future-work answer.

## 6. Can I have a conversation with it, or ask a follow-up?

**Where in the thesis:** Limitations (g) in the conclusions, and a failing
follow-up shown in "PoliRAG in Practice".

**Notes toward an answer.** No. Every call is stateless: `main.py query` takes
one question, and the analyser, retrieval and generator see only that text, so
"E o PS?" after a question about the AD's housing plans loses the topic. Say it
was a choice before it was a limitation. Stateless answers are reproducible and
judged one by one, and a party filter carried over from an earlier turn cannot
silently bias the next search. The evaluation is fair to it: the gold set is
single-turn, and the assistant baselines were also asked one question per
conversation. The fix is known (rewrite a follow-up plus recent turns into a
standalone question before analysis) and was left out by the code freeze of
2026-10-15. Measuring it needs multi-turn questions written for this corpus,
which the gold set does not have.

## 7. Did the test questions influence your design decisions?

**Where in the thesis:** Proposition, Gold set construction, the Protocol
paragraph. Evidence: `data/eval/extras/dev-only-recheck.md`
(`scripts/eval_extras/dev_only_recheck.py`).

**Notes toward an answer.** Yes, a little, and say so before being asked. Most
revisions were chosen on the 25 development questions (hybrid default,
reranker, `lexical_wide`, the topic-filter diagnosis). Three late ones were
judged on all 61 to narrow the intervals: contextual retrieval (`524d9ea`),
the wider net of 10 / 8 without the topic filter, and the 64k budget (both
`b054bf8`). Re-checked on dev alone from the stored runs, all three go the
same way: the wider net is even stronger on dev (recall +0.141*, against
+0.110* on test), 64k still loses, and contextual retrieval keeps its
direction with intervals touching zero (recall +0.034, nDCG +0.032). So the
decisions do not depend on test; what is not fully independent is contextual
retrieval's own gain on test.

Why it matters little:
- Each was a choice between two options, not a search. How much a test set
  leaks grows with the number of configurations tried on it.
- The test run was a fresh run on frozen code (`0293a0b`): analysis,
  generation and judging all redone; only the questions are shared.
- The headline claims do not rest on these choices. Routing (+0.209* recall)
  predates the split, hybrid (+0.121*) was chosen on dev, and the RQ5 gaps
  (−0.55 closed book) dwarf anything a two-way choice could inflate.
- The leaked effect is small and claimed modestly: on test the LLM context
  helps nDCG (+0.040*) but not `correctness_recall` (−0.012).

Follow-ups:
- *Why not keep test untouched?* With 22 answerable dev questions the
  intervals could not decide (contextual retrieval recall [−0.004, +0.074]).
  More confidence in the decision for a slightly less clean test, disclosed.
- *So the results card is optimistic?* At most slightly, through contextual
  retrieval. The wider net gains more on dev than on test, so test was not
  flattering it.
- *And q-59?* A bug fix, not tuning: the analyser mapped an unknown party
  onto a known one, and the fix covers every party outside the corpus. It is
  one of the four unanswerable test questions, so say "4 of 4, one of which
  motivated the fix".
- *Next time?* Write a small fresh test set after the code freeze. The
  harness exists, so it is the cheapest future-work item.

---

## Questions to expect that are not on this list

Add them as they come up in meetings. Likely candidates:

- Why not fine-tuning instead of retrieval? (The pre-thesis raised it; scope
  ruled it out. Have the reasoning ready, not just the outcome.)
- Why these eight parties, and what about coalitions or smaller parties?
  Notes: coalition members (PSD, CDS-PP, PPM; PCP, PEV) are answered from
  their coalition's programme. A party outside the corpus gets a fixed
  refusal that names it and lists the eight that are covered. Before
  2026-10-15 the system answered "ADN" with AD's programme (gold q-59); see
  `DECISIONS.md`, Settled.
- What stops the system from laundering a party's framing as neutral fact?
- How would this be kept running, and by whom?
