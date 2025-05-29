# RAG System for Political Programs Analysis

A modular Retrieval-Augmented Generation (RAG) system for analyzing Portuguese political party programs with support for base, corrective, and agentic RAG implementations.

## Project Structure

```bash
thesis/
├── main.py
├── config/
│   └── config.yaml
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── data/
│   │   ├── extraction/
│   │   └── preprocessing/
│   ├── embeddings/
│   │   └── embedding_generator.py
│   ├── rag/
│   │   ├── base/
│   │   ├── corrective/
│   │   └── agentic/
│   └── utils/
│       ├── config_loader.py
│       └── dependency_checker.py
└── tests/
```

## Features

### RAG Implementations

1. **Base RAG**: Simple retrieval + generation pipeline
2. **Corrective RAG**: Evaluates retrieval quality and refines queries when needed
3. **Agentic RAG**: Uses iterative reasoning with multiple search strategies

### Core Components

- **PDF Extraction**: Converts PDF files to markdown using marker
- **Embedding Generation**: Creates vector embeddings using sentence transformers
- **Vector Storage**: Uses Milvus for efficient similarity search
- **LLM Integration**: Uses LLaMA API for text generation
- **Configuration Management**: Centralized YAML-based configuration

## Quick Start

### 1. Initial Setup

```bash
# Check dependencies and setup data pipeline
python main.py --setup
```

This will:

- Check and install required dependencies

- Extract PDF files to markdown

- Generate embeddings and store in Milvus

### 2. Interactive Usage

```bash
# Base RAG (simple)
python main.py

# Corrective RAG (with query refinement)
python main.py --implementation corrective

# Agentic RAG (with iterative reasoning)
python main.py --implementation agentic
```

### 3. Single Query

```bash
# Ask a specific question
python main.py --query "What is PS's position on education?"

# Use corrective RAG for complex queries
python main.py --implementation corrective --query "Compare economic policies across parties"

# Use agentic RAG for comprehensive analysis
python main.py --implementation agentic --query "Analyze environmental policies" --top-k 8
```

## Configuration

Edit `config/config.yaml` to customize:

- **Paths**: Data directories
- **PDF Extraction**: Tool settings and output format
- **Text Chunking**: Method, size, and overlap
- **Embeddings**: Model and dimensions
- **Milvus**: Connection and index settings
- **LLM**: Model and generation parameters
- **RAG**: System prompts and retrieval settings

## Environment Variables

Create a `.env` file with:

```env
LLAMA_API_TOKEN=your_llama_api_token_here
```

## Dependencies

- Python 3.8+
- pymilvus
- sentence-transformers
- openai
- python-dotenv
- markdown
- click
- pypdf

Dependencies are automatically checked and installed when running `--setup`.

## Usage Examples

### Basic Query
```bash
python main.py --query "Quais são as propostas do PS para a educação?"
```

### Advanced Analysis
```bash
python main.py --implementation agentic --query "Compare as políticas ambientais de todos os partidos" --top-k 10
```

### Custom System Prompt
```bash
python main.py --system "You are a political expert. Provide detailed analysis." --query "Economic policies"
```

## API Usage

```python
from src.rag.base.base_rag import BaseRAG
from src.rag.corrective.corrective_rag import CorrectiveRAG
from src.rag.agentic.agentic_rag import AgenticRAG

# Initialize RAG system
rag = BaseRAG()

# Query the system
result = rag.query("What are the main education policies?")
print(result["response"])
```

## Architecture

### Base RAG Flow
1. User query → Embedding generation
2. Vector similarity search in Milvus
3. Retrieve top-k documents
4. Format context + generate response with LLM

### Corrective RAG Flow
1. Initial retrieval (same as base)
2. Evaluate retrieval quality using LLM
3. If quality is insufficient, refine query
4. Re-retrieve with refined query
5. Generate final response

### Agentic RAG Flow
1. Plan search strategy (break query into sub-questions)
2. Iterative search across multiple sub-queries
3. Assess information completeness after each iteration
4. Synthesize information from all searches
5. Generate comprehensive response

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure to run `python main.py --setup` first
2. **Milvus Connection**: Ensure Milvus is running on localhost:19530
3. **API Token**: Set your LLAMA_API_TOKEN in `.env` file
4. **Dependencies**: Run `python main.py --check-deps` to verify

### Debug Mode

Add verbose logging by modifying the config file or use:

```bash
python -v main.py --query "your question"
```

## Contributing

1. Follow the modular structure
2. Add new RAG implementations in `src/rag/`
3. Update configuration schema in `config/config.yaml`
4. Add tests in the `tests/` directory

## License

This project is for academic research purposes.
