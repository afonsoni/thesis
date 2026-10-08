"""
Re-chunk the indexable markdown with the current chunker settings and carry each
chunk's topics over from its classified checkpoint, matched by content hash.

For chunker changes that leave the embedded ``content`` untouched (e.g. the
``indexing.max_parent_tokens`` cap on ``parent_content``): the checkpoints are
rewritten in place without a single classification call. Fails if any chunk's
content has no classified match, since that means the change was not
content-preserving and the party needs a real reclassification.

Usage: python scripts/rebuild_parents.py   # then re-index with --from-classified
"""

import glob
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.rag.common.models import Chunk, ChunkStrategy  # noqa: E402
from src.rag.indexing.chunker import chunk_markdown_file  # noqa: E402
from src.rag.indexing.pipeline import _discover_markdown_files, save_classified_chunks  # noqa: E402
from src.utils.config_loader import config  # noqa: E402

CARRIED = ("topics", "topic_classification")


def _key(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()


def main() -> None:
    processed = str(config.get("paths.processed_data", "data/2_processed"))
    checkpoints = {}
    for path in glob.glob(os.path.join(processed, "*-classified*.json")):
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        checkpoints.setdefault(tuple(data.get("source_files", [])), []).append((path, data["chunks"]))

    max_parent = config.get("indexing.max_parent_tokens")
    for md in _discover_markdown_files(str(config.get("paths.markdown_data", "data/1_markdown"))):
        chunks = chunk_markdown_file(
            md,
            max_chunk_size=int(config.get("indexing.max_chunk_tokens")),
            chunk_overlap=int(config.get("indexing.chunk_overlap_tokens")),
            year=int(config.get("indexing.year", 2024)),
            strategy=ChunkStrategy(config.get("indexing.chunk_strategy")),
            tokenizer_name=str(config.get("embeddings.model")),
            max_parent_size=int(max_parent) if max_parent else None,
        )
        wanted = {_key(c.content) for c in chunks}
        # A file can have several checkpoints (older chunking runs); use the one
        # that covers every current chunk.
        match = next(
            ((p, old) for p, old in checkpoints.get((md,), []) if wanted <= {_key(o["content"]) for o in old}),
            None,
        )
        if match is None:
            sys.exit(f"{md}: no checkpoint covers the current chunks; reclassify it with `index --party`.")
        path, old = match
        by_key = {_key(o["content"]): o for o in old}
        chunks = [
            Chunk.model_validate({**c.model_dump(), **{f: by_key[_key(c.content)].get(f) for f in CARRIED}})
            for c in chunks
        ]
        save_classified_chunks(chunks, output_path=path, source_files=[md])
        big = max((len(c.parent_content or c.content) for c in chunks), default=0)
        print(f"{os.path.basename(path):45} {len(chunks):4} chunks, largest context {big:6} chars")


if __name__ == "__main__":
    main()
