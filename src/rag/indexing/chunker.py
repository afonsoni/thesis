"""
Markdown chunking for political manifestos.

Uses LangChain's MarkdownHeaderTextSplitter for header-aware splitting,
followed by RecursiveCharacterTextSplitter for large-chunk windowing.
Attaches party metadata from the filename.
"""

import logging
import os
import re
from typing import Any, Dict, List, Optional

from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)

from src.rag.common.models import Chunk, get_party_info

logger = logging.getLogger(__name__)

# Header hierarchy tailored for Portuguese political documents
HEADERS_TO_SPLIT_ON = [
    ("#", "Title"),
    ("##", "Major_Section"),
    ("###", "Policy_Area"),
    ("####", "Policy_Topic"),
    ("#####", "Subsection"),
    ("######", "Details"),
]

# Minimum content length to keep a chunk (avoids noise)
MIN_CHUNK_CHARS = 50


def chunk_markdown(
    markdown_content: str,
    file_name: str,
    max_chunk_size: int = 1000,
    chunk_overlap: int = 100,
    year: int = 2024,
) -> List[Chunk]:
    """
    Split a political manifesto markdown into semantically meaningful chunks.

    1. **Header splitting** – respects the document's header hierarchy
       so that each chunk inherits its section context.
    2. **Windowed splitting** – any chunk larger than *max_chunk_size*
       is further split with overlap to avoid losing context.

    Args:
        markdown_content: Raw markdown text.
        file_name: Original file name (used to derive party metadata).
        max_chunk_size: Maximum characters per chunk.
        chunk_overlap: Overlap characters between windowed sub-chunks.
        year: Election year for metadata.

    Returns:
        List of ``Chunk`` objects ready for classification & embedding.
    """
    party_info = get_party_info(file_name)

    # Stage 1 – split by markdown headers
    md_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=HEADERS_TO_SPLIT_ON,
        strip_headers=False,
    )
    header_chunks = md_splitter.split_text(markdown_content)

    # Stage 2 – recursive splitter for oversized chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=max_chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", "! ", "? ", ", ", " ", ""],
    )

    chunks: List[Chunk] = []

    for header_chunk in header_chunks:
        content = header_chunk.page_content.strip()
        if len(content) <= MIN_CHUNK_CHARS:
            continue

        base_metadata: Dict[str, Any] = dict(header_chunk.metadata)

        if len(content) <= max_chunk_size:
            # Fits in one chunk
            chunks.append(
                Chunk(
                    content=content,
                    metadata=base_metadata,
                    party_name=party_info["name"],
                    ideology=party_info["ideology"],
                    year=year,
                    size=len(content),
                    word_count=len(content.split()),
                    chunk_type="header_only",
                )
            )
        else:
            # Window into sub-chunks
            sub_texts = text_splitter.split_text(content)
            for idx, sub_text in enumerate(sub_texts):
                enhanced_meta = {
                    **base_metadata,
                    "sub_chunk_index": idx,
                    "total_sub_chunks": len(sub_texts),
                    "parent_chunk_size": len(content),
                }
                chunks.append(
                    Chunk(
                        content=sub_text,
                        metadata=enhanced_meta,
                        party_name=party_info["name"],
                        ideology=party_info["ideology"],
                        year=year,
                        size=len(sub_text),
                        word_count=len(sub_text.split()),
                        chunk_type="windowed",
                    )
                )

    logger.info(
        "Chunked %s → %d chunks (party=%s)",
        file_name,
        len(chunks),
        party_info["name"],
    )
    return chunks


def chunk_markdown_file(
    file_path: str,
    max_chunk_size: int = 1000,
    chunk_overlap: int = 100,
    year: int = 2024,
) -> List[Chunk]:
    """Convenience wrapper that reads a markdown file and chunks it."""
    with open(file_path, "r", encoding="utf-8") as fh:
        content = fh.read()
    file_name = os.path.basename(file_path)
    return chunk_markdown(content, file_name, max_chunk_size, chunk_overlap, year)
