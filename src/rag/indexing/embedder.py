"""
Embedding generation using the Portuguese sentence encoder.

Supports single and batch encoding, plus optional multi-representation
indexing (LLM-generated summaries for improved retrieval).
"""

import logging
from typing import List, Optional

from sentence_transformers import SentenceTransformer

from src.rag.common.models import Chunk, EmbeddedChunk
from src.utils.config_loader import config

logger = logging.getLogger(__name__)


class Embedder:
    """Wraps a SentenceTransformer model for encoding text into vectors."""

    def __init__(self, model_name: Optional[str] = None):
        model_name = model_name or config.get(
            "embeddings.model",
            "PORTULAN/serafim-900m-portuguese-pt-sentence-encoder-ir",
        )
        logger.info("Loading embedding model: %s", model_name)
        self.model = SentenceTransformer(model_name)
        self.dimension: int = self.model.get_sentence_embedding_dimension()
        logger.info("Embedding dimension: %d", self.dimension)

    # ------------------------------------------------------------------
    # Core encoding
    # ------------------------------------------------------------------

    def encode(self, text: str) -> List[float]:
        """Encode a single text string into a vector."""
        return self.model.encode(text, normalize_embeddings=True).tolist()

    def encode_batch(self, texts: List[str], batch_size: int = 64) -> List[List[float]]:
        """Encode a list of texts in batches."""
        embeddings = self.model.encode(
            texts,
            batch_size=batch_size,
            show_progress_bar=True,
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
    model: str = "gemini-2.5-flash",
) -> List[Chunk]:
    """
    Generate short LLM summaries for each chunk (multi-representation indexing).

    The summary is stored in ``chunk.summary`` and used for embedding,
    while the full ``chunk.content`` is kept for generation context.

    This improves retrieval for bullet-point-heavy manifesto sections
    where the raw text may not match well with natural-language queries.
    """
    import os
    from google import genai  # lazy import

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    logger.info("Generating summaries for %d chunks …", len(chunks))

    prompt_template = (
        "Resume o seguinte excerto de um programa político português "
        "numa frase curta e clara em português. Mantém os temas principais.\n\n"
        "EXCERTO:\n{content}\n\nRESUMO:"
    )

    for i, chunk in enumerate(chunks):
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt_template.format(content=chunk.content[:2000]),
            )
            chunk.summary = response.text.strip()
        except Exception as exc:
            logger.warning("Summary generation failed for chunk %s: %s", chunk.id, exc)
            # Leave summary as None – embedder will fall back to content

        if (i + 1) % 25 == 0:
            logger.info("Generated summaries for %d / %d chunks", i + 1, len(chunks))

    logger.info("Summary generation complete.")
    return chunks
