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
Ended up falling through a rabbithole on databases and vector databases and started overcomplicating the issue. Eventually, I found a video that said: [I replaced my entire stack with Postgres...](https://www.youtube.com/watch?v=TdondBmyNXc), where the video essayest mentions replacing the vector database he was using (Pinecone) with Postgresql, using something called pgvector. Why wasn't PostgreSQL never on the table before? I started thinking how I already knew how to use Postgres quite well. Also, the use cases seemed to suit my own very well, and the project I'm doing doesn't require a big dedicated vector database from a specfic manufacturer, it can very well survive being a postgres instance. Also, postgres is open-source. Almost none of the other vector databases were open source. The video essayist also mentions several interesting things, like:
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
Instead, I started adding more and more features until we got what we currently have (which is still not at the level I'd like it to be. But then again, when would it?). So the way I'd like to
I also got some inspiration from [OpenRAG](https://openragmoe.github.io/)

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

