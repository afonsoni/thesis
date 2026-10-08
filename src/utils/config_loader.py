"""
Read ``config/config.yaml`` once and look keys up by dotted path.

The YAML is the single source of truth: a key the code reads but the file lacks
raises, instead of silently falling back to a default written somewhere in the
code. Pass a default only for keys that are optional by design (e.g.
``embeddings.max_seq_length``).
"""

import os
from typing import Any

import yaml

CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "config",
    "config.yaml",
)
_REQUIRED = object()


class Config:
    def __init__(self, path: str = CONFIG_PATH):
        with open(path, encoding="utf-8") as fh:
            self._data = yaml.safe_load(fh) or {}

    def get(self, path: str, default: Any = _REQUIRED) -> Any:
        """Value at dotted *path*, e.g. ``"retrieval.rrf_k"``; *default* only if given."""
        value: Any = self._data
        for part in path.split("."):
            if not isinstance(value, dict) or part not in value:
                if default is _REQUIRED:
                    raise KeyError(f"{path!r} is missing from {CONFIG_PATH}")
                return default
            value = value[part]
        return value


config = Config()
