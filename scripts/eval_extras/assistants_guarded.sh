#!/bin/sh
# Gemini, then Claude only if the live OpenRouter balance covers it. A watchdog kills a run
# when the balance drops under $0.30 (kept for the deep-research judge).
cd "$(dirname "$0")/../.."
set -a; . ./.env; set +a
S=data/eval/extras
balance() { curl -s https://openrouter.ai/api/v1/credits -H "Authorization: Bearer $OPENROUTER_API_KEY" |
  python3 -c "import json,sys; d=json.load(sys.stdin)['data']; print(round(d['total_credits']-d['total_usage'],3))"; }
run() {
  python main.py eval --split test --variants $1 > $S/eval-test-$1.log 2>&1 &
  pid=$!
  while kill -0 $pid 2>/dev/null; do
    sleep 60
    b=$(balance); [ -n "$b" ] && [ $(echo "$b < 0.30" | bc) -eq 1 ] && { echo "WATCHDOG killed $1 at balance $b"; kill $pid; }
  done
  echo "$1 done, balance now $(balance)"
}
echo "START balance $(balance)"
run assistant_gemini
b=$(balance)
if [ $(echo "$b >= 4.5" | bc) -eq 1 ]; then run assistant_claude; else echo "SKIP assistant_claude: balance $b < 4.50"; fi
