"""
Check the LLM judge against a human: blind rating sheet, then agreement.

  export  Sample answers from one or more results JSONs (data/eval/results/*.json)
          and write a rating sheet with every claim the judge scored, but not its
          verdicts (those go to a separate key file, so the rating is blind).
  score   Read the filled-in sheet and report, per metric, claim-level agreement
          with the judge (raw % and Cohen's kappa) and answer-level correlation
          (Spearman) of the human and judge scores; relevance is compared 1-5.
  borrow  Give closed-book answers (no_retrieval) the context another variant
          retrieved for the same question, and judge faithfulness against it.
          A faithful RAG run has few unsupported claims, so a sheet drawn from
          one alone barely tests whether the judge catches them; these answers
          supply negatives picked without looking at the judge's verdicts.

In the sheet, mark each claim [x] (supported / covered) or [n] (not); leave [ ]
to skip it. Write the 1-5 relevance after "relevance:". ``--name`` keeps a second
sheet (``<name>-sheet.md``, ``<name>-key.json``) apart from the first.

Usage:
  python scripts/judge_validation.py export data/eval/results/current-*.json --n 25
  python scripts/judge_validation.py score --ratings data/eval/validation/ratings.json
  python scripts/judge_validation.py borrow data/eval/results/no_retrieval-X.json \
      --context-from data/eval/results/current-X.json --n 12
  python scripts/judge_validation.py export data/eval/validation/no_retrieval-borrowed.json \
      --n 12 --name judge-noret
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


def _paths(name: str):
    return (os.path.join(OUT_DIR, f"{name}-sheet.md"), os.path.join(OUT_DIR, f"{name}-key.json"),
            os.path.join(OUT_DIR, f"{name}-agreement.json"))


def cmd_borrow(args) -> None:
    from dotenv import load_dotenv

    load_dotenv()
    from src.rag.evaluation.judge import extract_claims, verify_claims
    from src.rag.evaluation.metrics.generation import _log

    questions = {q["id"]: q for q in json.load(open(args.dataset, encoding="utf-8"))["questions"]}
    donor = json.load(open(args.context_from, encoding="utf-8"))
    contexts = {r["question_id"]: r.get("context", "") for r in donor["per_question"]}
    runs = [r for r in json.load(open(args.results, encoding="utf-8"))["per_question"]
            if r["answer"].strip() and questions.get(r["question_id"], {}).get("answerable", True)
            and contexts.get(r["question_id"], "").strip()]
    random.Random(args.seed).shuffle(runs)
    out = []
    for r in runs[: args.n]:
        context = contexts[r["question_id"]]
        claims = extract_claims(questions[r["question_id"]]["question"], r["answer"])
        verdicts = verify_claims(claims, context) if claims else None
        if not verdicts:  # failed judge call or no claims: nothing to rate
            print(f"skip {r['question_id']}")
            continue
        out.append(dict(r, context=context, variant=f"{r['variant']}+context:{donor['variant']}",
                        judgements=dict(r.get("judgements") or {}, faithfulness=_log(claims, verdicts))))
    if not out:
        sys.exit("every judge call failed; nothing written")
    path = os.path.join(OUT_DIR, f"{out[0]['variant'].split('+')[0]}-borrowed.json")
    json.dump({"results": args.results, "context_from": args.context_from, "per_question": out},
              open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    unsupported = sum(not c["supported"] for r in out for c in r["judgements"]["faithfulness"])
    total = sum(len(r["judgements"]["faithfulness"]) for r in out)
    print(f"{len(out)} answers, {unsupported}/{total} claims unsupported -> {path}")


def cmd_export(args) -> None:
    sheet_path, key_path, _ = _paths(args.name)
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
    open(sheet_path, "w", encoding="utf-8").write("\n".join(sheet))
    json.dump(key, open(key_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(runs)} items -> {sheet_path} (key: {key_path})")


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


def load_ratings(path: str) -> Dict[int, dict]:
    """The rater page's JSON ({item: {"f": [...], "r": [...], "rel": n}}) in parse_sheet's shape."""
    return {int(i): {"metrics": {"faithfulness": v["f"], "correctness_recall": v["r"]}, "relevance": v["rel"]}
            for i, v in json.load(open(path, encoding="utf-8")).items()}


def cmd_score(args) -> None:
    from scipy.stats import spearmanr

    sheet_path, key_path, report_path = _paths(args.name)
    human = load_ratings(args.ratings) if args.ratings else parse_sheet(sheet_path)
    key = json.load(open(key_path, encoding="utf-8"))
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
        agreement = sum(a == b for a, b in zip(h_claims, j_claims)) / len(h_claims)
        pairs = list(zip(h_claims, j_claims))
        report[metric] = {
            "claims": len(h_claims), "answers": len(h_scores), "agreement": agreement,
            "kappa": cohen_kappa(h_claims, j_claims),
            # Kappa collapses when nearly every claim is supported; PABAK does not.
            "pabak": 2 * agreement - 1,
            "both_yes": pairs.count((True, True)), "both_no": pairs.count((False, False)),
            "human_no_judge_yes": pairs.count((False, True)), "human_yes_judge_no": pairs.count((True, False)),
            "spearman_answer_level": rho,
        }
    rel = [(human[e["item"]]["relevance"], e["relevance"]) for e in key
           if e.get("relevance") and human.get(e["item"], {}).get("relevance")]
    if len(rel) > 2:
        report["answer_relevance"] = {"answers": len(rel), "spearman": spearmanr(*zip(*rel)).statistic,
                                      "exact_agreement": sum(a == b for a, b in rel) / len(rel),
                                      "within_one": sum(abs(a - b) <= 1 for a, b in rel) / len(rel)}
    json.dump(report, open(report_path, "w"), indent=1)
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
    e.add_argument("--name", default="judge")
    s = sub.add_parser("score")
    s.add_argument("--name", default="judge")
    s.add_argument("--ratings", help="rater-page JSON to score instead of the sheet's [x]/[n] marks")
    b = sub.add_parser("borrow")
    b.add_argument("results")
    b.add_argument("--context-from", required=True)
    b.add_argument("--n", type=int, default=12)
    b.add_argument("--seed", type=int, default=0)
    b.add_argument("--dataset", default="data/eval/questions/golden.json")
    args = ap.parse_args()
    {"export": cmd_export, "score": cmd_score, "borrow": cmd_borrow}[args.cmd](args)


if __name__ == "__main__":
    main()
