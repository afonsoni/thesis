"""
End-to-end indexing pipeline.

Chains: chunk → classify → embed → store.
"""

import glob
import json
import logging
import os
from collections import Counter
from datetime import datetime
from typing import Any, Dict, List, Optional

from src.rag.common.models import Chunk, ChunkStrategy, EmbeddedChunk
from src.rag.indexing.chunker import chunk_markdown_file
from src.rag.indexing.classifier import classify_chunks
from src.rag.indexing.embedder import Embedder
from src.rag.indexing.store import VectorStore
from src.utils.config_loader import config

logger = logging.getLogger(__name__)


def _discover_markdown_files(directory: str) -> List[str]:
    """Recursively find the indexable .md files under *directory*.

    Skips ``_raw/``, where unprocessed parser output lives: indexing it next to
    the cleaned file would put every party in the index twice.
    """
    files = glob.glob(os.path.join(directory, "**", "*.md"), recursive=True)
    files = sorted(f for f in files if "_raw" not in os.path.relpath(f, directory).split(os.sep))
    per_dir = Counter(os.path.dirname(f) for f in files)
    crowded = [d for d, n in per_dir.items() if n > 1]
    if crowded:
        raise ValueError(
            f"More than one markdown per party folder in {crowded}: keep one "
            "(e.g. *-manual.md or *-clean.md) so the party is not indexed twice."
        )
    return files


def _build_default_checkpoint_path(
    md_files: List[str],
    processed_dir: str,
    party_filter: Optional[str],
) -> str:
    """Build a deterministic checkpoint filename in the processed-data directory."""
    os.makedirs(processed_dir, exist_ok=True)

    if len(md_files) == 1:
        base_name = os.path.splitext(os.path.basename(md_files[0]))[0]
        file_name = f"{base_name}-classified.json"
    else:
        now = datetime.now().strftime("%Y%m%d-%H%M%S")
        safe_filter = (party_filter or "all").replace(" ", "-").replace("/", "-")
        file_name = f"{safe_filter}-classified-{now}.json"

    return os.path.join(processed_dir, file_name)


def save_classified_chunks(
    chunks: List[Chunk],
    output_path: str,
    source_files: Optional[List[str]] = None,
) -> str:
    """Persist classified chunks to JSON for later embed/store reuse."""
    payload: Dict[str, Any] = {
        "format_version": 1,
        "chunk_count": len(chunks),
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source_files": source_files or [],
        "chunks": [c.model_dump() for c in chunks],
    }

    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)

    logger.info("Saved classified checkpoint with %d chunks to %s", len(chunks), output_path)
    return output_path


def load_classified_chunks(input_path: str) -> List[Chunk]:
    """Load classified chunks from checkpoint JSON format."""
    with open(input_path, "r", encoding="utf-8") as fh:
        raw = json.load(fh)
    if not isinstance(raw, dict) or not isinstance(raw.get("chunks"), list):
        raise ValueError(f"Invalid classified JSON format: missing 'chunks' list in {input_path}")
    loaded = [Chunk(**item) for item in raw["chunks"]]
    logger.info("Loaded %d classified chunks from %s", len(loaded), input_path)
    return loaded


def index_documents(
    markdown_dir: Optional[str] = None,
    party_filter: Optional[str] = None,
    chunk_strategy: Optional[str] = None,
    use_llm_classification: Optional[bool] = None,
    drop_existing: bool = False,
    classified_input_path: Optional[str] = None,
    classify_only: bool = False,
    contextual_headers: bool = False,
    table: Optional[str] = None,
) -> int:
    """
    Chunk, classify, embed and store the markdown manifestos; return the chunks stored.

    Args:
        markdown_dir: Root of the ``.md`` corpus (default ``paths.markdown_data``).
        party_filter: Only index files whose path contains this string, e.g. ``"livre"``.
        chunk_strategy: ``char`` / ``token`` / ``small_to_big`` (default
            ``indexing.chunk_strategy``); see :class:`ChunkStrategy`.
        use_llm_classification: Override ``indexing.use_llm_classification``.
            Without it chunks keep the default ``["outros"]`` topic, so topic
            filtering and ``topic_exploration`` routing will not work.
        drop_existing: Drop and recreate the table first.
        classified_input_path: Load a classified checkpoint instead of chunking
            and classifying again.
        classify_only: Stop after writing the classified checkpoint (no DB).
        contextual_headers: Embed ``party | section path`` + text instead of the
            bare text (see :meth:`Embedder.embed_chunks`). Stored content is unchanged.
        table: Write to this table instead of ``postgresql.table_name``.

    Every classifying run writes a checkpoint to ``paths.processed_data``.
    Sizes, models and batching come from the ``indexing`` config section.
    """
    markdown_dir = str(markdown_dir or config.get("paths.markdown_data", "data/1_markdown"))
    strategy = ChunkStrategy(
        chunk_strategy or config.get("indexing.chunk_strategy", ChunkStrategy.CHAR.value)
    )
    classify = bool(
        use_llm_classification
        if use_llm_classification is not None
        else config.get("indexing.use_llm_classification", True)
    )
    if classify_only and not classify:
        raise ValueError("--classify-only requires LLM classification to be enabled")
    if classify_only and classified_input_path:
        raise ValueError("--classify-only cannot be combined with --from-classified")

    if classified_input_path:
        all_chunks = load_classified_chunks(classified_input_path)
    else:
        md_files = _discover_markdown_files(markdown_dir)
        if party_filter:
            md_files = [f for f in md_files if party_filter.lower() in f.lower()]
        if not md_files:
            logger.warning("No markdown files found in %s (filter=%s)", markdown_dir, party_filter)
            return 0
        logger.info("Found %d markdown files to index.", len(md_files))

        # 1. Chunk. Size and overlap are characters under ``char`` and tokens
        # otherwise, so each unit has its own config keys.
        if strategy is ChunkStrategy.CHAR:
            size, overlap = config.get("indexing.max_chunk_size", 1000), config.get("indexing.chunk_overlap", 100)
        else:
            size, overlap = config.get("indexing.max_chunk_tokens", 112), config.get("indexing.chunk_overlap_tokens", 24)
        max_parent_tokens = config.get("indexing.max_parent_tokens")
        all_chunks = []
        for md_path in md_files:
            all_chunks.extend(chunk_markdown_file(
                md_path,
                max_chunk_size=int(size),
                chunk_overlap=int(overlap),
                year=int(config.get("indexing.year", 2024)),
                strategy=strategy,
                tokenizer_name=str(config.get("embeddings.model")),
                max_parent_size=int(max_parent_tokens) if max_parent_tokens else None,
            ))
        logger.info("Total chunks after splitting: %d", len(all_chunks))

        # 2. Classify, and checkpoint the result. An unclassified run writes no
        # checkpoint: it would look classified and poison a later --from-classified.
        if classify:
            all_chunks = classify_chunks(
                all_chunks,
                model=str(config.get(
                    "indexing.classification_model",
                    config.get("llm.openrouter.model", "google/gemma-4-31b-it:free"),
                )),
                batch_size=int(config.get("indexing.classification_batch_size", 15)),
                delay=float(config.get("indexing.classification_delay", 1.0)),
            )
            processed_dir = str(config.get("paths.processed_data", "data/2_processed"))
            save_classified_chunks(
                all_chunks,
                output_path=_build_default_checkpoint_path(md_files, processed_dir, party_filter),
                source_files=md_files,
            )
        else:
            logger.warning(
                "LLM classification disabled – %d chunks keep their default topics. "
                "Topic filtering and topic_exploration routing will not work on this index.",
                len(all_chunks),
            )

    if classify_only:
        logger.info("Classify-only mode complete – %d chunks processed.", len(all_chunks))
        return len(all_chunks)

    # 3. Embed
    embedder = Embedder()
    embedded_chunks: List[EmbeddedChunk] = embedder.embed_chunks(all_chunks, contextual=contextual_headers)

    # 4. Store
    store = VectorStore()
    if table:
        store.table = table
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
