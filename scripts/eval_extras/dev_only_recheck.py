"""Re-check, on the development questions alone, the design decisions judged on all 61 questions.

Three late revisions (contextual retrieval, the wider retrieval net, the 64k prompt budget) were
judged on all 61 gold questions, test included. This filters the stored per-question results of
those runs to each split and repeats the paired comparison, so it shows what a dev-only protocol
would have decided. No LLM calls; the all-61 column reproduces the numbers the commits cite.

Usage: python scripts/eval_extras/dev_only_recheck.py  (writes data/eval/extras/dev-only-recheck.md)
"""
import json
import sys

sys.path.insert(0, ".")
from src.rag.evaluation.stats import paired_diff  # noqa: E402

OUT = "data/eval/extras/dev-only-recheck.md"
# (decision, baseline runs, candidate runs, metrics); several runs = passes averaged per question
DECISIONS = [
    ("Contextual retrieval: plain hybrid index to LLM context (524d9ea, two passes)",
     ["current-20261011T210519", "current-20261011T211256"],
     ["contextual_llm-20261011T211023", "contextual_llm-20261011T211803"],
     ["recall", "mrr", "ndcg"]),
    ("Section headers only: plain hybrid index to headers (524d9ea, two passes)",
     ["current-20261011T210519", "current-20261011T211256"],
     ["contextual-20261011T210746", "contextual-20261011T211528"],
     ["recall", "ndcg"]),
    ("Wider net: 5 / 5 with the topic filter to 10 / 8 without it (b054bf8)",
     ["current-20261013T015009"], ["wide-20261013T032701"],
     ["recall", "ndcg", "correctness", "correctness_recall", "faithfulness"]),
    ("Prompt budget: 32k to 64k (b054bf8)",
     ["wide-20261013T032701"], ["wide_64k-20261013T051430"],
     ["correctness", "correctness_recall", "faithfulness"]),
]


def per_question(runs, metric):
    scores = []
    for name in runs:
        d = json.load(open(f"data/eval/results/{name}.json", encoding="utf-8"))
        scores.append({r["question_id"]: r["metrics"][metric] for r in d["per_question"] if metric in r["metrics"]})
    shared = set.intersection(*(set(s) for s in scores))
    return {q: sum(s[q] for s in scores) / len(scores) for q in shared}


def cell(a, b):
    r = paired_diff(a, b)
    if r is None:
        return "n/a"
    mean, (lo, hi), n = r
    star = "*" if lo > 0 or hi < 0 else ""
    return f"{mean:+.3f}{star} [{lo:+.3f}, {hi:+.3f}] (n={n})"


def main():
    gold = json.load(open("data/eval/questions/golden.json", encoding="utf-8"))
    split = {q["id"]: q["split"] for q in gold["questions"]}
    lines = ["# Dev-only re-check of the decisions judged on all 61 questions", "",
             "`python scripts/eval_extras/dev_only_recheck.py`. Paired differences (candidate minus",
             "baseline) with 95% bootstrap intervals over questions, from the stored runs; `*` means",
             "the interval excludes zero. Only answerable questions carry these metrics.", ""]
    for title, base, cand, metrics in DECISIONS:
        lines += [f"## {title}", "", "| metric | all 61 | dev | test |", "|---|---|---|---|"]
        for m in metrics:
            a, b = per_question(base, m), per_question(cand, m)
            cells = [cell({q: v for q, v in a.items() if s is None or split.get(q) == s},
                          {q: v for q, v in b.items() if s is None or split.get(q) == s})
                     for s in (None, "dev", "test")]
            lines.append(f"| {m} | " + " | ".join(cells) + " |")
        lines.append("")
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
