"""
Markdown chunking for political manifestos.

Uses LangChain's MarkdownHeaderTextSplitter for header-aware splitting,
followed by RecursiveCharacterTextSplitter for large-chunk windowing.
Attaches party metadata from the filename.
"""

import logging
import os
from typing import Any, Callable, Dict, List, Optional, Tuple

from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)

from src.rag.common.models import (
    HEADER_METADATA_KEYS,
    Chunk,
    ChunkStrategy,
    get_party_info,
)

logger = logging.getLogger(__name__)

# Header hierarchy tailored for Portuguese political documents
HEADERS_TO_SPLIT_ON = [
    ("#" * level, key)
    for level, key in enumerate(HEADER_METADATA_KEYS, start=1)
]

# Minimum content length to keep a chunk (avoids noise)
MIN_CHUNK_CHARS = 50

# Splitting boundaries, coarsest first — keep paragraphs and sentences intact
# where possible so a chunk stays semantically self-contained.
SEPARATORS = ["\n\n", "\n", ". ", "! ", "? ", ", ", " ", ""]


def _build_window_splitter(
    strategy: ChunkStrategy,
    max_chunk_size: int,
    chunk_overlap: int,
    tokenizer_name: Optional[str],
) -> Tuple[RecursiveCharacterTextSplitter, Callable[[str], int]]:
    """Build the windowing splitter and the size function it measures with.

    Under ``CHAR`` both are character-based (the historical baseline). Under the
    token strategies the splitter counts tokens with the *embedding model's own*
    tokenizer, so ``max_chunk_size`` becomes a token budget that the encoder can
    actually consume rather than a character count that silently overruns it.
    """
    if strategy is ChunkStrategy.CHAR:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=max_chunk_size,
            chunk_overlap=chunk_overlap,
            separators=SEPARATORS,
        )
        return splitter, len

    # Tokenizer only — avoids loading the full ~900M-parameter encoder just to count.
    from transformers import AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    splitter = RecursiveCharacterTextSplitter.from_huggingface_tokenizer(
        tokenizer,
        chunk_size=max_chunk_size,
        chunk_overlap=chunk_overlap,
        separators=SEPARATORS,
    )

    def count_tokens(text: str) -> int:
        return len(tokenizer.encode(text, add_special_tokens=False))

    return splitter, count_tokens


def _locate(content: str, pieces: List[str]) -> Optional[List[Tuple[int, int]]]:
    """Character span of each windowed piece inside *content*, in order.

    The splitter emits substrings of its input, overlapping by design, so each
    piece is searched for from just after the previous one's start. ``None`` if a
    piece cannot be found (the caller then falls back to the piece itself).
    """
    spans: List[Tuple[int, int]] = []
    cursor = 0
    for piece in pieces:
        start = content.find(piece, cursor)
        if start < 0:
            return None
        spans.append((start, start + len(piece)))
        cursor = start + 1
    return spans


def _bounded_parent(
    content: str,
    pieces: List[str],
    spans: Optional[List[Tuple[int, int]]],
    idx: int,
    measure: Callable[[str], int],
    max_parent_size: int,
) -> str:
    """Parent text for child *idx*: its whole section if that fits, else a window.

    Header sections are the natural parent, but a manifesto with only chapter
    headers (PAN: 14 for the whole document) makes every parent a whole chapter
    of 5-9k tokens, which crowds the generation prompt or does not fit in it. Past
    *max_parent_size*, the parent becomes the child plus as many neighbouring
    children as fit, grown one step at a time on alternating sides, cut from the
    section text so overlaps are not repeated.
    """
    if measure(content) <= max_parent_size:
        return content
    if spans is None:
        return pieces[idx]
    lo = hi = idx
    grew = True
    while grew:
        grew = False
        for a, b in ((lo - 1, hi), (lo, hi + 1)):
            if 0 <= a and b < len(spans) and measure(content[spans[a][0]:spans[b][1]]) <= max_parent_size:
                lo, hi = a, b
                grew = True
    return content[spans[lo][0]:spans[hi][1]]


def chunk_markdown(
    markdown_content: str,
    file_name: str,
    max_chunk_size: int = 1000,
    chunk_overlap: int = 100,
    year: int = 2024,
    strategy: ChunkStrategy = ChunkStrategy.CHAR,
    tokenizer_name: Optional[str] = None,
    max_parent_size: Optional[int] = None,
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
        max_chunk_size: Maximum chunk size, in characters under
            :attr:`ChunkStrategy.CHAR` and in *tokens* under the token
            strategies.
        chunk_overlap: Overlap between windowed sub-chunks, in the same unit.
        year: Election year for metadata.
        strategy: Windowing strategy. See :class:`ChunkStrategy` — the token
            strategies keep every chunk inside the encoder's context window,
            and ``SMALL_TO_BIG`` also records the parent section on each child.
        tokenizer_name: HF model id whose tokenizer defines the token budget.
            Required for the token strategies; ignored for ``CHAR``.
        max_parent_size: ``SMALL_TO_BIG`` only — cap on a child's parent, in
            tokens. A section over it gives each child a window of neighbouring
            children instead of the whole section. ``None`` keeps whole sections.

    Returns:
        List of ``Chunk`` objects ready for classification & embedding.
    """
    party_info = get_party_info(file_name)
    keep_parents = strategy is ChunkStrategy.SMALL_TO_BIG

    # Stage 1 – split by markdown headers
    md_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=HEADERS_TO_SPLIT_ON,
        strip_headers=False,
    )
    header_chunks = md_splitter.split_text(markdown_content)

    # Stage 2 – recursive splitter for oversized chunks
    text_splitter, measure = _build_window_splitter(
        strategy, max_chunk_size, chunk_overlap, tokenizer_name
    )

    chunks: List[Chunk] = []

    for header_chunk in header_chunks:
        content = header_chunk.page_content.strip()
        if len(content) <= MIN_CHUNK_CHARS:
            continue

        base_metadata: Dict[str, Any] = dict(header_chunk.metadata)

        if measure(content) <= max_chunk_size:
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
            spans = _locate(content, sub_texts) if keep_parents and max_parent_size else None
            for idx, sub_text in enumerate(sub_texts):
                parent = None
                if keep_parents:
                    parent = (
                        _bounded_parent(content, sub_texts, spans, idx, measure, max_parent_size)
                        if max_parent_size
                        else content
                    )
                enhanced_meta = {
                    **base_metadata,
                    "sub_chunk_index": idx,
                    "total_sub_chunks": len(sub_texts),
                    "parent_chunk_size": len(content),
                }
                chunks.append(
                    Chunk(
                        content=sub_text,
                        # Only the windowed children have a distinct parent to
                        # fall back to; header_only chunks already *are* it.
                        parent_content=parent,
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
        "Chunked %s → %d chunks (party=%s, strategy=%s, budget=%d %s)",
        file_name,
        len(chunks),
        party_info["name"],
        strategy.value,
        max_chunk_size,
        "chars" if strategy is ChunkStrategy.CHAR else "tokens",
    )
    return chunks


def chunk_markdown_file(
    file_path: str,
    max_chunk_size: int = 1000,
    chunk_overlap: int = 100,
    year: int = 2024,
    strategy: ChunkStrategy = ChunkStrategy.CHAR,
    tokenizer_name: Optional[str] = None,
    max_parent_size: Optional[int] = None,
) -> List[Chunk]:
    """Convenience wrapper that reads a markdown file and chunks it."""
    with open(file_path, "r", encoding="utf-8") as fh:
        content = fh.read()
    file_name = os.path.basename(file_path)
    return chunk_markdown(
        content,
        file_name,
        max_chunk_size,
        chunk_overlap,
        year,
        strategy=strategy,
        tokenizer_name=tokenizer_name,
        max_parent_size=max_parent_size,
    )
