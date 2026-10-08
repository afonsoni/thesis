#!/usr/bin/env bash
#
# Render the Mermaid diagrams in docs/architecture.md to the dissertation's
# figures (dissertation/images/architecture-<name>.pdf).
#
#   ./scripts/render_diagrams.sh
#
# docs/architecture.md is the single source: edit a diagram there, then re-run.
# Blocks are named by position, so adding or reordering one means updating
# NAMES. Needs Node (npx); the first run downloads mermaid-cli and its headless
# Chrome.

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

NAMES=(overview indexing retrieval generation evaluation)
OUT_DIR="dissertation/images"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Print-friendly: greyscale theme, a sans-serif close to the thesis font, and
# line breaks left to the <br/>s in the labels rather than to auto-wrapping.
cat > "$TMP/config.json" <<'EOF'
{
  "theme": "neutral",
  "themeVariables": {"fontFamily": "Helvetica, Arial, sans-serif", "fontSize": "14px"},
  "flowchart": {"htmlLabels": true, "curve": "basis", "nodeSpacing": 35,
                "rankSpacing": 40, "padding": 10, "wrappingWidth": 600}
}
EOF

npx -y @mermaid-js/mermaid-cli@11.17.0 \
    -i docs/architecture.md -o "$TMP/out.md" -e pdf --pdfFit \
    -b white -w 1200 -c "$TMP/config.json" -q

count=$(ls "$TMP"/out-*.pdf | wc -l | tr -d ' ')
if [ "$count" -ne "${#NAMES[@]}" ]; then
    echo "[diagrams] found $count diagrams but ${#NAMES[@]} names; update NAMES" >&2
    exit 1
fi

for i in "${!NAMES[@]}"; do
    mv "$TMP/out-$((i + 1)).pdf" "$OUT_DIR/architecture-${NAMES[$i]}.pdf"
    echo "[diagrams] $OUT_DIR/architecture-${NAMES[$i]}.pdf"
done
