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
- **Classification cost at full scale.** Eight parties at roughly 3k token
  chunks each; the checkpoint duplication was flagged as worth revisiting once
  all eight land.

## History gaps — reconstruct from memory, no git trail exists

- **Milvus → pgvector.** No reason recorded in the commit, and pgvector was
  not even among the candidates surveyed in the pre-thesis.
- **MiniLM → serafim.** Same commit, same silence. Serafim was not in the
  surveyed candidate list either; the January 2025 meeting note mentions
  struggling with BERTimbau, which may be the thread to pull.
- **The March 2026 rewrite** (`9d15f90`, +46.5k lines). The whole
  architecture, the 18-topic taxonomy, and the abandonment of agentic RAG
  landed in a single commit. What the "2 variations" in its message referred
  to is unstated.
- **Parser bake-off.** Which parser won and why, and why Marker's output still
  needed hand correction (`-manual.md`).
- **Chunk size 1000 → 1600 characters** (`5a8453e`). No reason recorded, and
  retroactively significant: it deepened the truncation bug quantified later.
- **The August 2026 "pre-existing local work" commits** (`8ccd547`,
  `f5c61c7`, `4f57720`) cover features with no development trail.

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
  Prototype Demonstration, Conclusions and Future Work. The Preamble chapter
  is dropped once its pivot story moves into the Introduction; the Work Plan
  section is already gone.
- **Political quiz** is future work, not a deliverable. Revisit only if time
  remains after the main chapters are drafted.
