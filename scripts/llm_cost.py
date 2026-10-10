"""
What an LLM workload would cost on OpenRouter's paid models, before running it.

Prices are read live from OpenRouter's public model list (``/api/v1/models``, no
key needed); costgoat.com/pricing/openrouter is a daily static snapshot of the
same data. Token counts come from the newest eval result of each variant that
recorded them (``llm_calls`` carries ``prompt_tokens``/``completion_tokens`` since
token accounting landed), and otherwise from the rough defaults below, so the
first paid run of a variant is what makes its later estimates accurate.

    python scripts/llm_cost.py eval --variants naive,current,hybrid --split dev
    python scripts/llm_cost.py eval --no-judge --models deepseek/deepseek-v4-flash
    python scripts/llm_cost.py eval --judge-model deepseek/deepseek-v4-pro
    python scripts/llm_cost.py index --party ad
    python scripts/llm_cost.py spent     # the key's spend so far, and its limit

Models marked * can reason: when reasoning is on (the default for some), its
hidden tokens bill as output, which neither the defaults nor a profile measured
on a model that did not reason include.
"""

from __future__ import annotations

import argparse
import glob
import json
import math
import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.utils.config_loader import config  # noqa: E402

API = "https://openrouter.ai/api/v1"
CHARS_PER_TOKEN = 3.5  # as in generation/synthesizer.py

# Rough per-question defaults, used until a variant has a measured run. Contexts
# follow config.yaml's own measurements: a flat route's parents total ~4k tokens,
# an all-party comparison is trimmed to max_prompt_tokens (16k), and a named
# 2-3 party comparison (3 parents each) lands around 6k.
CTX_FLAT, CTX_NAMED_COMPARISON = 4000, 6000
ANALYSIS, EXPANSION, ANSWER = (600, 150), (200, 150), (500, 600)  # (in, out) besides context
# Claim extraction x2, verification x3 (one against the context), relevance x1.
# Output from a 6-question paid run of `current` (2026-10-10): verification
# writes ~1.2k tokens a call, so ~5k per question, twice the first guess.
JUDGE_ANSWERABLE = (4600, 5000)
JUDGE_UNANSWERABLE = (850, 150)  # relevance only


def prices() -> dict:
    """{model id: (USD per prompt token, USD per completion token, reasons?)}."""
    models = requests.get(f"{API}/models", timeout=30).json()["data"]
    return {
        m["id"]: (float(m["pricing"]["prompt"]), float(m["pricing"]["completion"]),
                  "reasoning" in (m.get("supported_parameters") or []))
        for m in models
    }


def paid(model: str) -> str:
    return model.removesuffix(":free")


def default_candidates() -> list:
    keys = ["llm.openrouter.model", "evaluation.judge_model", "indexing.classification_model"]
    ids = [config.get(k) for k in keys] + list(config.get("llm.openrouter.fallback_models", []))
    return list(dict.fromkeys(paid(m) for m in ids if m))


def measured(variant: str, results_dir: str):
    """Mean (in, out) tokens per question for pipeline and judge from the newest
    result of *variant* that recorded tokens, plus its file; None if there is none."""
    for path in sorted(glob.glob(f"{results_dir}/{variant}-*.json"), reverse=True):
        runs = json.load(open(path))["per_question"]
        calls = [c for r in runs for c in r.get("llm_calls", [])]
        if not calls or "prompt_tokens" not in calls[0]:
            continue
        sums = {"pipeline": [0, 0], "judge": [0, 0]}
        for c in calls:
            role = "judge" if c["step"].startswith("judge:") else "pipeline"
            sums[role][0] += c["prompt_tokens"]
            sums[role][1] += c["completion_tokens"]
        return {role: (i / len(runs), o / len(runs)) for role, (i, o) in sums.items()}, path
    return None


def default_tokens(cfg, questions, judge: bool) -> dict:
    """Total (in, out) tokens of one variant over *questions*, per role."""
    pipe, jud = [0, 0], [0, 0]
    max_ctx = int(config.get("llm.openrouter.max_prompt_tokens", 16000))
    for q in questions:
        ctx = CTX_FLAT
        if cfg.use_routing and q.query_type == "comparison":
            ctx = max_ctx if q.coverage == "exhaustive" else CTX_NAMED_COMPARISON
        steps = [ANSWER] + [ANALYSIS] * cfg.use_query_analysis + [EXPANSION] * cfg.use_multi_query
        pipe[0] += ctx + sum(i for i, _ in steps)
        pipe[1] += sum(o for _, o in steps)
        if judge:
            i, o = JUDGE_ANSWERABLE if q.answerable else JUDGE_UNANSWERABLE
            jud[0] += i + (ctx if q.answerable else 0)  # faithfulness reads the context
            jud[1] += o
    return {"pipeline": tuple(pipe), "judge": tuple(jud)}


def print_table(tokens: dict, models: list, judge_model, table: dict) -> None:
    """*tokens*: {role: (in, out)} totals. Every role is priced at the row's model,
    except the judge when *judge_model* pins it."""
    def cost(model, role):
        p_in, p_out, _ = table[model]
        return tokens[role][0] * p_in + tokens[role][1] * p_out

    for role, (i, o) in tokens.items():
        if i or o:
            print(f"  {role:<9} {i / 1e6:7.2f}M tokens in  {o / 1e6:6.2f}M out")
    fixed = 0.0
    if judge_model and tokens.get("judge", (0, 0)) != (0, 0):
        fixed = cost(judge_model, "judge")
        print(f"  judge priced at {judge_model}: ${fixed:.2f}")
    roles = [r for r in tokens if not (judge_model and r == "judge")]

    def total(m):
        return fixed + sum(cost(m, r) for r in roles) if m in table else math.inf

    print(f"\n  {'model':<44} {'$/M in':>7} {'$/M out':>8} {'estimate':>9}")
    for m in sorted(models, key=total):
        if m not in table:
            print(f"  {m:<44} not on OpenRouter")
            continue
        p_in, p_out, reasons = table[m]
        print(f"  {m + ' *' * reasons:<44} {p_in * 1e6:7.3f} {p_out * 1e6:8.3f} {'$%.2f' % total(m):>9}")


def cmd_eval(args, table) -> None:
    from src.rag.evaluation.dataset import load_dataset
    from src.rag.evaluation.variants import resolve_variants

    dataset = load_dataset(args.dataset or config.get("evaluation.dataset_path"))
    if args.curated_only:
        dataset = dataset.curated_only()
    if args.split:
        dataset = dataset.with_split(args.split)
    questions = dataset.questions[: args.limit] if args.limit else dataset.questions
    names = args.variants.split(",") if args.variants else list(config.get("evaluation.variants"))
    results_dir = str(config.get("evaluation.results_dir", "data/eval/results"))
    judge = not args.no_judge

    total = {"pipeline": [0, 0], "judge": [0, 0]}
    print(f"eval: {', '.join(names)} over {len(questions)} questions, judge {'on' if judge else 'off'}")
    for cfg in resolve_variants(names):
        found = measured(cfg.name, results_dir)
        if found:
            per_q, path = found
            tokens = {r: (i * len(questions), o * len(questions)) for r, (i, o) in per_q.items()}
            source = f"measured, {Path(path).name}"
        else:
            tokens, source = default_tokens(cfg, questions, judge), "default"
        if not judge:
            tokens["judge"] = (0, 0)
        for role in total:
            total[role][0] += tokens[role][0]
            total[role][1] += tokens[role][1]
        print(f"  {cfg.name:<15} {sum(i for i, _ in tokens.values()) / 1e3:8.0f}k in "
              f"{sum(o for _, o in tokens.values()) / 1e3:6.0f}k out  ({source})")
    print()
    print_table({r: tuple(v) for r, v in total.items()}, args.models, args.judge_model, table)


def cmd_index(args, table) -> None:
    """Topic classification: one call per ``classification_batch_size`` chunks, the
    chunk counts and sizes read off each party's newest classified checkpoint."""
    batch = int(config.get("indexing.classification_batch_size", 15))
    template = 2865  # chars of classifier.BATCH_CLASSIFICATION_PROMPT
    tokens_in = tokens_out = calls = 0
    for party in args.party or ["ad", "be", "chega", "il", "livre", "pan", "pcp", "ps"]:
        paths = sorted(glob.glob(f"{config.get('paths.processed_data')}/{party}-*-classified.json"),
                       key=os.path.getmtime)
        if not paths:
            print(f"  {party}: no classified checkpoint to size it from, skipped")
            continue
        chunks = json.load(open(paths[-1]))["chunks"]
        n = math.ceil(len(chunks) / batch)
        calls += n
        tokens_in += n * template / CHARS_PER_TOKEN + sum(len(c["content"]) for c in chunks) / CHARS_PER_TOKEN
        tokens_out += len(chunks) * 40  # a topic list per chunk
        print(f"  {party:<6} {len(chunks):5d} chunks, {n:3d} calls  ({Path(paths[-1]).name})")
    print()
    print_table({"classify": (tokens_in, tokens_out)}, args.models, None, table)


def cmd_spent(_args, _table) -> None:
    load_dotenv(Path(__file__).resolve().parents[1] / ".env")
    key = requests.get(f"{API}/key", timeout=30,
                       headers={"Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}"}).json()["data"]
    print(f"spent ${key['usage']:.4f} total, ${key['usage_daily']:.4f} today; "
          f"limit {'none' if key['limit'] is None else '$%.2f' % key['limit']}, "
          f"remaining {'n/a' if key['limit_remaining'] is None else '$%.4f' % key['limit_remaining']}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    ev = sub.add_parser("eval", help="estimate a `main.py eval` run")
    ev.add_argument("--variants", help="comma-separated (default: config evaluation.variants)")
    ev.add_argument("--dataset")
    ev.add_argument("--split", choices=["dev", "test"])
    ev.add_argument("--curated-only", action="store_true")
    ev.add_argument("--limit", type=int, help="only the first N questions")
    ev.add_argument("--no-judge", action="store_true")
    ev.add_argument("--judge-model", help="price the judge at this model; rows then vary the generator")
    ix = sub.add_parser("index", help="estimate topic classification for `main.py index`")
    ix.add_argument("--party", action="append", help="repeatable (default: all eight)")
    for p in (ev, ix):
        p.add_argument("--models", type=lambda s: s.split(","), default=default_candidates(),
                       help="comma-separated model ids (default: config's models, without :free)")
    sub.add_parser("spent", help="what the OpenRouter key has spent, and its limit (needs the key)")
    args = parser.parse_args()

    table = prices() if args.command != "spent" else {}
    if getattr(args, "judge_model", None) and args.judge_model not in table:
        parser.error(f"{args.judge_model} is not on OpenRouter")
    {"eval": cmd_eval, "index": cmd_index, "spent": cmd_spent}[args.command](args, table)


if __name__ == "__main__":
    main()
