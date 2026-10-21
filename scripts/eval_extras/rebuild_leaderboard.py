"""Rebuild leaderboard-test from every saved test result on the frozen code (latest per variant)."""
import glob, json, sys
sys.path.insert(0, ".")
from src.rag.evaluation.models import VariantResult
from src.rag.evaluation.report import write_leaderboard
from src.rag.evaluation.dataset import load_dataset
from src.rag.retrieval.config import RetrievalConfig

ORDER = ["naive", "multiquery", "routed", "dense_only", "hybrid", "contextual", "current", "reranked",
         "hybrid_only", "reranked_only", "no_retrieval", "no_retrieval_strong", "current_strong",
         "assistant_gpt", "assistant_gemini", "assistant_claude", "deep_research_claude"]
latest = {}
for f in sorted(glob.glob("data/eval/results/*-2026102*.json")):
    d = json.load(open(f))
    if d.get("split") == "test" and d.get("code_version") == "0293a0b":
        latest[d["variant"]] = VariantResult.model_validate(d)  # sorted names: later timestamp wins
results = [latest[v] for v in ORDER if v in latest]
qs = load_dataset("data/eval/questions/golden.json").with_split("test").questions
broad = {q.id for q in qs if len(set(q.gold_chunk_keys)) > RetrievalConfig().top_k}
print(write_leaderboard(results, "data/eval/reports", broad_ids=broad), [r.variant for r in results])
