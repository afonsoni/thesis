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
