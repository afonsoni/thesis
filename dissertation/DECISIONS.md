# Open decisions

Hand-maintained. These are choices to make, not passages to write — the passages
live in `WRITING-TODO.md`, generated from the `\TODO` markers in the LaTeX source.

Move an item to **Settled** rather than deleting it: a decision with a recorded
reason is exactly the material the decision-history thread of the Proposition
chapter is built from.

## Structural

- **RQ4 (cost) — keep or cut?** Well supported: the harness records
  `avg_latency_s` and `error_rate`, and both the hybrid result and the
  reranker's latency raise the question naturally. It is also the least
  central of the four if the chapter runs long.
- **Open-source framing.** Whether "built entirely from open components" is
  a research question (needs a proprietary comparison run) or a stated design
  constraint (needs no extra work). See `VIVA-QUESTIONS.md` item 1.
- **A fifth RQ on gold-set methodology?** Whether a synthetic-anchored,
  hand-curated gold set substitutes for a human-authored one. Arguably the
  most novel contribution, but it may belong in the Proposition as
  methodology rather than as a headline question. Worth raising with the
  supervisor.
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

- **Generation and judge models.** Currently `gemma-4-31b-it:free`, which hits
  429s, and the judge is the same model as the generator, so self-preference
  bias is live (the config file already warns about it). Pick the final models
  before the headline evaluation runs, because every number in the results
  section depends on them.
- **No-retrieval baseline for RQ5.** RQ5 (retrieval versus scale) needs a
  rung on the ladder with retrieval disabled, run over the same gold set with
  the same judge, plus ideally one run against a stronger model without
  retrieval. Until that exists, RQ5 is unanswerable and should not stay in the
  Introduction.
- **Gold-set curation.** The ~30–50 hand-curated questions in `golden.json`
  are not confirmed done. Headline numbers are blocked until they are.
- **Reranker verdict.** Implemented (`05908ac`, cross-encoder
  `BAAI/bge-reranker-v2-m3`) but never measured on the leaderboard. Decide
  whether it earns its latency cost, and whether it ships as a result or as
  future work.
- **Hybrid retrieval verdict.** Gains were honestly described as "narrower
  than expected". The leaderboard settles whether it stays on as a default.
- **Chunk-size sweep (128–2048 tokens).** Promised in the pre-thesis and never
  run. Cheap now that the harness exists, and it would answer RQ1 directly.
  Two prerequisites found 2026-10-09:
  - *Gold matching.* Gold keys are hashes of the current 400-token chunks
    (`keys.py`), so a re-chunked index has none of them. The sweep needs
    overlap-based matching: a chunk counts as relevant if it shares enough text
    with a gold chunk.
  - *Run it after the party-name decision.* Chunk size and party names
    interact. On the PAN touradas question, the best touradas chunk ranked
    49 / 18 / 6 / 3 at 128 / 200 / 400 / 800 tokens with "PAN" in the query
    (fewer, bigger chunks leave fewer generic "O PAN é…" chunks to compete),
    but 1 / 4 / 1 / 11 with it stripped. A sweep run with party names would
    pick the wrong size.

  Embedding the small-to-big parents as chunks (alone: rank 8, or 7 stripped;
  alongside the children: 11, or 1 stripped) did not help on that question.
  Parked unless the dev results show broad questions failing.
- **Encoder comparison — decided, to run** (2026-10-06). Re-index the same
  corpus once per encoder (same chunking) and compare retrieval-only metrics
  (hit@k, MRR, nDCG) on the gold set; no LLM judge needed. Candidates:
  Qwen3-Embedding-0.6B (current), multilingual-E5, BGE-M3, and a
  Portuguese-native encoder with a long enough window if one exists. Answers
  RQ1 together with the chunk-size sweep.
- **Dense-retrieval ablations on the dev split — decided, to run** (2026-10-09).
  Three cheap changes, each measured against `current` on retrieval-only
  metrics before any becomes a default:
  1. *Contextual chunk headers*: embed `party | section path` + content.
     `content` stays unchanged, so gold keys still match; needs a second
     table and re-embedding only. 58% of chunks (1,635 of 2,815) contain no
     heading at all.
  2. *Task-specific query instruction* for Qwen3-Embedding, in English per
     the model card, instead of the shipped "Given a web search query…".
     Query side only, no re-index.
  3. *Party names stripped from dense queries* under a party filter (the
     lexical side already does this).

  Built 2026-10-09 as the ladder variants `contextual`, `instructed` and
  `party_stripped` (`src/rag/evaluation/variants.py`); `contextual` searches
  the `party_programs_ctx` table, built from the same eight checkpoints.

  Evidence (q-04, "Qual é a posição do PAN sobre as touradas?", PAN-filtered,
  rank of the best gold chunk among 179): 6 as is; 1 with the party name
  stripped; 2 with contextual headers; 1 with both; 3 with the custom
  instruction. Generic self-describing chunks ("O PAN é um partido de
  causas…") rank top-3 for four of five different PAN questions: the party
  name pulls the query towards chunks *about the party*, which a party
  filter makes pure noise. The reranker on the dense top 30 also lifts two
  gold chunks to ranks 1–2; the other two (one line each inside chunks about
  other things) never reach the top 30.
- **Agentic rung — decided, to build** (2026-10-06). An LLM-driven retrieval
  loop (decide whether/what to retrieve, re-query, self-check) added as a
  ladder variant, so "agentic vs hybrid + reranking" becomes measurable.
  Corrective RAG stays out: its fallback is web search, and answers must come
  from the manifestos. Watch the per-query LLM call count against free-tier
  rate limits.
- **Re-classify AD after the prompt fix** (2026-10-06). The classifier
  over-assigned extra labels (spot check in `HISTORY-GAPS.md` §7); the
  prompt is tightened and the cap dropped from 4 to 3. The AD checkpoint
  predates the fix. Re-run the 30-chunk spot check afterwards for a
  before/after figure.
- **Classification cost at full scale.** Eight parties at roughly 3k token
  chunks each; the checkpoint duplication was flagged as worth revisiting once
  all eight land.

## History gaps

All nine answered on 2026-10-06 in `HISTORY-GAPS.md` (the user's answers,
then git evidence, fill-ins and fact-checks). That file is the raw material
for the decision-history thread of the Proposition chapter.

## Settled

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
- **Preamble is kept, unnumbered** (2026-10-08, reverses the 2026-08-16 plan
  to drop it). It opens the main matter as a starred chapter listed in the
  table of contents without a number, so the Introduction is Chapter 1.
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
