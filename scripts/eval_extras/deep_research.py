"""Unconstrained research-agent ceiling: Opus 5.5 via Claude Code, web only, no turn/search/token cap.

Answers come from `claude -p` (empty folder, --restricted so user/project settings, hooks and
plugins are ignored, only WebSearch + WebFetch, no MCP), cached per question so a rerun
resumes. The frozen harness then judges them like any closed-book rung (same Qwen judge,
references, metrics). Cost in llm_calls is Claude Code's notional total_cost_usd.

Usage: python deep_research.py <cache_dir> <dataset.json> <results_dir> [split|-] [parallel] [max_new]
Judging runs only once every question has an answer.
"""
import json, os, subprocess, sys, tempfile, threading, time
from concurrent.futures import ThreadPoolExecutor
from types import SimpleNamespace

sys.path.insert(0, ".")
from dotenv import load_dotenv; load_dotenv(".env")
from src.rag.evaluation.dataset import load_dataset
from src.rag.evaluation.pipeline import _build_metrics, code_version
from src.rag.evaluation.report import save_result
from src.rag.evaluation.runner import _aggregate, run_variant
from src.rag.generation.prompts import ASSISTANT_SYSTEM_PROMPT, CLOSED_BOOK_PROMPT
from src.rag.retrieval.config import RetrievalConfig

S, DATASET, RESULTS = sys.argv[1:4]
SPLIT = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] != "-" else None
PARALLEL = int(sys.argv[5]) if len(sys.argv) > 5 else 3
MAX_NEW = int(sys.argv[6]) if len(sys.argv) > 6 else 0  # answer at most this many per call (0 = all)
MODEL = "opus"  # the CLI rejects "claude-opus-5-5"; init_model records what answered
EFFORT = "high"  # pinned so the thesis can state it; max judged overkill
NAME = "deep_research_claude"
CACHE = os.path.join(S, f"{NAME}-cache.json")
SYSTEM = ASSISTANT_SYSTEM_PROMPT + (
    "\n\nPesquisa na web tantas vezes quantas precisares e lê as fontes que quiseres, "
    "incluindo os próprios programas eleitorais, antes de responder."
)


def ask(question: str) -> dict:
    """One headless Claude Code run in an empty folder; returns answer + run stats."""
    cmd = ["claude", "-p", CLOSED_BOOK_PROMPT.format(question=question),
           "--model", MODEL, "--effort", EFFORT, "--system-prompt", SYSTEM,
           "--restricted", "--tools", "WebSearch,WebFetch", "--allowedTools", "WebSearch,WebFetch",
           "--strict-mcp-config", "--disable-slash-commands", "--no-session-persistence",
           "--output-format", "stream-json", "--verbose"]
    start = time.time()
    with tempfile.TemporaryDirectory() as empty:
        out = subprocess.run(cmd, cwd=empty, capture_output=True, text=True).stdout
    events = [json.loads(l) for l in out.splitlines() if l.strip().startswith("{")]
    init = next((e for e in events if e.get("type") == "system" and e.get("subtype") == "init"), {})
    final = next((e for e in reversed(events) if e.get("type") == "result"), {})
    uses = [b.get("name") for e in events if e.get("type") == "assistant"
            for b in e.get("message", {}).get("content", []) if b.get("type") == "tool_use"]
    usage = final.get("usage") or {}
    return {
        "answer": final.get("result", "") if not final.get("is_error") else "",
        "error": final.get("subtype") if final.get("is_error") or not final else None,
        "secs": round(time.time() - start, 1),
        "num_turns": final.get("num_turns"),
        "cost_usd": final.get("total_cost_usd") or 0.0,
        "prompt_tokens": sum(usage.get(k) or 0 for k in ("input_tokens", "cache_read_input_tokens",
                                                         "cache_creation_input_tokens")),
        "completion_tokens": usage.get("output_tokens") or 0,
        "web_searches": uses.count("WebSearch"),
        "web_fetches": uses.count("WebFetch"),
        "init_tools": init.get("tools"), "init_mcp": init.get("mcp_servers"),
        "init_plugins": init.get("plugins"), "init_model": init.get("model"),
    }


dataset = load_dataset(DATASET)
if SPLIT:
    dataset = dataset.with_split(SPLIT)
cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
todo = [q for q in dataset.questions if not cache.get(q.id, {}).get("answer")]
print(f"{len(todo)} to answer, {len(dataset.questions) - len(todo)} cached", flush=True)


LOCK = threading.Lock()


def work(q):
    answer = ask(q.question)
    with LOCK:
        cache[q.id] = answer
        json.dump(cache, open(CACHE, "w"), ensure_ascii=False, indent=1)
    r = cache[q.id]
    print(f"ANSWERED {q.id} secs={r['secs']} turns={r['num_turns']} searches={r['web_searches']} "
          f"fetches={r['web_fetches']} notional=${r['cost_usd']:.3f} error={r['error']}", flush=True)


with ThreadPoolExecutor(PARALLEL) as pool:
    list(pool.map(work, todo[:MAX_NEW] if MAX_NEW else todo))

left = sum(not cache.get(q.id, {}).get("answer") for q in dataset.questions)
if left:
    print(f"PENDING {left} questions still unanswered; judging deferred", flush=True)
    sys.exit(0)

by_text = {q.question: cache[q.id] for q in dataset.questions}


def generate(result):
    r = by_text[result.query.original_query]
    if not r["answer"]:
        raise RuntimeError(f"no answer: {r['error']}")
    return SimpleNamespace(answer=r["answer"], context="")


cfg = RetrievalConfig(name=NAME, use_retrieval=False, web_search=True, generation_model=f"claude-opus-5-5 (Claude Code, effort {EFFORT})")
result = run_variant(cfg, dataset, _build_metrics(True, None), k=cfg.top_k, generate_fn=generate)
for run, q in zip(result.per_question, dataset.questions):  # real agent wall time and notional cost
    r = cache[q.id]
    run.latency_s = r["secs"]
    run.llm_calls.insert(0, {"step": "deep research answer (notional, Claude plan)", "model": MODEL,
                             "prompt_tokens": r["prompt_tokens"], "completion_tokens": r["completion_tokens"],
                             "cost": r["cost_usd"], "secs": r["secs"]})
result.aggregate = _aggregate(result.per_question)
result.code_version, result.dataset_path, result.split = code_version(), DATASET, SPLIT or ""
print("SAVED", save_result(result, RESULTS), {k: round(v, 3) for k, v in result.aggregate.items()
                                              if k in ("correctness_recall", "correctness", "abstention",
                                                       "false_refusal", "avg_latency_s")})
