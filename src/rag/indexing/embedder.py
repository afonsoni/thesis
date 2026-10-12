"""
Embedding generation with a SentenceTransformer encoder (Qwen3-Embedding by default).

Retrieval encoders are asymmetric: queries get an instruction prefix, documents
none. ``encode_query`` / ``encode_document`` from sentence-transformers apply
whichever prompt the model declares, so search must go through
:meth:`Embedder.encode_query`.
"""

import logging
from typing import List, Optional

from sentence_transformers import SentenceTransformer

from src.rag.common.models import Chunk, EmbeddedChunk, section_path
from src.utils.config_loader import config

logger = logging.getLogger(__name__)


def _pools_last_token(model: SentenceTransformer) -> bool:
    """True for decoder-based encoders (e.g. Qwen3-Embedding) that pool the last token."""
    return any(
        getattr(m, "pooling_mode", None) == "lasttoken" or getattr(m, "pooling_mode_lasttoken", False)
        for m in model.modules()
    )


class Embedder:
    """Wraps a SentenceTransformer model for encoding text into vectors."""

    def __init__(self, model_name: Optional[str] = None):
        model_name = model_name or config.get("embeddings.model")
        logger.info("Loading embedding model: %s", model_name)
        # The cached copy first: an online load spends 5-12 s asking the Hub
        # whether the files changed, an offline one 0.7 s. Download only if absent.
        try:
            self.model = SentenceTransformer(model_name, local_files_only=True)
        except OSError:
            self.model = SentenceTransformer(model_name)

        # Left padding, as Qwen3-Embedding's model card specifies. Pooling is correct
        # either way (sentence-transformers uses the attention mask), but the side
        # shifts bf16 vectors by ~3e-3, so it stays fixed for reproducible indexes.
        if _pools_last_token(self.model):
            self.model.tokenizer.padding_side = "left"

        # Optional cap on the encoder's window; anything past it is truncated silently.
        max_seq_length = config.get("embeddings.max_seq_length", None)
        if max_seq_length:
            self.model.max_seq_length = int(max_seq_length)

        self.dimension: int = self.model.get_embedding_dimension()
        logger.info(
            "Embedding dimension: %d | max_seq_length: %s | prompts: %s",
            self.dimension,
            self.model.max_seq_length,
            sorted(k for k, v in self.model.prompts.items() if v) or "none",
        )

    def encode_query(self, text: str, instruction: Optional[str] = None) -> List[float]:
        """Encode search text, with the model's query instruction when it has one.

        *instruction* replaces the shipped task sentence, in Qwen3-Embedding's
        ``Instruct: <task>\\nQuery:`` format (the model card recommends a
        task-specific one, written in English).
        """
        prompt = f"Instruct: {instruction}\nQuery:" if instruction else None
        return self.model.encode_query(text, prompt=prompt, normalize_embeddings=True).tolist()

    def embed_chunks(
        self, chunks: List[Chunk], batch_size: int = 64, contextual: bool = False,
    ) -> List[EmbeddedChunk]:
        """Encode each chunk's ``content`` as a document and attach the vector.

        With *contextual*, the embedded text is prefixed with ``party | section
        path``: a windowed child past the first carries no heading of its own (58%
        of chunks), so its vector cannot tell which section it belongs to. A chunk's
        LLM-written ``context``, when it has one, is prefixed too. Only the embedded
        text changes; ``content`` (and so every gold key) does not.
        """
        texts = [f"{c.context}\n{c.content}" if c.context else c.content for c in chunks]
        if contextual:
            texts = [
                f"{' | '.join(filter(None, [c.party_name, section_path(c.metadata)]))}\n{t}"
                for c, t in zip(chunks, texts)
            ]
        logger.info("Embedding %d chunks (batch_size=%d) …", len(texts), batch_size)
        vectors = self.model.encode_document(
            texts, batch_size=batch_size, show_progress_bar=True, normalize_embeddings=True,
        ).tolist()
        embedded = [EmbeddedChunk(**c.model_dump(), embedding=v) for c, v in zip(chunks, vectors)]
        logger.info("Embedding complete – %d vectors generated.", len(embedded))
        return embedded
