"""
Embedding generation using the Portuguese sentence encoder.

Supports single and batch encoding, plus optional multi-representation
indexing (LLM-generated summaries for improved retrieval).
"""

import inspect
import json
import logging
from typing import List, Optional

from huggingface_hub import hf_hub_download
from sentence_transformers import SentenceTransformer

from src.rag.common.models import Chunk, EmbeddedChunk
from src.rag.common.llm_client import generate_text
from src.utils.config_loader import config

logger = logging.getLogger(__name__)


def _uses_last_token_pooling(model_name: str) -> bool:
    """Whether the model's SentenceTransformer pooling config uses last-token pooling.

    Read from the model repo's ``1_Pooling/config.json`` before the model is built,
    because the tokenizer's padding side has to be set at construction time.
    Returns False if the file cannot be read — the safe default for the
    mean/CLS-pooling models where padding side does not matter.
    """
    try:
        path = hf_hub_download(repo_id=model_name, filename="1_Pooling/config.json")
        with open(path, "r", encoding="utf-8") as fh:
            return bool(json.load(fh).get("pooling_mode_lasttoken", False))
    except Exception as exc:  # offline, local path, or non-ST repo layout
        logger.debug("Could not read pooling config for %s: %s", model_name, exc)
        return False


class Embedder:
    """Wraps a SentenceTransformer model for encoding text into vectors."""

    def __init__(self, model_name: Optional[str] = None):
        model_name = model_name or config.get(
            "embeddings.model",
            "Qwen/Qwen3-Embedding-0.6B",
        )
        logger.info("Loading embedding model: %s", model_name)

        # Last-token pooling models (Qwen3-Embedding and other decoder-based
        # encoders) MUST pad on the left: with right padding, the "last token" of
        # a short sequence in a mixed-length batch is a PAD token, so the whole
        # embedding is garbage. It fails silently — no error, just bad vectors —
        # so detect it from the model card rather than relying on config.
        model_kwargs = {}
        if _uses_last_token_pooling(model_name):
            # sentence-transformers renamed tokenizer_kwargs -> processor_kwargs.
            # Pick whichever the installed version accepts: passing the retired name
            # would eventually be ignored, and silently ignoring it reintroduces the
            # corruption this guards against.
            param = (
                "processor_kwargs"
                if "processor_kwargs" in inspect.signature(SentenceTransformer).parameters
                else "tokenizer_kwargs"
            )
            model_kwargs[param] = {"padding_side": "left"}

        self.model = SentenceTransformer(model_name, **model_kwargs)

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
