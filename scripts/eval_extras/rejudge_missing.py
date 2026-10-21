"""Fill in generation scores the judge omitted in the frozen test results (code 0293a0b).

The judge omits a score when its call fails, so an outage never counts as a 0. On the test
split five (variant, question) pairs ended up unscored, and the leaderboard, which averages
every variant over the questions all of them were scored on, dropped those questions from
every row. This runs the same judge on the stored answer and context and fills in only the
missing metrics; every recorded score stays as it was. The repair calls are not added to the
run's llm_calls or models_used, so judge cost per answer stays one judging pass for every
variant; the aggregate is recomputed. At temperature 0 the judge repeats its replies token for
token, so a pair whose reply did not parse the first time stays unscored.

Usage: python scripts/eval_extras/rejudge_missing.py [--dry-run]
"""
import copy
import glob
import json
import sys

sys.path.insert(0, ".")
from dotenv import load_dotenv  # noqa: E402

load_dotenv()

from src.rag.evaluation.dataset import load_dataset  # noqa: E402
from src.rag.evaluation.metrics.generation import GenerationJudgeMetric, _f1  # noqa: E402
from src.rag.evaluation.models import VariantResult  # noqa: E402
from src.rag.evaluation.runner import _aggregate  # noqa: E402
from src.utils.config_loader import config  # noqa: E402

JUDGEMENT_OF = {"faithfulness": "faithfulness", "correctness": "correctness_precision",
                "correctness_recall": "correctness_recall", "answer_relevance": "answer_relevance",
                "abstention": "abstention"}


def expected(q, run) -> set:
    if not q.answerable:
        return {"abstention"}
    keys = {"answer_relevance", "false_refusal", "correctness", "correctness_recall"}
    if run.context.strip():
        keys |= {"faithfulness", "correctness_grounded"}
    return keys


def main(dry_run: bool) -> None:
    questions = {q.id: q for q in load_dataset("data/eval/questions/golden.json").with_split("test").questions}
    latest = {}
    for f in sorted(glob.glob("data/eval/results/*-2026102*.json")):  # the files rebuild_leaderboard reads
        d = json.load(open(f, encoding="utf-8"))
        if d.get("split") == "test" and d.get("code_version") == "0293a0b":
            latest[d["variant"]] = f

    metric = GenerationJudgeMetric(model=config.get("evaluation.judge_model"))
    # Reuse the reference claims every other variant was scored against, so a re-judged
    # correctness compares with theirs instead of with a fresh extraction.
    for path in latest.values():
        for run in json.load(open(path, encoding="utf-8"))["per_question"]:
            ref = run.get("judgements", {}).get("correctness_recall")
            q = questions.get(run["question_id"])
            if ref and q:
                metric._reference_claims.setdefault((q.id, q.reference_answer), [c["claim"] for c in ref])
    for variant, path in sorted(latest.items()):
        result = VariantResult.model_validate(json.load(open(path, encoding="utf-8")))
        judged = any("answer_relevance" in r.metrics or "abstention" in r.metrics for r in result.per_question)
        changed = False
        for run in result.per_question:
            q = questions[run.question_id]
            missing = expected(q, run) - set(run.metrics) if judged and run.answer.strip() and not run.error else set()
            if not missing:
                continue
            print(f"{variant} {run.question_id}: missing {sorted(missing)}")
            if dry_run:
                continue
            scratch = copy.deepcopy(run)
            scratch.judgements = {}
            new = metric.score(scratch, q)
            filled = {k: v for k, v in new.items() if k in missing and k != "correctness_grounded"}
            run.metrics.update(filled)
            grounded = _f1(run.metrics.get("faithfulness"), run.metrics.get("correctness_recall"))
            if "correctness_grounded" in missing and grounded is not None:
                run.metrics["correctness_grounded"] = filled["correctness_grounded"] = grounded
            for k in filled:
                if k in JUDGEMENT_OF and JUDGEMENT_OF[k] in scratch.judgements:
                    run.judgements[JUDGEMENT_OF[k]] = scratch.judgements[JUDGEMENT_OF[k]]
            print(f"   filled {filled}; still missing {sorted(missing - set(run.metrics))}")
            changed = changed or bool(filled)
        if changed:
            result.aggregate = _aggregate(result.per_question)
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(result.model_dump(), fh, ensure_ascii=False, indent=2)
            print(f"   rewrote {path}")


if __name__ == "__main__":
    main(dry_run="--dry-run" in sys.argv)
