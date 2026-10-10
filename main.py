"""
CLI entry-point for the RAG System for Political Programs Analysis.

Commands:
    python main.py parse   [--input-dir ...] [--output-dir ...]
    python main.py index   [--party X] [--drop] [--no-classify]
                           [--classify-only | --from-classified PATH]
    python main.py query   "question" [--top-k 5] [--no-expand] [--verbose]
    python main.py eval    [--variants naive,current] [--dataset PATH]
                           [--curated-only] [--top-k 5] [--no-judge]
"""

import argparse
import logging
import os
import sys

from dotenv import load_dotenv

from src.rag.common.models import ChunkStrategy

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("main")


# ---------------------------------------------------------------------------
# Sub-command handlers
# ---------------------------------------------------------------------------

def cmd_parse(args):
    from src.rag.indexing.parser import parse_pdfs

    generated = parse_pdfs(
        pdf_dir=args.input_dir,
        output_dir=args.output_dir,
    )
    logger.info("Generated %d markdown files.", len(generated))


def cmd_clean(args):
    import glob

    from src.rag.indexing.cleaner import clean_markdown

    raw_dir = os.path.join(args.markdown_dir, "_raw")
    files = sorted(glob.glob(os.path.join(raw_dir, "**", "*.md"), recursive=True))
    if args.party:
        files = [f for f in files if os.path.basename(f).startswith(args.party.lower() + "-")]
    if not files:
        logger.error("No raw markdown found in %s (party=%s)", raw_dir, args.party)
        sys.exit(1)
    for path in files:
        clean_markdown(path, model=args.model)


def cmd_index(args):
    from src.rag.indexing.pipeline import index_documents

    count = index_documents(
        party_filter=args.party,
        chunk_strategy=args.chunk_strategy,
        use_llm_classification=False if args.no_classify else None,
        drop_existing=args.drop,
        classified_input_path=args.from_classified,
        classify_only=args.classify_only,
        contextual_headers=args.contextual_headers,
        table=args.table,
    )
    logger.info("Processed %d chunks total.", count)


class _ElapsedFormatter(logging.Formatter):
    """``[  3.2s] message``: seconds since the program started."""

    def format(self, record):
        return f"[{record.relativeCreated / 1000:5.1f}s] {record.getMessage()}"


def cmd_query(args):
    from src.rag.common.llm_client import CALL_LOG
    from src.rag.retrieval.pipeline import retrieve
    from src.rag.generation.pipeline import generate

    if not args.question:
        logger.error("Please provide a question with: python main.py query \"your question\"")
        sys.exit(1)

    # Show the user each step and how long they have waited, instead of the
    # developer log (back with --verbose).
    if not args.verbose:
        logging.getLogger().setLevel(logging.WARNING)
        from transformers.utils import logging as hf_logging
        hf_logging.disable_progress_bar()  # "Loading weights" bar
    handler = logging.StreamHandler()
    handler.setFormatter(_ElapsedFormatter())
    progress = logging.getLogger("rag.progress")
    progress.setLevel(logging.INFO)
    progress.propagate = False
    progress.addHandler(handler)

    first_call = len(CALL_LOG)
    result = retrieve(
        args.question,
        top_k=args.top_k,
        expand_queries=not args.no_expand,
    )

    # Stream the answer as it is written; the rule above it goes out with the
    # first words, so the progress lines stay above it.
    streamed = []

    def show(text):
        if not streamed:
            print("\n" + "=" * 60)
        streamed.append(text)
        print(text, end="", flush=True)

    answer = generate(result, on_token=show)
    if not streamed:  # nothing to generate (no documents found)
        print("\n" + "=" * 60 + "\n" + answer.answer, end="")
    print("\n" + "=" * 60)

    if answer.sources:
        print(f"\nFontes ({len(answer.sources)}):")
        for s in answer.sources:
            score_label = s.get("score_type", "cosine")
            print(f"  [{s['n']}] {s['party']} – {s.get('section', '')} ({score_label}={s['similarity']})")

    calls = CALL_LOG[first_call:]
    if calls:
        tokens_in = sum(c["prompt_tokens"] for c in calls)
        tokens_out = sum(c["completion_tokens"] for c in calls)
        cost = sum(c["cost"] for c in calls)
        print(f"\nModelos ({len(calls)} chamadas, {tokens_in} tokens in / {tokens_out} out, ${cost:.4f}):")
        for c in calls:
            print(f"  {c['step']}: {c['model']} ({c['secs']:.1f}s)")


def cmd_eval(args):
    from src.rag.evaluation.pipeline import evaluate

    variants = [v.strip() for v in args.variants.split(",")] if args.variants else None
    results = evaluate(
        variant_names=variants,
        dataset_path=args.dataset,
        curated_only=args.curated_only,
        split=args.split,
        k=args.top_k,
        use_judge=not args.no_judge,
        judge_model=args.judge_model,
    )

    print("\n" + "=" * 60)
    print("Evaluation summary (means over dataset):")
    for r in results:
        print(f"\n[{r.variant}]  (n={r.dataset_size})")
        for metric, value in r.aggregate.items():
            print(f"  {metric:<18} {value}")
    print("=" * 60)
    print("Leaderboard refreshed in the reports directory.")


# ---------------------------------------------------------------------------
# Argument parser
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="RAG System for Portuguese Political Programs Analysis",
    )
    sub = parser.add_subparsers(dest="command", help="Available commands")

    # parse
    p_parse = sub.add_parser("parse", help="Convert PDFs to markdown via marker_single")
    p_parse.set_defaults(func=cmd_parse)
    p_parse.add_argument("--input-dir", default="data/0_raw", help="PDF source directory")
    p_parse.add_argument("--output-dir", default="data/1_markdown/_raw", help="Markdown output directory (raw, before cleaning)")

    # clean
    p_clean = sub.add_parser("clean", help="Rebuild header structure of raw markdown into <party>/<stem>-clean.md")
    p_clean.set_defaults(func=cmd_clean)
    p_clean.add_argument("--party", type=str, default=None, help="Only clean this party key (e.g. 'be')")
    p_clean.add_argument("--markdown-dir", default="data/1_markdown", help="Markdown root (reads <root>/_raw)")
    p_clean.add_argument("--model", type=str, default=None, help="OpenRouter model for the structure pass")

    # index
    p_index = sub.add_parser("index", help="Run the indexing pipeline (chunk → classify → embed → store)")
    p_index.set_defaults(func=cmd_index)
    p_index.add_argument("--party", type=str, default=None, help="Only index files matching this party key (e.g. 'livre')")
    p_index.add_argument("--all", action="store_true", help="Index all parties (the default without --party)")
    p_index.add_argument("--drop", action="store_true", help="Drop existing table before indexing")
    resume = p_index.add_mutually_exclusive_group()
    resume.add_argument("--classify-only", action="store_true", help="Stop after classify and save checkpoint JSON (no DB write)")
    resume.add_argument("--from-classified", type=str, default=None, help="Load classified chunks from JSON and skip chunk/classify")
    p_index.add_argument("--contextual-headers", action="store_true",
                         help="Embed 'party | section path' + text (content stored unchanged)")
    p_index.add_argument("--table", type=str, default=None,
                         help="Target table (default postgresql.table_name), e.g. indexing.contextual_table")
    p_index.add_argument("--no-classify", action="store_true",
                         help="Skip LLM topic classification (overrides indexing.use_llm_classification). "
                              "Chunks keep their default topics, so topic filtering and topic_exploration "
                              "routing will not work on the resulting index.")
    p_index.add_argument("--chunk-strategy", type=str, default=None,
                         choices=[s.value for s in ChunkStrategy],
                         help="Chunk windowing strategy (default: indexing.chunk_strategy from config). "
                              "'char' is the truncating baseline kept for ablations.")

    # query
    p_query = sub.add_parser("query", help="Ask a question to the RAG system")
    p_query.set_defaults(func=cmd_query)
    p_query.add_argument("question", nargs="?", type=str, help="The question to ask")
    p_query.add_argument("-k", "--top-k", type=int, default=None, help="Number of documents to retrieve (default: retrieval.default_top_k)")
    p_query.add_argument("--no-expand", action="store_true", help="Disable multi-query expansion")
    p_query.add_argument("-v", "--verbose", action="store_true", help="Show the developer log, not just the steps")

    # eval
    p_ev = sub.add_parser("eval", help="Run the evaluation harness over one or more variants")
    p_ev.set_defaults(func=cmd_eval)
    p_ev.add_argument("--variants", type=str, default=None,
                      help="Comma-separated variant names (naive,multiquery,routed,current). "
                           "Defaults to config evaluation.variants.")
    p_ev.add_argument("--dataset", type=str, default=None, help="Gold-set JSON path")
    p_ev.add_argument("--curated-only", action="store_true", help="Only evaluate human-validated questions")
    p_ev.add_argument("--split", choices=["dev", "test"], default=None,
                      help="Only evaluate one split: dev while tuning, test for headline numbers")
    p_ev.add_argument("-k", "--top-k", type=int, default=None, help="Chunks retrieved per flat route for every variant "
                           "(default: evaluation.top_k); fan-outs keep top_k_per_party per party")
    p_ev.add_argument("--judge-model", type=str, default=None, help="Override the LLM-judge model")
    p_ev.add_argument("--no-judge", action="store_true", help="Skip the (LLM) generation-judge metrics")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    if not hasattr(args, "func"):
        parser.print_help()
        sys.exit(1)
    args.func(args)


if __name__ == "__main__":
    main()
