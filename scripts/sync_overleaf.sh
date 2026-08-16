#!/usr/bin/env bash
#
# Push the dissertation/ folder to Overleaf.
#
# The repository is the source of truth; Overleaf is a read-only mirror kept
# up to date for supervisor review. Two modes:
#
#   ./scripts/sync_overleaf.sh            # git bridge push (needs OVERLEAF_PROJECT_ID)
#   ./scripts/sync_overleaf.sh --zip      # build a zip to upload by hand
#
# The git bridge requires an Overleaf paid or institutional plan. Set the
# project id once (it is the 24-character hex string in the project URL,
# https://www.overleaf.com/project/<id> — not the share-link token):
#
#   git config overleaf.projectid <id>
#
# Authentication is handled by git itself. Overleaf accepts only git tokens,
# and the username must be the literal "git" — not your email, which returns
# 403. The remote URL below embeds it, so git only asks for the token; the
# macOS keychain remembers it. This script never handles the secret.

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

PREFIX="dissertation"

if [[ "${1:-}" == "--zip" ]]; then
    OUT="${ROOT_DIR}/dissertation-overleaf.zip"
    rm -f "$OUT"
    # Ship sources only: no build artifacts, no compiled PDF.
    (cd "$PREFIX" && zip -r -q "$OUT" . \
        -x '*.aux' '*.bbl' '*.blg' '*.fdb_latexmk' '*.fls' '*.acn' '*.acr' \
           '*.alg' '*.glg' '*.glo' '*.gls' '*.glsdefs' '*.idx' '*.ilg' \
           '*.ind' '*.ist' '*.lof' '*.log' '*.lot' '*.out' '*.synctex.gz' \
           '*.toc' '*.xdv' '*.pdf' '.gitignore')
    echo "[overleaf] wrote $OUT"
    echo "[overleaf] upload it in Overleaf: Menu > Import from > Zip file"
    exit 0
fi

PROJECT_ID="${OVERLEAF_PROJECT_ID:-$(git config --get overleaf.projectid || true)}"
if [[ -z "$PROJECT_ID" ]]; then
    echo "[overleaf] no project id configured." >&2
    echo "[overleaf] run: git config overleaf.projectid <24-char-id-from-project-url>" >&2
    echo "[overleaf] or use: $0 --zip" >&2
    exit 1
fi

REMOTE_URL="https://git@git.overleaf.com/${PROJECT_ID}"
if git remote get-url overleaf >/dev/null 2>&1; then
    git remote set-url overleaf "$REMOTE_URL"
else
    git remote add overleaf "$REMOTE_URL"
fi

# git subtree rewrites dissertation/ history so the folder becomes the repo
# root on the Overleaf side, which is where Overleaf expects dissertation.tex.
echo "[overleaf] pushing ${PREFIX}/ to ${REMOTE_URL} (branch master)..."
git subtree push --prefix="$PREFIX" overleaf master
echo "[overleaf] done."
