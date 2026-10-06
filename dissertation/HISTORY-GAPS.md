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

Both `pdfminer` and `pymupdf` were not able to extract the PDF text properly. Honestly, I didn't care about columns, tables, or graphs. Images also not.
What I really cared the most was that the text was properly extracted, and that I would not neet to make a lot of manual changes. Besides pdfminer and pymupdf I also tried a Microsoft PDF extractor, but again, it wasn't as good as marker.
The nicest thing about marker, was that it was extracting from PDF directly to markdown, it was open source, local and was free. That last reason was also the reason to rule out some other parsers like LlamaParse. Also the fact it is not built on Gen AI, but regular embedding text extractors. It has a VLM, but it only calls it where necessary, which improves speed while keeping accuracy.
Finally, Markdown headers ended up being needed for header-aware chunking. I didn't spend much time on this. I mostly looked for the first tool that worked well for what I was needing.

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

I mostly fixed some broken headers and removed text that was not important. Basically the differences you can see between the regular extracted text and the manual variant. Check it please and fill in the missing parts.
I only got to fix those parties for now. I want to fix the rest soon. All parties should have a manual version before embedding. Perhaps I wil rerun marker with new settings, as it has gotten a newer version, and check if indeed we get less errors.
It took a while to fix a single political party program (around 20-30 minutes, depending on size and amount of things that must be cleaned up). We should try to make the cleanup of markdown political programs automated, so that in the future we can just had new political programs, from other years, for example, to add even more context to the RAG system.

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

The first embedding model (all-MiniLM-L6-v2) was just to get things started. Indeed, starting with an embedding that doesn't work with Portuguese meant that the first results I was getting were not good, but at least I could see that the RAG system was working. After having the RAG system working, then I started seeing how I could improve results. One of the first things I thought about was the embedding model: how can I get the embeddings to work best for the language in the political parties' programs.
The first time I started seeing actual ok results was when I started using serafim, which I found either on HuggingFace or on a paper on portuguese encoders (https://arxiv.org/html/2407.19527v1). I don't remember which one came first.
On HuggingFace it had one of the best results in Portuguese encoding. Especially since it was tuned for information retrieval (IR). It was also a sentence transformer made for Portuguese, by Portuguese. However, it also became less interesting because it had a big limitation: max_seq_length is 128 tokens. Our median chunk was 365 tokens. I did not notice it at the time of choosing, and only after a while of testing, was I able to understand its limitation. Once the limitation was found, it was time to choose another embedding model.
For now we use Qwen embedding, but I still wonder if there is another possible one, better for Portuguese. I still would like to compare our current Embedding model to Bertimbau or some other embedding model that is currently on the top of Portuguese embeddings, especially for information retrieval. But how would I compare it? How does one compare embedding models/encoders/decoders etc? What are the differences, even? Should we shortly explain that in the thesis?
Perhaps changing the model is something for the future.

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

At first, I was really unaware of the amount of vector databases that existed, and what each was able to offer. Not only have we Milvus, but also some other databases that I wondered using. Perhaps a list of various databases are somewhere in the repo or Obsidian notes. I also found my original source for choosing a vector database, [here](https://medium.com/@mutahar789/optimizing-rag-a-guide-to-choosing-the-right-vector-database-480f71a33139)
I also found a newer website with some more recent information that can help us understand why I was going for one vector database instead of another [here](https://www.braintrust.dev/articles/best-vector-databases-for-rag-2026)
I thought of using Milvus because I saw the amount of people online (various Medium posts and Reddit users) that mentioned how barebones, fast and overall how good it was. Because of that, and also because I thought I would need a dedicated vector database for this project, I decided to give it a try. However, I got immediately frustrated with the setup of it, it was more complicated than it should've been.
Ended up falling through a rabbithole on databases and vector databases and started overcomplicating the issue. Eventually, I found a video that said: [I replaced my entire stack with Postgres...](https://www.youtube.com/watch?v=TdondBmyNXc), where the video essayest mentions replacing the vector database he was using (Pinecone) with Postgresql, using something called pgvector. Why wasn't PostgreSQL never on the table before? I started thinking how I already knew how to use Postgres quite well. Also, the use cases seemed to suit my own very well, and the project I'm doing doesn't require a big dedicated vector database from a specfic manufacturer, it can very well survive being a postgres instance. Also, postgres is open-source, like most of the dedicated vector databases I had considered (Milvus, Qdrant, Chroma, Weaviate, Faiss; Pinecone being the exception), so licence was not what set it apart: what did was not needing a separate service. The video essayist also mentions several interesting things, like:
- PostgreSQL has reliable task queues
- Full text search
- Hybrid vector search
There is more information on [this article](https://volito.digital/how-postgresql-replaces-elasticsearch-redis-kafka-pinecone-and-mongodb-using-extensions-for-ai-vectors-queues-caching-and-search/)

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

This was a doozy. At first, I tried to use local models to not only test my system, but also because they were self contained models, open source and free. 2 years ago, on 2024, when the thesis started, using an LLM for free was still rare. The only way to use a LLM for free, was by either running it yourself, or paying a subscription. You could also create an OpenAI account and use their weaker models for free (until a certain point), but that was a business tactic to have more people using ChatGPT and I didn't want to do that. So we started using Ollama, with varied outcomes. Some better, some worse. The biggest problem was that my machine was not powerful enough to run good models, only the smaller ones. Also, the responses were usually quite slow. That was hindering the progress of the thesis in a way, by not giving me the best results and also waiting so long for things to happen, so we had to change.
I do not remember if Gemini came after right away or if it was after another mistaken route I took, to use something called LlamaAPI. This was something similar to OpenRouter, where you would choose a model to call, and the API would route your call to the proper place (maybe check OpenRouter to understand how that works, as this was basically the same thing). That was shortlived. I added $10 to that API, but after a while, it was deprecated and I was not able to retrieve those $10 anymore. There was no reason for the closure. The website was [this one](https://www.llama-api.com/), though you cannot even access it anymore. Because of that, I tried to steer away from anything similar (hence why it took so long to go back to something similar, like OpenRouter). So I used Gemini for a while, as that was the same thing that was being used at my work. Also because their models are quite ok, they were cheap and I was able to get some free credits to try Google's models and their APIs, so I figured: why not? The quality on Portuguese was also quite ok. The models used at the time were Gemini 2.5 Flash and Pro. I used Gemini for a while, but that was also prone to problems, such as quotas and also because I wanted to easily try other models, and was not able to using only Google's API. Because of that, went on the look for something simpler, and better. OpenRouter was mentioned online, in newsletters that I received on my email and at work, too, by fellow colleagues who like to experiment with LLMs. Knowing about everyone's general good experience with it, I decided to give it a go. Perfect stuff, I can change models easily, and even use the free tier Gemma 4 without a hassle. This made me happy.
The reasons to use Gemma 4 are:
- It's a really competent LLM, despite its size
- It's free
- It is an open model
- Works surprisingly well with Portuguese
- I can easily make a lot of calls in a row (that's mostly on OpenRouter, I guess)

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

The whole ordeal with the variations of RAG systems, is because I wanted to check the differences between them. How better is agentic RAG versus a base/naive RAG? What about corrective RAG? However, it ended up being slightly different, because it was hard creating those different variants. And also, once I understood precisely what Corrective RAG was and what I would need to do to implement it, with the whole "go online to correct your assumption" (check what Corrective RAG is exactly, I know it has web searches), I ended up not creating it.
Instead, I started adding more and more features until we got what we currently have (which is still not at the level I'd like it to be. But then again, when would it?). So the way I'd like to go about this, is that the RAG system was organicaly built, feature by feature. I tried to think deeply about each new thing added, and how it would impact the final results.
Because the thesis was left in standby a couple of times, we would see a lot of breaks between commits (this might not be necessary to add to the thesis).
I also got some inspiration from [OpenRAG](https://openragmoe.github.io/) and tried to check for some RAG in 2026 tips to always keep the project updated up until the delivery date (like [this website](https://lushbinary.com/blog/rag-retrieval-augmented-generation-production-guide/), for example)

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

It came from looking at the different political programs of all parties and seeing which topics come up the most, as well as looking online for ways to compare different programs, like [this one](https://expresso.pt/politica/eleicoes/legislativas-2024/comparador-de-programas). [This one](https://www.politicaativapt.com/partidos/comparar) also has a bunch of topics, but they are a bit simpler. It ended up being a mix between the first and the second.
Many times a chunk can have more than a single topic (check for 2 examples to give). In those cases, we have more than one topic. That can help with the retrieval, depending on the question and how general (or non general) it is.
Regarding the keyword fallback, I don't like hard coded things and prefer that instead of storing worse data without knowing, it's better to fail fast.

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

Chunking has been changing many times during the implementation of the RAG system. I tried smaller chunking in the beginning of the implementation, mostly as testing purposes, and also because the overall idea of chunking and chunk size in 2024 was still on the 500 max_chunk_size. Contexts were not big, LLMs had a hard time interpreting a big chunk, or finding the most relevant things. Eventually, made the max chunk size at 1000, and later on even made it bigger, to 1600, as well as the increse of chunking size. These decisions were informed mostly by how the industry was moving. I was seeing more and more articles mentioning that the chunk size should be bigger, as LLMs now have the possibility of getting more context. But choosing encoding/embbeding models was a pain in the ass. I was having so many issues (mostly inside my head) about what the best one would be, as a model that isn't made thinking about portuguese, will undoubtly encode words in strange manner and it will be harder to look them up. Portuguese words have many different meanings, and also there are homonymous words (canto, "corner" vs "I sing", or rio, "river" vs "I laugh"), homographs (fábrica vs fabrica), and homophones (concelho vs conselho), though these last ones probably won't make a big problem. It's mainly the homonymous words that I'm most worried about.
The whole serafim's 128-token window limited was more of a mistake in the choosing of the encoding model. It seemed perfect, as it had a really good performance and quality on Portuguese and was quite recent. But I was not aware that the size of it was that small, and that hindered the progression of the system, as the results I was having were still under what I was expecting. Only once I started measuring the chunks and the different encoding values, was I understanding that serafim had this drawback.

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

The evaluation idea was already existent almost since the beginning. We needed a way to evaluate the RAG system and that is what we are going to present in the thesis, too. We need to evaluate how the final system compares to something with less features. How much does the reranking help with improving the answers of the system? What about the hybrid search? Is Agentic RAG better than a simple hybrid + reranking RAG? How does the final system compare to a simple LLM call to a regular model (like Gemini 3.6 Flash or GPT-5.6 Luna)? What about a more powerful LLM from the main names on AI at the moment (Claude Opus 5.5 or Fable 5.1, Gemini 4 Argon, GPT‑6.1 Sol or 6 Astra, Kimi K3, Muse Spark 1.3)? Does it take less resources?
There are other things that I find harder to evaluate: how are we going to evaluate the embedding model? How are we going to understand which chunking strategies are better?
I did use AI assisted development. At first I did it all by myself (only inline aid), then started using a GPT model (trying to remember which one it was), finally started using Claude by the end, to help with tyding everything up and finishing some of the features that were left out incomplete. Claude was a great help in the end also to think a bit about what was missing. The thesis was and will be written solely by me (this will be what will be written in the thesis, at least, you can help with some things, such as suggestions, but I will be the one deciding if we use them or not)

---

# Fill-ins and flags (Claude, 2026-10-06)

Evidence and checks for the parts you asked me to complete. These are notes
for you to write from, not thesis prose.

## 1. Parser
- **"Is Marker GenAI?"** Mostly no, and your reading is right. By default
  Marker runs neural models (Surya) that *detect* layout and reading order
  and *transcribe* the text on the page. That is AI, but its job is to
  recognise what is there, not to generate new content. The generative part
  is the optional LLM pass (`--use_llm`), which you didn't use. One nuance:
  the OCR step is itself a sequence model that emits text token by token, so
  avoid the GenAI label altogether. Suggested wording: "Marker converts PDFs
  with neural layout-detection and OCR models; its optional LLM-assisted mode
  was not used." Nothing in it can be challenged.
- **Licence nuance:** Marker's code is GPL-3.0, but its model weights use a
  modified OpenRAIL-M licence, which is free for research and personal use
  with commercial limits. "Open source and free" holds for this thesis, but
  state it precisely, because examiners check licences.
- **Name the Microsoft tool.** It's probably MarkItDown (released Dec 2024).
  Confirm this, so it can sit in the candidates list with the others.
- "First tool that worked well" is an honest and defensible framing. Say it
  plainly: parsing was a means, not the object of study.

## 2. Manual correction: what the diff shows
Measured from the first Marker output (`1af3074`, April 2025, which matches
today's `_raw/` apart from image links) against `-manual.md`:

| Party | Words | Headers | `#` (H1) | Table lines | Image links |
|---|---|---|---|---|---|
| AD | 56,817 → 55,474 | 238 → 218 | 3 → 2 | 251 → 117 | 338 → 0 |
| LIVRE | 61,491 → 60,247 | 159 → 60 | 57 → 1 | 22 → 0 | 0 → 0 |
| PCP | 42,856 → 41,070 | 301 → 224 | 11 → 1 | 118 → 9 | 4 → 0 |
| PS | 52,307 → 51,668 | 163 → 138 | 1 → 1 | 24 → 24 | 29 → 0 |

Note: the committed non-manual files for LIVRE, PCP and PS were already the
corrected text, so `1af3074` is the only true "before" in git.

The fixes fall into four kinds:
1. **Rebuilding the header hierarchy.** Marker flattened sections into many
   H1s. LIVRE had 57, one per page running header plus one per section
   title. Each manifesto now has a single H1 (the title) and a consistent
   H2–H6 tree, for example AD: Programa → Ambição → Qualificação → Educação →
   "1. Porque é preciso mudar / 2. Metas / 3. Medidas". This is what
   header-aware chunking depends on, so it's the key fix.
2. **Removing the table of contents.** Marker turned it into Markdown tables
   (`| 2.<br>Metas | 51 |`). That accounts for most of the dropped table
   lines in AD and PCP. If left in, a TOC chunk matches almost any query
   while containing no proposals.
3. **Removing layout residue:** image links, `<span id="page-…">` anchors, repeated page
   headers ("Programa do LIVRE | Legislativas 2024"), and split cover titles
   ("**FUTURO contrato com o**").
4. **Little else.** Only about 1–4% of words were removed, so the content is
   essentially untouched. That's worth saying, because it shows the
   correction didn't edit what parties actually proposed.

Real tables were kept (PS: 24 → 24).

**Automation note (future work).** Fixes 2 and 3 are mechanical and
scriptable. Fix 1 needs judgement, though a header-level heuristic or an LLM
pass could handle it. Your point about adding future election cycles is the
argument for automating it.

**Correction:** the LIVRE "mojibake" flagged earlier was a false alarm. My
own output truncation cut "estereótipos" mid-character. The file is clean,
and no manifesto contains a replacement character.

**Your addition (why automate cleaning):** besides adding future and past
election cycles (turning the system into an archive of what parties
proposed), automation would let someone add manifestos from parties that are
on the ballot but not in parliament. That's a good accessibility argument:
small parties are the ones voters know least about. Use it in Future Work and
Implications.

## 3. Embeddings: comparing encoders (your questions)
- **How to compare them:** the harness can already do it. Re-index the same
  corpus once per encoder, with the same chunking, then run the retrieval-only
  metrics (hit@k, MRR, nDCG) on the same gold set. Retrieval metrics don't
  need the LLM judge, so the cost is just indexing time. Candidates:
  Qwen3-Embedding-0.6B (current), multilingual-E5, BGE-M3, and a BERTimbau
  or Serafim-family model with a longer window if one exists. This would
  answer RQ1 directly.
- **The differences, briefly:** an *encoder* (BERT family: BERTimbau,
  serafim) reads the whole text in both directions and pools it into a
  vector. A *decoder-based embedder* (Qwen3-Embedding) is an LLM trained
  further for retrieval, which takes the last token's state as the vector.
  It brings long context windows and instruction prefixes ("query: …").
  Separately, *sentence-similarity* training (STS) and *retrieval* training
  (query → passage) optimise different things.
- **Should the thesis explain it?** Yes, one or two paragraphs in State of the
  Art "Recent developments". It's what justifies the serafim → Qwen3 reversal.
- **Also cite** the Serafim paper (arXiv 2407.19527) as the source you found.

## 4. Vector store
- **Factual problem to fix:** "almost none of the other vector databases were
  open source" is wrong. Milvus (Apache-2.0), Qdrant (Apache-2.0), Chroma
  (Apache-2.0), Weaviate (BSD-3) and Faiss (MIT) are all open source. Only
  Pinecone is proprietary. An examiner would catch this.
- **The real argument** is already in your answer and holds up: no extra
  dedicated service, a database you already knew, metadata filtering in plain
  SQL, and built-in full-text search. That last one made hybrid retrieval
  almost free later, so tell it as a payoff you didn't plan for.
- The Milvus setup frustration fits the facts: the config pointed at a Milvus
  server (`localhost:19530`) that the code never used. Only the embedded Lite
  file was ever used.
- Blog posts and a YouTube video are weak citations. For the thesis, cite the
  pgvector repo/docs and, if possible, a benchmark or paper. Keep the video as
  the honest "how I found it" anecdote, not as evidence.

## 5. LLMs
- Strong, complete answer. The LlamaAPI episode explains the eight-month gap
  before OpenRouter, so keep it. It's a concrete case of the "field moving
  fast" theme: a service vanishing mid-project.
- Gemma 4 being an open-weights model supports the open-components framing
  (see `DECISIONS.md`, open-source framing).

## 6. RAG variants: what CRAG and agentic RAG are
- **Corrective RAG** (Yan et al., 2024, "Corrective Retrieval Augmented
  Generation"): a small *retrieval evaluator* scores the retrieved documents.
  If it judges them *correct*, they are refined (split into strips, irrelevant
  ones filtered out). If *incorrect*, they are discarded and a **web search**
  replaces them. If *ambiguous*, both are used. So your memory is right: web
  search is central. That's a principled reason to drop it here, because a
  manifesto QA system must answer from the manifestos, not the open web. Say
  this explicitly; it reads as a design decision rather than a gap.
- **Agentic RAG:** an LLM agent decides whether, what and how often to
  retrieve (tool calls, loops, self-checks). It costs many LLM calls per
  query, which free-tier rate limits make painful. That's a second honest
  reason.
- **"Organically, feature by feature"** matches the ladder well: each rung is
  one of the features, in the order they were added. Pausing between commits
  isn't thesis material, agreed.
- The `testing_rag` reading of "2 variations" wasn't confirmed or denied. Fine
  to leave it out of the thesis.

## 7. Taxonomy: multi-label examples (AD, classified checkpoint)
Labels per chunk: 1 label: 29 chunks, 2: 108, 3: 176, 4: 70. So 92% of
chunks carry two or more topics.

Good examples for the thesis:
- *"ESTUDANTES E ALOJAMENTO"* (student residences) →
  `habitacao, educacao, governacao`
- *"Isenção de IMT e Imposto de Selo para jovens"* (house purchase) →
  `habitacao, impostos, jovens`

**Spot check done (30 random AD chunks, seed 7):**
- The **first label was right in about 29 of 30**. The primary topic is
  reliable.
- **Extra labels were the problem.** About 8 of 30 chunks had a clearly
  wrong extra label: a tourism chunk tagged `saude`, a sea-and-fisheries
  chunk tagged `educacao`, business financing tagged `financas` (which means
  public finances), a cultural-policy chunk tagged `politica_externa`, and a
  poverty diagnosis tagged `governacao, saude`. About 6 more had a weak
  `governacao`, added whenever the State or municipalities were mentioned.
- **One under-assignment:** student residences got no `jovens`, even though
  the prompt used that exact case as an example.
- **Confidence is uninformative.** Every one of the 383 chunks scored 4 or
  5, so it can't be used to filter unsure labels.
- **Root cause in the prompt:** the batch prompt said "classifica com
  MÚLTIPLAS categorias (máximo 4)", which reads as an instruction to give
  several. The model obliged.

**Fix applied** (`src/rag/indexing/classifier.py`): both prompts now share
one rule set. It puts the primary topic first and adds another label only if
the chunk holds a concrete proposal or figure on it ("na dúvida, omite").
It expects 1–2 labels and allows 3 at most, with explicit rules against
`governacao`-as-catch-all and `financas` for private finance. The hard cap
also drops from 4 to 3. The AD checkpoint predates this, so re-classify AD
along with the other seven, then re-run the spot check to get a
before/after number for the thesis.

**Original flag:** some labels look over-assigned. A justice-targets chunk got
`ambiente`, and a consumer-protection chunk got `educacao, saude`. With 64%
of chunks carrying three or more labels, the topic filter may be weaker than
it looks. Two options:
- mention it as a limitation, or
- spot-check about 30 chunks by hand and report agreement. That's a small,
  cheap validation of the classifier, which currently has none.

Also cite the two comparators (Expresso comparador, Política Ativa) as the
sources the taxonomy was derived from. The removed keyword list had 17
topics, so it was likely the earlier draft.

## 8. Chunk size
- "The industry moved to bigger chunks" needs a citation, or it reads as
  folklore. The chunk-size sweep promised in the pre-thesis would turn it into
  your own evidence.
- **The homonym point** (canto, rio) is good material, but it belongs in
  `ProblemAndChallenges.tex` as a Portuguese-specific challenge (the L57
  TODO asks for exactly that), not in the chunking history.
- **Turning point:** the doubt came from measuring chunk lengths in tokens
  against the encoder's window. That answers the open question in entry 9.

## 9. Evaluation and AI assistance
- **Your evaluation questions map onto the RQs**, with two scope warnings:
  - "Is agentic RAG better than hybrid + reranking?" needs an agentic rung,
    which doesn't exist. Either build it or keep it out of the RQs.
  - Comparing against several frontier models costs money per model. RQ5
    needs one no-retrieval run, ideally against one strong model. Pick one,
    not six.
- "How to evaluate the embedding model and chunking strategies": see 3 above.
  Both are retrieval-only re-index runs on the same gold set.
- **AI-assistance statement (revised 2026-10-06):** Claude may draft
  passages; you review them and rewrite them in your own words. The
  Methodology disclosure should then cover both the code (plain local work,
  then GPT, then Claude) and drafting assistance on the text. Agree the
  wording with your supervisor.
- **Decided:** build an agentic rung, and run the encoder comparison from 3.
  Both are tracked in `DECISIONS.md`.
