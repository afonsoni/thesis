"""Re-ask only the errored questions of a saved test result, merge them in, save as a new result.

Same variant config, judge and metrics as the frozen harness; the merged result keeps the
original code_version and records which questions were patched in config["patched"].
Usage: python patch_errors.py <variant>
"""
import glob, json, sys
from collections import Counter
sys.path.insert(0, ".")
from dotenv import load_dotenv; load_dotenv(".env")
from src.rag.common.llm_transport import MODEL_USAGE
from src.rag.evaluation.dataset import load_dataset
from src.rag.evaluation.models import VariantResult
from src.rag.evaluation.pipeline import _build_metrics
from src.rag.evaluation.report import save_result
from src.rag.evaluation.runner import _aggregate, run_variant
from src.rag.evaluation.variants import resolve_variants
from src.utils.config_loader import config

variant = sys.argv[1]
path = sorted(glob.glob(f"data/eval/results/{variant}-2026102*.json"))[-1]
old = VariantResult.model_validate(json.load(open(path)))
failed = [r.question_id for r in old.per_question if r.error]
print("patching", path, failed, flush=True)

dataset = load_dataset("data/eval/questions/golden.json").with_split("test")
dataset.questions = [q for q in dataset.questions if q.id in failed]
cfg = resolve_variants([variant])[0]
before = Counter(MODEL_USAGE)
new = run_variant(cfg, dataset, _build_metrics(True, None), k=cfg.top_k, generate=True,
                  wait_out_attempts=int(config.get("evaluation.wait_out_attempts")))
fresh = {r.question_id: r for r in new.per_question}
old.per_question = [fresh.get(r.question_id, r) for r in old.per_question]
old.aggregate = _aggregate(old.per_question)
old.models_used = dict(Counter(old.models_used) + (Counter(MODEL_USAGE) - before))
old.config = {**old.config, "patched": failed}
old.created_at = new.created_at
print("still failing", [r.question_id for r in old.per_question if r.error],
      "patch cost $%.3f" % sum(c["cost"] for r in new.per_question for c in r.llm_calls))
print("SAVED", save_result(old, "data/eval/results"))
