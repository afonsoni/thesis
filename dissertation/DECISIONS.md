# Open decisions

Hand-maintained. These are choices to make, not passages to write — the passages
live in `WRITING-TODO.md`, generated from the `\TODO` markers in the LaTeX source.

Move an item to **Settled** rather than deleting it: a decision with a recorded
reason is exactly the material the decision-history thread of the Proposition
chapter is built from.

## Structural

- **Evaluation chapter structure and RQ wording** (proposal 2026-10-16, in
  `EVALUATION-CHAPTER.md`). Results card first, RQ5 second, the ladder third,
  cost as columns. RQ1 needs rewording to what was measured (representation),
  since granularity and encoder comparisons are not run.
- **Open-source framing.** Whether "built entirely from open components" is
  a research question (needs a proprietary comparison run) or a stated design
  constraint (needs no extra work). See `VIVA-QUESTIONS.md` item 1.
  Since 2026-10-15 proprietary models are in the evaluation (GPT-5.4 for
  `*_strong`, three assistants for `assistant_*`), but only as yardsticks: the
  system itself is still all open-weight.
- **Where does the parser/embedding/vector-DB candidate research live?**
  Currently duplicated: surveyed in `ProblemAndChallenges.tex` §Approaches and
  referenced again in the Proposition. The plan is to migrate each block into
  the matching Proposition subsection and delete it from the problem chapter —
  do it block by block so nothing is lost.
- **Old vault outline vs. the three-part Proposition.** `Thesis Index.md` in
  the Obsidian vault organises the proposition as Why-RAG → Challenges →
  Solutions → Tools. Those bullets reshuffle into indexing / query time /
  evaluation rather than being discarded.
- **The "three RAG implementations" framing** from the vault's `A falar.md`
  (naive / agentic / a third) was superseded by the feature-flagged variant
  ladder, which isolates one technique per rung. The thesis should say so
  explicitly rather than leave the older plan unaddressed.

## Technical — these gate what can be written

- **Judge–human agreement** (raised 2026-10-15). Every RAGAS-style number
  rests on one LLM judge (`qwen/qwen3.8-27b`) that no human has checked on
  this corpus. `scripts/judge_validation.py` exports a blind sheet of about 25
  answers' claims; rating it (about an hour) gives claim-level Cohen's kappa
  and answer-level Spearman for the Methodology chapter. Decided 2026-10-16:
  the user rates the sheet.
- **AD classification spot check, after.** AD was re-classified with the
  tightened prompt on 2026-10-07 (`54808b6`). The 30-chunk spot check
  (`HISTORY-GAPS.md` §7) has not been re-run for the before/after figure the
  Proposition promises (`\TODO` there).

## History gaps

All nine answered on 2026-10-06 in `HISTORY-GAPS.md` (the user's answers,
then git evidence, fill-ins and fact-checks). That file is the raw material
for the decision-history thread of the Proposition chapter.

## Settled

- **Code freeze** (2026-10-15). No new code unless something is needed for
  the thesis. Left as future work, never run: the chunk-size sweep (needs
  span-based gold matching, an equal token budget per size and one index per
  size; the PAN touradas probe ranked the best chunk 49 / 18 / 6 / 3 at
  128 / 200 / 400 / 800 tokens with the party name in the query, 1 / 4 / 1 / 11
  without), the encoder comparison (not blocked by gold matching, but needs an
  encoder per index table), and the agentic rung.
- **A fifth RQ on gold-set methodology: overtaken** (2026-10-15). RQ5 became
  retrieval versus scale, and the gold set is hand-written and hand-reviewed,
  not synthetic-anchored. It stays methodology in the Proposition unless the
  supervisor wants it as an RQ.
- **Models** (2026-10-10, judge 2026-10-11). Every LLM role runs on the paid
  `google/gemma-4-26b-a4b-it` (`ec46db9`), with free fallbacks recorded per
  call; chunk contexts by `google/gemma-4-31b-it`. The judge is
  `qwen/qwen3.8-27b` (`186bf78`), a different model family from the
  generator, so self-preference bias is no longer live.
- **RQ5 rungs built and run** (2026-10-15, `8b736ba`): `no_retrieval` (the
  production generator answering from memory), `no_retrieval_strong` and
  `current_strong` (`evaluation.strong_model`, `openai/gpt-5.4`).
- **Gold set curated** (2026-10-15, `6a0b3eb`): 61 of 61 questions reviewed by
  hand, with a dev/test split.
- **Hybrid retrieval is the default** (2026-10-11, `f4f7f9c`): dev nDCG +0.064
  over `dense_only`.
- **Reranker lost** (dev): recall -0.055 at twice the latency. Stays off;
  reported as a negative result.
- **Contextual retrieval is the default index** (2026-10-12, `524d9ea`): recall
  +0.046 and nDCG +0.057 over `hybrid` on all 61 questions, two passes.
- **Classification at full scale done** (2026-10-07, `54808b6`): all eight
  parties classified; the checkpoint-duplication worry is moot.
- **Dense-retrieval ablations: headers measured, the other two dropped
  unrun** (2026-10-15). Section headers in the embedded text (`contextual`)
  were measured, recall +0.026 over `hybrid`, and folded into contextual
  retrieval (+0.046 with the LLM context), now the default. Stripping party
  names from dense queries and a task-specific Qwen instruction (built
  2026-10-09 as `party_stripped` and `instructed`) were removed before any run:
  the default stack already fixes the question that motivated them (q-04, PAN
  on touradas: gold at ranks 1–3 in `current`), and the ladder already has
  more rungs than the thesis will report. The probe that motivated them, for a
  limitations line if wanted (dense only, PAN-filtered, rank of the best gold
  chunk among 179): 6 as is, 1 with the party name stripped, 2 with headers, 3
  with the instruction; generic "O PAN é um partido…" chunks ranked top 3 for
  four of five PAN questions.
- **Overleaf is a mirror, not the source of truth** (2026-08-16). The git
  bridge needs a paid plan, so the repository holds the LaTeX and
  `scripts/sync_overleaf.sh` builds a zip to drop into Overleaf for
  supervisor review. Never edit the Overleaf copy; the next sync overwrites it.
- **XeLaTeX is the only engine** (2026-08-16). `fontspec` plus the bundled
  NewsGotT fonts rule out pdflatex; pinned in `.latexmkrc`, a magic comment,
  and the workspace settings.
- **Chapter layout** (2026-08-16): Introduction, State of the Art, The Problem
  and its Challenges, Proposition (indexing / query time / evaluation),
  PoliRAG in Practice, Conclusions and Future Work. The Work Plan section
  is already gone.
- **No Preamble chapter** (2026-10-18, reverses the 2026-10-08 decision to
  keep it unnumbered). It was a checkpoint-era account of the abandoned
  bias-classification idea, mostly a literature list for that idea, and its
  political-bias thread already runs through the State of the Art, the
  Problem chapter and the framing-leakage revision. The pivot is now one
  paragraph in Introduction > Research Methods. Its four orphan sources
  (Helgesson Hallström, Lang et al., Tavares, The Bipartisan Press) were
  dropped; `pretraining-political-bias` stays, cited elsewhere.
- **The system is named PoliRAG, provisionally** (2026-10-08). The name sits
  in one macro, `\sysname` in `dissertation.tex`, so a later rename is a
  one-line change. It is introduced in the Abstract, Resumo, Introduction
  (Motivation) and the Proposition lead-in; the demonstration chapter is
  "PoliRAG in Practice". Rejected: ManifestoRAG, Manifesta (no "RAG"),
  politico-meter (implies measuring leaning, the abandoned original idea).
- **No part pages** (2026-10-08). The "Introductory material" and "Core of the
  Dissertation" dividers were removed; they added pages without aiding
  navigation.
- **Political quiz** is future work, not a deliverable. Revisit only if time
  remains after the main chapters are drafted.
- **Parties outside the corpus get a refusal, not a lookalike's programme**
  (2026-10-15; `ec100e3`, `c13d365`, `ee62e67`). Gold q-59 ("O que propõe o
  ADN para a habitação?") names a real party with no programme in the corpus.
  `current-20261013T140724` answered with Aliança Democrática's housing
  measures: the analyzer had mapped ADN to AD. `wide-20261013T032701` named no
  party and led with AD anyway. The deterministic alias regex was not to blame
  (it never matches "adn"). The analysis prompt asked for "nomes exactos da
  lista" and showed only full names, so the model snapped any party onto the
  nearest listed one.
  - *Fix.* The analyzer also returns `unlisted_parties`. A question naming
    only such parties skips the search and gets the fixed
    `OUT_OF_CORPUS_ANSWER`, which also lists the eight corpus parties. A
    mixed question ("PS e ADN") is answered for the corpus party and opens
    with `OUT_OF_CORPUS_NOTE`. A live check after the first fix still found
    "PS e ADN" read as AD, and PPM sent to PAN. The analyzer's party table now
    shows each party's initials, plus one sentence on the coalitions: PSD,
    CDS-PP and PPM ran as AD, and PCP and PEV as CDU.
  - *Two refusals, two meanings.* `NO_INFO_ANSWER` says retrieval found
    nothing, and does not claim the manifestos are silent (top-k cannot prove
    absence, q-61). The out-of-corpus answer is certain: the programme is not
    in the corpus.
  - *Rejected: a hand-made list of non-corpus parties.* It needs no LLM, but
    it refuses good questions: "ADN" is also Portuguese for DNA (a question
    about criminal DNA databases), and "RIR" and "MAS" are ordinary words.
  - *No ablation flag* (recommended, to confirm). This is a bug fix, not a
    retrieval technique under study. Every reported rung is re-run after
    it, so the paired comparisons stay clean. Report the effect as q-59
    before and after (abstention 0.857 in `current-20261015T034207` came from
    q-59 failing).
  - *Limits.* Detection relies on the LLM recognising a party name. In
    October 2026 each case was checked live once, and the analyzer varies
    between calls. The faithfulness judge may count the note in a mixed
    answer as an unsupported claim; no gold question is mixed today.
  - *Where it goes.* Proposition §Query analysis (a "Revision: parties
    outside the corpus" paragraph), §Grounding and neutrality (the two
    refusals), and Limitations. Not placed as a `\TODO` yet, because
    `Proposition.tex` had uncommitted edits from another session.
