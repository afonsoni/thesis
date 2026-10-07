"""
End-to-end indexing pipeline.

Chains: parse → chunk → classify → (optional: summarise) → embed → store.
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
from src.rag.indexing.embedder import Embedder, generate_summaries
from src.rag.indexing.parser import parse_pdfs
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

    raw_chunks = raw.get("chunks") if isinstance(raw, dict) else None
    if not isinstance(raw_chunks, list):
        raise ValueError(f"Invalid classified JSON format: missing 'chunks' list in {input_path}")

    loaded: List[Chunk] = []
    for idx, item in enumerate(raw_chunks):
        if not isinstance(item, dict):
            logger.warning("Skipping non-object chunk at index %d in %s", idx, input_path)
            continue

        chunk_data = dict(item)
        chunk_data.setdefault("year", int(config.get("indexing.year", 2024)))
        loaded.append(Chunk(**chunk_data))

    logger.info("Loaded %d classified chunks from %s", len(loaded), input_path)
    return loaded


def index_documents(
    markdown_dir: Optional[str] = None,
    party_filter: Optional[str] = None,
    generate_chunk_summaries: bool = False,
    classification_model: Optional[str] = None,
    classification_batch_size: Optional[int] = None,
    classification_delay: Optional[float] = None,
    max_chunk_size: Optional[int] = None,
    chunk_overlap: Optional[int] = None,
    chunk_strategy: Optional[str] = None,
    use_llm_classification: Optional[bool] = None,
    year: int = 2024,
    drop_existing: bool = False,
    classified_input_path: Optional[str] = None,
    checkpoint_output_path: Optional[str] = None,
    classify_only: bool = False,
    save_checkpoint: bool = True,
) -> int:
    """
    Run the full indexing pipeline on markdown files.

    Args:
        markdown_dir: Directory containing ``.md`` files (subfolders supported).
                      Defaults to config ``paths.markdown_data``.
        party_filter: If set, only index files whose path contains this string
                      (case-insensitive). E.g. ``"livre"`` or ``"ps"``.
        generate_chunk_summaries: Generate LLM summaries for multi-representation indexing.
        classification_model: OpenRouter model name for classification.
        classification_batch_size: Number of chunks per classification API request.
        classification_delay: Delay between classification API requests.
        max_chunk_size: Max chunk size — characters under the ``char`` strategy,
            tokens under the token strategies. Defaults per-strategy from config.
        chunk_overlap: Overlap for windowed chunks, in the same unit.
        chunk_strategy: One of ``char`` / ``token`` / ``small_to_big``
            (see :class:`ChunkStrategy`). Defaults to ``indexing.chunk_strategy``.
        use_llm_classification: Run LLM topic classification over the chunks.
            Defaults to ``indexing.use_llm_classification``. When disabled, chunk
            topics stay at their default ``["outros"]``, so topic filtering and
            ``topic_exploration`` routing will not work against the index.
        year: Election year metadata.
        drop_existing: Drop and recreate the table before indexing.
        classified_input_path: Load pre-classified chunks from JSON and skip chunk/classify.
        checkpoint_output_path: Save classified chunks to this JSON path.
        classify_only: Stop after classification checkpoint generation.
        save_checkpoint: Persist checkpoints during normal index runs.

    Returns:
        Total number of chunks stored.
    """
    markdown_dir = str(markdown_dir or config.get("paths.markdown_data", "data/1_markdown"))
    strategy = ChunkStrategy(
        chunk_strategy or config.get("indexing.chunk_strategy", ChunkStrategy.CHAR.value)
    )
    embedding_model = str(config.get("embeddings.model"))
    max_parent_tokens = config.get("indexing.max_parent_tokens")
    max_parent_tokens = int(max_parent_tokens) if max_parent_tokens else None
    # Size/overlap live under different config keys per strategy, because the two
    # are measured in different units and are not interchangeable.
    if strategy is ChunkStrategy.CHAR:
        max_chunk_size = int(max_chunk_size or config.get("indexing.max_chunk_size", 1000))
        chunk_overlap = int(chunk_overlap or config.get("indexing.chunk_overlap", 100))
    else:
        max_chunk_size = int(max_chunk_size or config.get("indexing.max_chunk_tokens", 112))
        chunk_overlap = int(chunk_overlap or config.get("indexing.chunk_overlap_tokens", 24))
    classification_model = str(
        classification_model
        or config.get(
            "indexing.classification_model",
            config.get("llm.openrouter.model", "google/gemma-4-31b-it:free"),
        )
    )
    classification_batch_size = int(
        classification_batch_size or config.get("indexing.classification_batch_size", 15)
    )
    classification_delay = float(
        classification_delay
        if classification_delay is not None
        else config.get("indexing.classification_delay", 1.0)
    )
    classify = bool(
        use_llm_classification
        if use_llm_classification is not None
        else config.get("indexing.use_llm_classification", True)
    )
    md_files: List[str] = []

    if classify_only and not classify:
        raise ValueError("--classify-only requires LLM classification to be enabled")

    if classified_input_path:
        if classify_only:
            raise ValueError("--classify-only cannot be combined with --from-classified")
        all_chunks = load_classified_chunks(classified_input_path)
    else:
        md_files = _discover_markdown_files(markdown_dir)

        if party_filter:
            md_files = [f for f in md_files if party_filter.lower() in f.lower()]

        if not md_files:
            logger.warning("No markdown files found in %s (filter=%s)", markdown_dir, party_filter)
            return 0

        logger.info("Found %d markdown files to index.", len(md_files))

        # 1. Chunk
        all_chunks = []
        for md_path in md_files:
            chunks = chunk_markdown_file(
                md_path,
                max_chunk_size=max_chunk_size,
                chunk_overlap=chunk_overlap,
                year=year,
                strategy=strategy,
                tokenizer_name=embedding_model,
                max_parent_size=max_parent_tokens,
            )
            all_chunks.extend(chunks)

        logger.info("Total chunks after splitting: %d", len(all_chunks))

        # 2. Classify. Skipping this leaves every chunk on its default ``["outros"]``
        # topic, which costs no OpenRouter quota but disables topic filtering and
        # topic_exploration routing for the resulting index.
        if classify:
            all_chunks = classify_chunks(
                all_chunks,
                model=classification_model,
                batch_size=classification_batch_size,
                delay=classification_delay,
            )
        else:
            logger.warning(
                "LLM classification disabled – %d chunks keep their default topics. "
                "Topic filtering and topic_exploration routing will not work on this index.",
                len(all_chunks),
            )

        # An unclassified run has nothing worth checkpointing: the JSON would look
        # like a classified checkpoint and silently poison a later --from-classified.
        should_checkpoint = classify and (save_checkpoint or checkpoint_output_path or classify_only)
        if should_checkpoint:
            processed_dir = str(config.get("paths.processed_data", "data/2_processed"))
            output_path = checkpoint_output_path or _build_default_checkpoint_path(md_files, processed_dir, party_filter)
            save_classified_chunks(all_chunks, output_path=output_path, source_files=md_files)

    # 3. (Optional) Generate summaries for multi-representation indexing
    if generate_chunk_summaries:
        all_chunks = generate_summaries(all_chunks, model=classification_model)

    if classify_only:
        logger.info("Classify-only mode complete – %d chunks processed.", len(all_chunks))
        return len(all_chunks)

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
