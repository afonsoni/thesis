"""
Stable content-based keys for evaluation ground truth.

Retrieval ground truth is matched by a hash of chunk *content*, not by the
database UUID. ``VectorStore.insert_chunks`` mints a fresh UUID on every insert
and re-indexing (``--drop``) re-mints them, so ids are unstable across index
rebuilds. Content, on the other hand, is stable as long as the chunking
parameters do not change — so a content hash lets a gold set survive re-indexing.
"""

from __future__ import annotations

import hashlib
import re
import unicodedata

_WS_RE = re.compile(r"\s+")


def normalize_content(content: str) -> str:
    """Normalize chunk text for stable hashing (NFC, trimmed, whitespace-collapsed)."""
    text = unicodedata.normalize("NFC", content or "")
    text = _WS_RE.sub(" ", text).strip()
    return text


def chunk_key(content: str) -> str:
    """Return a stable ``sha1:<hex>`` key for a chunk's content."""
    digest = hashlib.sha1(normalize_content(content).encode("utf-8")).hexdigest()
    return f"sha1:{digest}"
