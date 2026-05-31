#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "[tests] Starting dedicated test DB service..."
docker compose up -d postgres_test

echo "[tests] Running full pytest suite..."
python -m pytest -q
