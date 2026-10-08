#!/usr/bin/env bash
#
# Refresh the Overleaf mirror of dissertation/.
#
# The repository is the source of truth; Overleaf is a read-only copy kept up
# to date for supervisor review. Never edit the Overleaf copy — the next sync
# overwrites it.
#
#   ./scripts/sync_overleaf.sh          # build the upload bundle (free plan)
#   ./scripts/sync_overleaf.sh --git    # git-bridge push (paid plans only)
#
# Free-plan upload, once the bundle is built:
#   1. Open the project on overleaf.com.
#   2. Drag dissertation-overleaf.zip onto the project's file tree (or use
#      Upload and pick the zip). Overleaf extracts it and overwrites the
#      files it contains, so the project keeps its URL, its share links and
#      its comment history.
#
# The git bridge needs an Overleaf paid or institutional plan; on a free
# account it returns 403. It also requires token auth with the literal
# username "git" (an account email returns 403 with a misleading message).

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

PREFIX="dissertation"
OUT="${ROOT_DIR}/dissertation-overleaf.zip"

build_zip() {
    rm -f "$OUT"
    # Ship sources only: no build artifacts, no compiled PDF, no local config.
    # Only the compiled PDF is excluded: figures in images/ are PDFs too.
    (cd "$PREFIX" && zip -r -q "$OUT" . \
        -x '*.aux' '*.bbl' '*.blg' '*.fdb_latexmk' '*.fls' '*.acn' '*.acr' \
           '*.alg' '*.glg' '*.glo' '*.gls' '*.glsdefs' '*.idx' '*.ilg' \
           '*.ind' '*.ist' '*.lof' '*.log' '*.lot' '*.out' '*.synctex.gz' \
           '*.toc' '*.xdv' 'dissertation.pdf' '.gitignore' '.latexmkrc')
    echo "[overleaf] wrote $OUT ($(unzip -l "$OUT" | tail -1 | awk '{print $2}') files)"
    echo "[overleaf] drag it onto the Overleaf project's file tree to update in place."
}

if [[ "${1:-}" != "--git" ]]; then
    build_zip
    exit 0
fi

PROJECT_ID="${OVERLEAF_PROJECT_ID:-$(git config --get overleaf.projectid || true)}"
if [[ -z "$PROJECT_ID" ]]; then
    echo "[overleaf] no project id configured." >&2
    echo "[overleaf] run: git config overleaf.projectid <24-char-id-from-project-url>" >&2
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
