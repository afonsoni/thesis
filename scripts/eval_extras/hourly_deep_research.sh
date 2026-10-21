#!/bin/sh
# 4 questions per hour (sequential) until all 36 are answered, then judge. Gives up after 15 rounds.
cd "$(dirname "$0")/../.."
S=data/eval/extras
for round in $(seq 1 15); do
  start=$(date +%s)
  echo "ROUND $round $(date +%H:%M)"
  python scripts/eval_extras/deep_research.py $S data/eval/questions/golden.json data/eval/results test 1 4 >> $S/deep-research-test.log 2>&1
  grep -q '^SAVED' $S/deep-research-test.log && { grep -E '^SAVED' $S/deep-research-test.log; exit 0; }
  wait=$((3600 - ($(date +%s) - start))); [ $wait -gt 0 ] && sleep $wait
done
echo "GAVE UP after 15 rounds"
