# RAG System for Political Programs Analysis

A unified Retrieval-Augmented Generation (RAG) system for analyzing Portuguese political party programs (2024 elections). The pipeline is structured into three clean stages — **indexing**, **retrieval**, and **generation** — with advanced techniques drawn from the RAG-from-Scratch research series.

## Project Structure

```bash
thesis/
├── main.py                     # CLI entry-point
├── config/
│   └── config.yaml             # Centralized configuration
├── data/
│   ├── 0_raw/                  # Source PDF files
│   ├── 1_markdown/             # Parsed markdown (per party)
│   └── 2_processed/            # Classified JSON outputs
├── src/
│   ├── rag/
│   │   ├── common/             # Shared Pydantic models & constants
│   │   │   └── models.py
│   │   ├── indexing/           # Parse → Chunk → Classify → Embed → Store
│   │   │   ├── parser.py
│   │   │   ├── chunker.py
│   │   │   ├── classifier.py
│   │   │   ├── embedder.py
│   │   │   ├── store.py
│   │   │   └── pipeline.py
│   │   ├── retrieval/          # Analyze → Expand → Route → Search
│   │   │   ├── query_analyzer.py
│   │   │   ├── query_expander.py
│   │   │   ├── router.py
│   │   │   ├── searcher.py
│   │   │   └── pipeline.py
│   │   └── generation/         # LLM clients → Prompts → Synthesis
│   │       ├── llm_client.py
│   │       ├── prompts.py
│   │       ├── synthesizer.py
│   │       └── pipeline.py
│   └── utils/
│       └── config_loader.py    # YAML config helper
├── tests/
└── docker-compose.yml          # PostgreSQL 17 + pgvector
```

## Key Techniques

| Technique                     | Source              | Where Used                    |
| ----------------------------- | ------------------- | ----------------------------- |
| Multi-Query Expansion         | Part 5              | `retrieval/query_expander.py` |
| Reciprocal Rank Fusion        | Part 6 (RAG-Fusion) | `retrieval/searcher.py`       |
| Question Decomposition        | Part 7              | `generation/synthesizer.py`   |
| Logical Routing               | Part 10             | `retrieval/router.py`         |
| Metadata-Filtered Search      | Part 11             | `indexing/store.py`           |
| Multi-Representation Indexing | Part 12             | `indexing/embedder.py`        |

## Core Components

- **PDF Extraction**: `marker_single` CLI tool (produces clean markdown)
- **Chunking**: Header-aware LangChain splitter + recursive windowing
- **Topic Classification**: Structured LLM output via OpenRouter (18 Portuguese categories, multi-label) with keyword fallback
- **Embeddings**: `PORTULAN/serafim-900m-portuguese-pt-sentence-encoder-ir` (1536d, Portuguese-specific)
- **Vector Store**: PostgreSQL 17 + pgvector with HNSW index
- **LLM Generation**: Unified OpenRouter transport with configurable models

## Quick Start

### Prerequisites

```bash
# Start PostgreSQL + pgvector
docker compose up -d

# Install Python dependencies
pip install sentence-transformers psycopg2-binary langchain-text-splitters \
            requests python-dotenv pydantic pyyaml
```

### Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_openrouter_key
```

### 1. Parse PDFs → Markdown

```bash
python main.py parse --input-dir data/0_raw --output-dir data/1_markdown
```

### 2. Index Documents

```bash
# Index all parties
python main.py index --all

# Index a single party
python main.py index --party livre

# Re-index from scratch (drops existing data)
python main.py index --all --drop
```

### 3. Query

```bash
# Simple question
python main.py query "Quais são as propostas do PS para a educação?"

# Comparison (auto-detected)
python main.py query "Comparar as políticas de saúde do PS e do CHEGA"

# Topic exploration
python main.py query "Que partidos falam sobre imigração?"

# With more context
python main.py query "Políticas ambientais dos partidos de esquerda" --top-k 10
```

## Configuration

All settings in `config/config.yaml`:

- **Paths**: data directories
- **Embeddings**: model name, dimension
- **PostgreSQL**: connection details, table name
- **LLM**: OpenRouter model, temperature, max tokens
- **Retrieval**: multi-query count, RRF k-value, default top-k
- **Indexing**: chunk size, overlap, classification model

## Architecture

### Indexing Flow

```
PDF → marker_single → Markdown → Header-aware chunking →
  Topic classification (OpenRouter/keyword) → Embedding (Serafim 900M) →
  PostgreSQL + pgvector (HNSW index)
```

### Query Flow

```
User question → Query Analysis (structured LLM output) →
  Logical Routing by query type →
    ├─ single_party:      metadata-filtered + multi-query + RRF
    ├─ comparison:         per-party parallel search + RRF + grouped synthesis
    ├─ topic_exploration:  topic-filtered + multi-query + RRF
    └─ general:            broad multi-query + RRF
  → Answer Synthesis (direct / comparison / decomposed) →
  Final answer with source citations
```

## Parties Tracked (2024)

| Party                             | Ideology |
| --------------------------------- | -------- |
| Aliança Democrática (AD)          | Right    |
| Bloco de Esquerda (BE)            | Left     |
| CHEGA                             | Right    |
| Iniciativa Liberal (IL)           | Right    |
| LIVRE                             | Left     |
| Pessoas-Animais-Natureza (PAN)    | Left     |
| Partido Comunista Português (PCP) | Left     |
| Partido Socialista (PS)           | Left     |

## API Usage

```python
from src.rag.retrieval.pipeline import retrieve
from src.rag.generation.pipeline import generate

# Full RAG pipeline
result = retrieve("O que propõe o LIVRE sobre habitação?")
answer = generate(result)
print(answer.answer)

# Indexing
from src.rag.indexing.pipeline import index_documents
index_documents(party_filter="livre", drop_existing=True)
```

## Troubleshooting

1. **PostgreSQL not running**: `docker compose up -d`
2. **No API key**: Set `OPENROUTER_API_KEY` in `.env`
3. **No results**: Run `python main.py index --all` first
4. **pgvector not installed**: The Docker image (`pgvector/pgvector:pg17`) includes it

## Contributing

1. Follow the modular structure
2. Add new RAG implementations in `src/rag/`
3. Update configuration schema in `config/config.yaml`
4. Add tests in the `tests/` directory

## License

This project is for academic research purposes.
