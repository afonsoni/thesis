"""
End-to-end indexing pipeline.

Chains: parse → chunk → classify → (optional: summarise) → embed → store.
"""

import glob
import logging
import os
from typing import List, Optional

from src.rag.common.models import Chunk, EmbeddedChunk
from src.rag.indexing.chunker import chunk_markdown_file
from src.rag.indexing.classifier import classify_chunks
from src.rag.indexing.embedder import Embedder, generate_summaries
from src.rag.indexing.parser import parse_pdfs
from src.rag.indexing.store import VectorStore
from src.utils.config_loader import config

logger = logging.getLogger(__name__)


def _discover_markdown_files(directory: str) -> List[str]:
    """Recursively find all .md files under *directory*."""
    return sorted(glob.glob(os.path.join(directory, "**", "*.md"), recursive=True))


def index_documents(
    markdown_dir: Optional[str] = None,
    party_filter: Optional[str] = None,
    use_llm_classification: bool = True,
    generate_chunk_summaries: bool = False,
    classification_model: Optional[str] = None,
    classification_batch_size: Optional[int] = None,
    classification_delay: Optional[float] = None,
    max_chunk_size: Optional[int] = None,
    chunk_overlap: Optional[int] = None,
    year: int = 2024,
    drop_existing: bool = False,
) -> int:
    """
    Run the full indexing pipeline on markdown files.

    Args:
        markdown_dir: Directory containing ``.md`` files (subfolders supported).
                      Defaults to config ``paths.markdown_data``.
        party_filter: If set, only index files whose path contains this string
                      (case-insensitive). E.g. ``"livre"`` or ``"ps"``.
        use_llm_classification: Use LLM for topic classification (vs keyword fallback).
        generate_chunk_summaries: Generate LLM summaries for multi-representation indexing.
        classification_model: OpenRouter model name for classification.
        classification_batch_size: Number of chunks per classification API request.
        classification_delay: Delay between classification API requests.
        max_chunk_size: Max characters per chunk.
        chunk_overlap: Overlap characters for windowed chunks.
        year: Election year metadata.
        drop_existing: Drop and recreate the table before indexing.

    Returns:
        Total number of chunks stored.
    """
    markdown_dir = str(markdown_dir or config.get("paths.markdown_data", "data/1_markdown"))
    max_chunk_size = int(max_chunk_size or config.get("indexing.max_chunk_size", 1000))
    chunk_overlap = int(chunk_overlap or config.get("indexing.chunk_overlap", 100))
    classification_model = str(
        classification_model
        or config.get(
            "indexing.classification_model",
            config.get("llm.openrouter.model", "google/gemini-2.5-flash"),
        )
    )
    classification_batch_size = int(
        classification_batch_size or config.get("indexing.classification_batch_size", 10)
    )
    classification_delay = float(
        classification_delay
        if classification_delay is not None
        else config.get("indexing.classification_delay", 12.0)
    )
    md_files = _discover_markdown_files(markdown_dir)

    if party_filter:
        md_files = [f for f in md_files if party_filter.lower() in f.lower()]

    if not md_files:
        logger.warning("No markdown files found in %s (filter=%s)", markdown_dir, party_filter)
        return 0

    logger.info("Found %d markdown files to index.", len(md_files))

    # 1. Chunk
    all_chunks: List[Chunk] = []
    for md_path in md_files:
        chunks = chunk_markdown_file(
            md_path,
            max_chunk_size=max_chunk_size,
            chunk_overlap=chunk_overlap,
            year=year,
        )
        all_chunks.extend(chunks)

    logger.info("Total chunks after splitting: %d", len(all_chunks))

    # 2. Classify
    all_chunks = classify_chunks(
        all_chunks,
        use_llm=use_llm_classification,
        model=classification_model,
        batch_size=classification_batch_size,
        delay=classification_delay,
    )

    # 3. (Optional) Generate summaries for multi-representation indexing
    if generate_chunk_summaries:
        all_chunks = generate_summaries(all_chunks, model=classification_model)

    # 4. Embed
    embedder = Embedder()
    embedded_chunks: List[EmbeddedChunk] = embedder.embed_chunks(all_chunks)

    # 5. Store
    store = VectorStore()
    store.connect()
    try:
        if drop_existing:
            store.drop_table()
        store.create_table(embedding_dim=embedder.dimension)
        inserted = store.insert_chunks(embedded_chunks)
        logger.info("Indexing complete – %d chunks stored.", inserted)
        return inserted
    finally:
        store.close()


def index_from_pdfs(
    pdf_dir: Optional[str] = None,
    output_dir: Optional[str] = None,
    **kwargs,
) -> int:
    """Parse PDFs first, then run the indexing pipeline on the output."""
    generated = parse_pdfs(pdf_dir=pdf_dir, output_dir=output_dir)
    if not generated:
        logger.warning("No markdown files were generated from PDFs.")
        return 0
    # Use the output directory as the markdown source
    md_dir = output_dir or config.get("paths.markdown_data", "data/1_markdown")
    return index_documents(markdown_dir=md_dir, **kwargs)
