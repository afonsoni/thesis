"""
Check the LLM judge against a human: blind rating sheet, then agreement.

  export  Sample answers from one or more results JSONs (data/eval/results/*.json)
          and write a rating sheet with every claim the judge scored, but not its
          verdicts (those go to a separate key file, so the rating is blind).
  score   Read the filled-in sheet and report, per metric, claim-level agreement
          with the judge (raw % and Cohen's kappa) and answer-level correlation
          (Spearman) of the human and judge scores; relevance is compared 1-5.

In the sheet, mark each claim [x] (supported / covered) or [n] (not); leave [ ]
to skip it. Write the 1-5 relevance after "relevance:".

Usage:
  python scripts/judge_validation.py export data/eval/results/current-*.json --n 25
  python scripts/judge_validation.py score
"""

import argparse
import json
import os
import random
import re
import sys
from typing import Dict, List, Optional, Sequence

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

OUT_DIR = "data/eval/validation"
SHEET = os.path.join(OUT_DIR, "judge-sheet.md")
KEY = os.path.join(OUT_DIR, "judge-key.json")
CLAIM_METRICS = {
    "faithfulness": "Is the claim supported by the CONTEXT?",
    "correctness_recall": "Does the ANSWER state this reference claim?",
}


def cohen_kappa(a: Sequence[bool], b: Sequence[bool]) -> Optional[float]:
    """Cohen's kappa for two binary raters; ``None`` if undefined (no data or no variance)."""
    n = len(a)
    if n == 0:
        return None
    po = sum(x == y for x, y in zip(a, b)) / n
    pa, pb = sum(a) / n, sum(b) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return None if pe == 1 else (po - pe) / (1 - pe)


def cmd_export(args) -> None:
    runs = []
    for path in args.results:
        for r in json.load(open(path, encoding="utf-8"))["per_question"]:
            if r.get("judgements", {}).get("faithfulness"):
                runs.append(r)
    random.Random(args.seed).shuffle(runs)
    runs = runs[: args.n]
    questions = {q["id"]: q for q in json.load(open(args.dataset, encoding="utf-8"))["questions"]}

    sheet = [
        "# Judge validation sheet", "",
        "Mark each claim `[x]` (yes) or `[n]` (no); leave `[ ]` to skip. Give relevance 1-5",
        "(5 = answers the question directly and completely). Judge verdicts are hidden in",
        "judge-key.json; run `python scripts/judge_validation.py score` when done.", "",
    ]
    key = []
    for i, r in enumerate(runs, 1):
        q = questions.get(r["question_id"], {})
        sheet += [f"## item-{i:02d}", "", f"**Question:** {q.get('question', r['question_id'])}", "",
                  "**Answer:**", "", r["answer"], ""]
        if q.get("reference_answer"):
            sheet += ["**Reference answer:**", "", q["reference_answer"], ""]
        entry = {"item": i, "question_id": r["question_id"], "variant": r["variant"], "metrics": {}}
        for metric, prompt in CLAIM_METRICS.items():
            claims = r.get("judgements", {}).get(metric) or []
            if not claims:
                continue
            sheet += [f"**{metric}** — {prompt}", ""]
            sheet += [f"- [ ] {c['claim']}" for c in claims]
            sheet.append("")
            entry["metrics"][metric] = [c["supported"] for c in claims]
        rel = r.get("judgements", {}).get("answer_relevance")
        entry["relevance"] = rel["score"] if rel else None
        sheet += ["relevance: ", "", "<details><summary>Context the generator read</summary>", "",
                  r.get("context", ""), "", "</details>", ""]
        key.append(entry)
    os.makedirs(OUT_DIR, exist_ok=True)
    open(SHEET, "w", encoding="utf-8").write("\n".join(sheet))
    json.dump(key, open(KEY, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(runs)} items -> {SHEET} (key: {KEY})")


def parse_sheet(path: str) -> Dict[int, dict]:
    items, cur, metric = {}, None, None
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        m = re.match(r"^## item-(\d+)$", line)
        if m:
            cur = items.setdefault(int(m.group(1)), {"metrics": {}, "relevance": None})
            metric = None
            continue
        if cur is None:
            continue
        m = re.match(r"^\*\*(\w+)\*\* — ", line)
        if m and m.group(1) in CLAIM_METRICS:
            metric = m.group(1)
            cur["metrics"][metric] = []
            continue
        m = re.match(r"^- \[([ xXnN])\] ", line)
        if m and metric:
            mark = m.group(1).lower()
            cur["metrics"][metric].append(None if mark == " " else mark == "x")
            continue
        m = re.match(r"^relevance:\s*([1-5])?", line)
        if m:
            cur["relevance"] = int(m.group(1)) if m.group(1) else None
            metric = None
    return items


def cmd_score(_args) -> None:
    from scipy.stats import spearmanr

    human, key = parse_sheet(SHEET), json.load(open(KEY, encoding="utf-8"))
    report = {}
    for metric in CLAIM_METRICS:
        h_claims, j_claims, h_scores, j_scores = [], [], [], []
        for entry in key:
            judge = entry["metrics"].get(metric)
            marks = human.get(entry["item"], {}).get("metrics", {}).get(metric)
            if not judge or not marks or len(marks) != len(judge):
                continue
            pairs = [(h, j) for h, j in zip(marks, judge) if h is not None]
            if not pairs:
                continue
            h_claims += [h for h, _ in pairs]
            j_claims += [j for _, j in pairs]
            h_scores.append(sum(h for h, _ in pairs) / len(pairs))
            j_scores.append(sum(j for _, j in pairs) / len(pairs))
        if not h_claims:
            continue
        rho = spearmanr(h_scores, j_scores).statistic if len(h_scores) > 2 else None
        report[metric] = {
            "claims": len(h_claims), "answers": len(h_scores),
            "agreement": sum(a == b for a, b in zip(h_claims, j_claims)) / len(h_claims),
            "kappa": cohen_kappa(h_claims, j_claims), "spearman_answer_level": rho,
        }
    rel = [(human[e["item"]]["relevance"], e["relevance"]) for e in key
           if e.get("relevance") and human.get(e["item"], {}).get("relevance")]
    if len(rel) > 2:
        report["answer_relevance"] = {"answers": len(rel), "spearman": spearmanr(*zip(*rel)).statistic,
                                      "exact_agreement": sum(a == b for a, b in rel) / len(rel)}
    json.dump(report, open(os.path.join(OUT_DIR, "judge-agreement.json"), "w"), indent=1)
    for metric, r in report.items():
        print(metric, {k: (round(v, 3) if isinstance(v, float) else v) for k, v in r.items()})


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("export")
    e.add_argument("results", nargs="+")
    e.add_argument("--n", type=int, default=25)
    e.add_argument("--seed", type=int, default=0)
    e.add_argument("--dataset", default="data/eval/questions/golden.json")
    sub.add_parser("score")
    args = ap.parse_args()
    {"export": cmd_export, "score": cmd_score}[args.cmd](args)


if __name__ == "__main__":
    main()
