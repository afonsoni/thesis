"""
Embedding generation using the Portuguese sentence encoder.

Supports single and batch encoding, plus optional multi-representation
indexing (LLM-generated summaries for improved retrieval).
"""

import logging
from typing import List, Optional

from sentence_transformers import SentenceTransformer

from src.rag.common.models import Chunk, EmbeddedChunk
from src.rag.common.llm_client import generate_text
from src.utils.config_loader import config

logger = logging.getLogger(__name__)


def _pools_last_token(model: SentenceTransformer) -> bool:
    """Whether the loaded model pools the final token rather than averaging.

    True for decoder-based encoders such as Qwen3-Embedding. Reads the pooling
    module that is already in memory, so it needs no network call, and accepts
    both the current ``pooling_mode`` string and the older per-mode booleans.
    """
    for module in model.modules():
        if getattr(module, "pooling_mode", None) == "lasttoken":
            return True
        if getattr(module, "pooling_mode_lasttoken", False):
            return True
    return False


class Embedder:
    """Wraps a SentenceTransformer model for encoding text into vectors."""

    def __init__(self, model_name: Optional[str] = None):
        model_name = model_name or config.get(
            "embeddings.model",
            "Qwen/Qwen3-Embedding-0.6B",
        )
        logger.info("Loading embedding model: %s", model_name)
        self.model = SentenceTransformer(model_name)

        # Pad on the left for last-token-pooling encoders, as Qwen3-Embedding's
        # model card specifies. This is defensive rather than load-bearing:
        # sentence-transformers 5.x finds the final *unmasked* token via the
        # attention mask, so it already pools correctly with either padding side.
        # Kept because it costs nothing and the guarantee is the library's, not
        # the model's — a pooling path that indexed position -1 directly would
        # read a PAD token off a short sequence in a mixed-length batch.
        if _pools_last_token(self.model) and self.model.tokenizer.padding_side != "left":
            self.model.tokenizer.padding_side = "left"

        # Optional hard cap on the encoder's context window. This is the knob that
        # matters most for retrieval quality: anything beyond it is truncated
        # silently at encode time. Leave unset to use the model's own default.
        max_seq_length = config.get("embeddings.max_seq_length")
        if max_seq_length:
            self.model.max_seq_length = int(max_seq_length)

        dim = self.model.get_sentence_embedding_dimension()
        self.dimension: int = dim if dim is not None else int(config.get("embeddings.dimension", 1024))
        # Prompts a model declares for asymmetric retrieval (query vs document).
        self._prompts = dict(getattr(self.model, "prompts", None) or {})
        logger.info(
            "Embedding dimension: %d | max_seq_length: %s | prompts: %s",
            self.dimension,
            self.model.max_seq_length,
            sorted(k for k, v in self._prompts.items() if v) or "none",
        )

    # ------------------------------------------------------------------
    # Core encoding
    # ------------------------------------------------------------------

    def _prompt_name(self, kind: str) -> Optional[str]:
        """Return *kind* if the loaded model declares a non-empty prompt for it.

        Retrieval models are asymmetric: queries get an instruction prefix,
        documents get none. Passing a prompt name a model does not declare raises,
        and symmetric models (serafim, the STS-tuned ones) declare nothing at all —
        so both cases fall back to unprefixed encoding.
        """
        return kind if self._prompts.get(kind) else None

    def encode(self, text: str) -> List[float]:
        """Encode a single text as a *document* (the indexing side)."""
        return self.model.encode(
            text,
            prompt_name=self._prompt_name("document"),
            normalize_embeddings=True,
        ).tolist()

    def encode_query(self, text: str) -> List[float]:
        """Encode a single text as a *query*, applying the model's instruction
        prefix when it has one. Must be used for search-time encoding, or an
        asymmetric model silently loses the accuracy its prompts exist to add."""
        return self.model.encode(
            text,
            prompt_name=self._prompt_name("query"),
            normalize_embeddings=True,
        ).tolist()

    def encode_batch(self, texts: List[str], batch_size: int = 64) -> List[List[float]]:
        """Encode a list of texts as *documents*, in batches."""
        embeddings = self.model.encode(
            texts,
            batch_size=batch_size,
            show_progress_bar=True,
            prompt_name=self._prompt_name("document"),
            normalize_embeddings=True,
        )
        return embeddings.tolist()

    # ------------------------------------------------------------------
    # Chunk-level helpers
    # ------------------------------------------------------------------

    def embed_chunks(self, chunks: List[Chunk], batch_size: int = 64) -> List[EmbeddedChunk]:
        """
        Generate embeddings for a list of chunks.

        For each chunk the text used for embedding is:
        - the *summary* if present (multi-representation indexing), or
        - the full *content* otherwise.

        Returns:
            List of ``EmbeddedChunk`` objects with the ``embedding`` field populated.
        """
        texts = [c.summary or c.content for c in chunks]
        logger.info("Embedding %d chunks (batch_size=%d) …", len(texts), batch_size)
        vectors = self.encode_batch(texts, batch_size=batch_size)

        embedded: List[EmbeddedChunk] = []
        for chunk, vec in zip(chunks, vectors):
            ec = EmbeddedChunk(
                **chunk.model_dump(),
                embedding=vec,
            )
            embedded.append(ec)

        logger.info("Embedding complete – %d vectors generated.", len(embedded))
        return embedded


# ---------------------------------------------------------------------------
# Optional: multi-representation summary generation
# ---------------------------------------------------------------------------

def generate_summaries(
    chunks: List[Chunk],
    model: Optional[str] = None,
) -> List[Chunk]:
    """
    Generate short LLM summaries for each chunk (multi-representation indexing).

    The summary is stored in ``chunk.summary`` and used for embedding,
    while the full ``chunk.content`` is kept for generation context.

    This improves retrieval for bullet-point-heavy manifesto sections
    where the raw text may not match well with natural-language queries.
    """
    logger.info("Generating summaries for %d chunks …", len(chunks))

    prompt_template = (
        "Resume o seguinte excerto de um programa político português "
        "numa frase curta e clara em português. Mantém os temas principais.\n\n"
        "EXCERTO:\n{content}\n\nRESUMO:"
    )
    selected_model = model or str(
        config.get("llm.openrouter.model", "google/gemma-4-31b-it:free"),
    )

    for i, chunk in enumerate(chunks):
        try:
            summary = generate_text(
                prompt=prompt_template.format(content=chunk.content[:2000]),
                model=selected_model,
                temperature=0.2,
                max_tokens=180,
            )
            chunk.summary = summary.strip()
        except Exception as exc:
            logger.warning("Summary generation failed for chunk %s: %s", chunk.id, exc)
            # Leave summary as None – embedder will fall back to content

        if (i + 1) % 25 == 0:
            logger.info("Generated summaries for %d / %d chunks", i + 1, len(chunks))

    logger.info("Summary generation complete.")
    return chunks
