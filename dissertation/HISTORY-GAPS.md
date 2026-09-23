# History gaps

Raw material for the decision-history thread of the Proposition chapter. Each
entry gives what git shows, then questions only you can answer. Write under
**Your answer** in any form: bullets, half-sentences, Portuguese or English.
"Don't remember" is a valid answer. It tells me to write around the gap
honestly instead of inventing a reason.

Once an entry is answered, it gets drafted into the matching `\TODO` in
`chapters/Proposition.tex` and summarised under **Settled** in `DECISIONS.md`.

---

## 1. Parser bake-off: PDFMiner → PyMuPDF → Marker

**What git shows**
- `80530d7` (2025-01-29): `tests/pdf_extractor_v1.py` uses `pdfminer`,
  `tests/pdf_extractor_v2.py` uses `pymupdf`. Both produce plain text.
- `1af3074` (2025-04-03): `tests/pdf_extractor.py` calls `marker_single` and
  all 8 manifestos are committed as Markdown (+ `_meta.json`).
- The pre-thesis also lists PyPDF and LlamaParse as candidates. Nothing in git
  shows they were tried.

**Questions**
- What was wrong with the PDFMiner and PyMuPDF output? (column order, tables,
  headers lost, hyphenation, encoding?) A specific manifesto that broke?
- Did you actually try PyPDF or LlamaParse, or rule them out on paper? Why?
  (LlamaParse: paid/cloud?)
- What made Marker win: Markdown headers (needed for header-aware chunking)?
  Tables? Quality by eye?
- How did you judge quality: side-by-side reading, a checklist, anything
  measured?

**Your answer**


---

## 2. Hand-correcting Marker output (`-manual.md`)

**What git shows**
- `77eb97f` (2025-08-24) "started improving markdowns", `2c52f75`
  (2025-08-31) "improved markdowns".
- Manual variants exist for only 4 of 8 parties: `ad`, `livre`, `pcp`, `ps`.

**Questions**
- What did you fix by hand? (broken header levels, merged columns, tables,
  page headers/footers, footnotes, junk characters?)
- Why those four parties? Worst Marker output, biggest parties, or just the
  ones you got to?
- Roughly how long did one manifesto take?
- Did you consider re-running Marker with other settings, or with an LLM
  cleanup pass, instead of manual work?
- The other four (`be`, `chega`, `il`, `pan`): will they get manual versions
  before embedding, or be indexed from raw Marker output? (This is the work
  you're about to do, so the answer can come later.)

**Your answer**


---

## 3. Embeddings: all-MiniLM-L6-v2 → serafim-900m

**What git shows**
- `3312dba` (2025-05-29): config uses `all-MiniLM-L6-v2` (384 dim,
  English-only), `chunk_size: 512`.
- The pre-thesis names `paraphrase-multilingual-MiniLM-L12-v2` as the MTEB
  pick. The code used the English L6 model instead.
- `2c52f75` (2025-08-31): switched to
  `PORTULAN/serafim-900m-portuguese-pt-sentence-encoder-ir`. No reason given.
  Serafim isn't in the pre-thesis candidate list.
- The January 2025 meeting note mentions BERTimbau struggling.

**Questions**
- Was the English L6 model deliberate (quick start) or a slip?
- How did you find serafim: supervisor, paper, HF search, PORTULAN/Albertina
  news?
- What convinced you: native pt-PT, the "-ir" (retrieval) variant, the size,
  results you saw?
- Did you compare it against anything (BERTimbau, multilingual-E5, MiniLM) or
  pick it outright?
- Did you notice its 128-token limit at the time?

**Your answer**


---

## 4. Vector store: Milvus Lite → PostgreSQL + pgvector

**What git shows**
- `3312dba` (2025-05-29): `milvus_demo.db` (Milvus Lite file) and `pymilvus`.
- `2c52f75` (2025-08-31): `docker-compose.yml` with `pgvector/pgvector:pg17`,
  new `database.py`; the README just says "the database chosen … is
  PostgreSQL, using pgvector". `milvus_demo.db` deleted in `9d15f90`.
- pgvector isn't in the pre-thesis candidate list (Faiss, Pinecone, Qdrant,
  Milvus, ChromaDB, Weaviate).

**Questions**
- Why Milvus first: ANN-benchmarks results, the Lite single-file mode,
  a tutorial?
- What went wrong with it, or what made pgvector attractive? (metadata
  filtering with SQL, one DB for everything, Docker, familiarity from work,
  Milvus Lite limits on macOS?)
- Did full-text search (later used for hybrid retrieval) play any part, or
  was that a lucky side effect?
- Why wasn't pgvector in the original survey: didn't know it, or didn't see
  it as a "vector DB"?

**Your answer**


---

## 5. LLM: local Llama-2/Mistral → Gemini → OpenRouter

**What git shows**
- `3312dba` (2025-05-29): config default `llama-2-7b-chat.Q4_0.gguf`, with
  llama and mistral model types (local, quantised).
- `9d15f90` (2026-03-01): Gemini via `google.generativeai`.
- `411b886` (2026-04-09): OpenRouter "instead of just gemini (less
  constrained to a single model)".
- Today: `gemma-4-31b-it:free` on OpenRouter, with 429 problems.
- Pre-thesis candidates: Llama 3.3 70B, DeepSeek-V3, GPT-4, Gemini 2.0 Flash.

**Questions**
- Did you ever run the local GGUF models end to end? Why were they dropped
  (quality in Portuguese, speed on the Mac, memory)?
- Why Gemini next: free tier, Portuguese quality, long context?
- What exactly pushed you to OpenRouter: Gemini quotas, wanting to compare
  models, a model being deprecated?
- Why the free tiers throughout: no budget, or a principle (a civic tool
  anyone can run)? This feeds the open-source-framing decision.

**Your answer**


---

## 6. RAG variants: base / corrective / agentic → "2 variations" → the ladder

**What git shows**
- `3312dba` (2025-05-29): empty stubs `src/rag/agentic/agentic_rag.py` and
  `src/rag/corrective/corrective_rag.py` next to `base_rag.py`. README:
  "base, corrective, and agentic RAG implementations".
- `9d15f90` (2026-03-01) "2 variations of RAG": the CLI offers
  `base | testing | agentic`, where `agentic` is a placeholder. The two real
  variations look like `base_rag.py` and the new `testing_rag.py` (Gemini,
  header-aware context) plus the new modular `src/rag/` pipeline.
- `8ccd547` (2026-08-05): the feature-flagged variant ladder replaces separate
  implementations.
- Vault `A falar.md`: "3 RAG implementations (naive / agentic / third)".

**Questions**
- Is that reading of "2 variations" right? If not, what were they?
- Why were corrective and agentic RAG never implemented: time, cost of many
  LLM calls on a free tier, or a sense they wouldn't help on this corpus?
- What did the "third" implementation in `A falar.md` mean?
- Who or what suggested the ladder idea (one technique per rung, same code)?
  Supervisor, a paper, your own frustration with comparing separate
  implementations?
- Anything happen between Aug 2025 and Mar 2026? (No commits for six months:
  work, courses, a break? One sentence is enough; it explains the jump.)

**Your answer**


---

## 7. The 18-category topic taxonomy

**What git shows**
- Appears fully formed in `9d15f90` (`TOPIC_CATEGORIES` in
  `common/models.py`, classifier + prompts). No earlier draft in git.
- `c298e4b` (2026-04-18): keyword fallback classifier removed, checkpoint/resume added.

**Questions**
- Where did the 18 categories come from: Manifesto Project (MARPOR) coding
  scheme, Portuguese ministry portfolios, manifesto chapter titles, an LLM
  suggestion, your own judgement?
- Did you check them against the manifestos (do all 8 parties' chapters map
  cleanly)?
- Why multi-label instead of one topic per chunk?
- Why did the keyword fallback go: bad labels, or a fail-fast principle?

**Your answer**


---

## 8. Chunk size 1000 → 1600 characters, overlap 100 → 200

**What git shows**
- `5a8453e` (2026-04-09): config `max_chunk_size: 1000 → 1600`,
  `chunk_overlap: 100 → 200`. The commit message only says "small changes to
  chunking size".
- With serafim's 128-token window this made truncation worse; the Aug 2026
  audit found 89.5% of chunks truncated.

**Questions**
- What prompted it: answers missing context, chunks cutting proposals in
  half, a tutorial/default value?
- Did you look at retrieval results before and after, or was it a hunch?
- Was it ever measured in tokens at that point?

**Your answer**


---

## 9. Spring–summer 2026 work committed in August

**What git shows**
- `8ccd547`, `f5c61c7`, `4f57720` (2026-08-05/06) are marked "pre-existing
  local work". The commit bodies explain *what* each does well; what's missing
  is *when and how* it was built.

**Questions**
- Roughly when were the evaluation harness and optional classification
  written (May? July?), and what triggered them?
- What made you start doubting the embeddings in August, the discovery that
  led to the truncation audit? (This is the turning point of the whole story,
  so any detail helps: a bad answer, a length check, a remark from someone.)
- Did you use a coding assistant heavily from some point on? The thesis may
  need a line on AI-assisted development in Methodology; worth deciding
  with your supervisor.

**Your answer**

