"""Side experiment outside the frozen harness: `current` with its answers written on a laptop.

The generator is Gemma 4 26B-A4B quantised to 4 bits (Ollama `gemma4:26b-a4b-it-q4_K_M`),
the production model at lower precision. Query analysis and expansion stay on OpenRouter's
Gemma, so retrieval is `current`'s and only the answer moves. The judge is unchanged (Qwen on
OpenRouter). No file under src/ changes: the transport's POST is swapped in this process for
models prefixed `ollama/`, through Ollama's native API so the context window can be set
(its OpenAI-compatible endpoint keeps the small default and would cut the 28k-token prompts).

Usage: python scripts/eval_extras/local_generation.py [split|-] [max_questions] [db_port]
"""
import sys
from collections import Counter

import requests

sys.path.insert(0, ".")
from dotenv import load_dotenv; load_dotenv(".env")
from src.utils.config_loader import config

SPLIT = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] != "-" else None
MAX_Q = int(sys.argv[2]) if len(sys.argv) > 2 else 0
if len(sys.argv) > 3:  # the thesis DB on another port, when 5432 is taken
    config._data["postgresql"]["port"] = sys.argv[3]

import src.rag.common.llm_transport as T
from src.rag.evaluation.dataset import load_dataset
from src.rag.evaluation.pipeline import _build_metrics, code_version
from src.rag.evaluation.report import save_result
from src.rag.evaluation.runner import run_variant
from src.rag.evaluation.variants import get_variant

LOCAL = "gemma4:26b-a4b-it-q4_K_M"
PREFIX = "ollama/"
NUM_CTX = 32768  # longest test prompt is ~28.2k tokens
OLLAMA_URL = "http://localhost:11434/api/chat"
_openrouter_post = T._post_chat


def _post_chat(payload, api_key, timeout_seconds, requested, on_token=None):
    if not payload["model"].startswith(PREFIX):
        return _openrouter_post(payload, api_key, timeout_seconds, requested, on_token)
    body = {
        "model": payload["model"][len(PREFIX):],
        "messages": payload["messages"],
        "stream": False,
        "think": False,  # the OpenRouter runs did not reason either
        "options": {"temperature": payload["temperature"], "num_predict": payload["max_tokens"],
                    "num_ctx": NUM_CTX},
    }
    try:
        r = requests.post(OLLAMA_URL, json=body, timeout=1800)
    except requests.RequestException as exc:
        raise T.OpenRouterTransportError(f"Ollama request failed: {exc}") from exc
    if r.status_code >= 400:
        raise T.OpenRouterTransportError(f"Ollama failed ({r.status_code}): {r.text[:300]}",
                                         status_code=r.status_code)
    d = r.json()
    if d.get("prompt_eval_count", 0) >= NUM_CTX:
        raise T.OpenRouterTransportError(f"prompt filled num_ctx={NUM_CTX}; it was cut")
    T.MODEL_USAGE[payload["model"]] += 1
    T._LAST_ANSWER.model = payload["model"]
    T._LAST_ANSWER.usage = {"prompt_tokens": d.get("prompt_eval_count", 0),
                            "completion_tokens": d.get("eval_count", 0), "cost": 0.0}
    T._LAST_ANSWER.annotations = []
    T._LAST_ANSWER.truncated = d.get("done_reason") == "length"
    return d["message"]["content"].strip()


T._post_chat = _post_chat

dataset_path = config.get("evaluation.dataset_path")
dataset = load_dataset(dataset_path)
if SPLIT:
    dataset = dataset.with_split(SPLIT)
if MAX_Q:
    dataset.questions = dataset.questions[:MAX_Q]

cfg = get_variant("current").model_copy(update={"name": "current_local", "generation_model": PREFIX + LOCAL})
before = Counter(T.MODEL_USAGE)
result = run_variant(cfg, dataset, _build_metrics(True, None), k=cfg.top_k,
                     wait_out_attempts=int(config.get("evaluation.wait_out_attempts")))
result.models_used = dict(T.MODEL_USAGE - before)
result.code_version, result.dataset_path, result.split = code_version(), dataset_path, SPLIT or ""
out = config.get("evaluation.results_dir") if not MAX_Q else "data/eval/results/smoke"
print("SAVED", save_result(result, out), {k: round(v, 3) for k, v in result.aggregate.items()})
