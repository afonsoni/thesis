"""
CLI entry-point for the RAG System for Political Programs Analysis.

Commands:
    python main.py parse   [--input-dir ...] [--output-dir ...]
    python main.py index   [--party X] [--all] [--drop] [--summaries]
                           [--classify-only] [--from-classified PATH]
                           [--checkpoint-out PATH] [--no-checkpoint]
    python main.py query   "question" [--top-k 5] [--no-expand]
    python main.py eval-dataset [--sample-size 60] [--types ...] [--out PATH]
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

    if args.classify_only and args.from_classified:
        logger.error("Cannot combine --classify-only with --from-classified")
        sys.exit(2)

    party_filter = None if args.all else args.party
    count = index_documents(
        party_filter=party_filter,
        chunk_strategy=args.chunk_strategy,
        use_llm_classification=False if args.no_classify else None,
        generate_chunk_summaries=args.summaries,
        drop_existing=args.drop,
        classified_input_path=args.from_classified,
        checkpoint_output_path=args.checkpoint_out,
        classify_only=args.classify_only,
        save_checkpoint=not args.no_checkpoint,
    )
    logger.info("Processed %d chunks total.", count)


def cmd_query(args):
    from src.rag.common.llm_client import CALL_LOG
    from src.rag.retrieval.pipeline import retrieve
    from src.rag.generation.pipeline import generate

    if not args.question:
        logger.error("Please provide a question with: python main.py query \"your question\"")
        sys.exit(1)

    first_call = len(CALL_LOG)
    result = retrieve(
        args.question,
        top_k=args.top_k,
        expand_queries=not args.no_expand,
    )

    answer = generate(result)

    print("\n" + "=" * 60)
    print(answer.answer)
    print("=" * 60)

    if answer.sources:
        print(f"\nFontes ({len(answer.sources)}):")
        for s in answer.sources:
            score_label = s.get("score_type", "cosine")
            print(f"  • {s['party']} – {s.get('section', '')} ({score_label}={s['similarity']})")

    calls = CALL_LOG[first_call:]
    if calls:
        print(f"\nModelos ({len(calls)} chamadas):")
        for step, model in calls:
            print(f"  {step}: {model}")


def cmd_eval_dataset(args):
    from src.rag.evaluation.dataset import build_dataset, save_dataset

    types = [t.strip() for t in args.types.split(",")] if args.types else None
    dataset = build_dataset(
        sample_size=args.sample_size,
        types=types,
        model=args.model,
    )
    if not dataset.questions:
        logger.error("No questions generated. Is the index populated? (python main.py index --all)")
        sys.exit(1)
    save_dataset(dataset, args.out)
    logger.info(
        "Generated %d questions → %s. Review and set curated=true on the best ones "
        "(e.g. copy into golden.json).",
        len(dataset.questions),
        args.out,
    )


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
    p_parse.add_argument("--input-dir", default="data/0_raw", help="PDF source directory")
    p_parse.add_argument("--output-dir", default="data/1_markdown/_raw", help="Markdown output directory (raw, before cleaning)")

    # index
    p_clean = sub.add_parser("clean", help="Rebuild header structure of raw markdown into <party>/<stem>-clean.md")
    p_clean.add_argument("--party", type=str, default=None, help="Only clean this party key (e.g. 'be')")
    p_clean.add_argument("--markdown-dir", default="data/1_markdown", help="Markdown root (reads <root>/_raw)")
    p_clean.add_argument("--model", type=str, default=None, help="OpenRouter model for the structure pass")

    p_index = sub.add_parser("index", help="Run the indexing pipeline (chunk → classify → embed → store)")
    p_index.add_argument("--party", type=str, default=None, help="Only index files matching this party key (e.g. 'livre')")
    p_index.add_argument("--all", action="store_true", help="Index all parties")
    p_index.add_argument("--drop", action="store_true", help="Drop existing table before indexing")
    p_index.add_argument("--summaries", action="store_true", help="Generate LLM summaries for multi-representation indexing")
    p_index.add_argument("--classify-only", action="store_true", help="Stop after classify and save checkpoint JSON (no DB write)")
    p_index.add_argument("--from-classified", type=str, default=None, help="Load classified chunks from JSON and skip chunk/classify")
    p_index.add_argument("--checkpoint-out", type=str, default=None, help="Output path for classified checkpoint JSON")
    p_index.add_argument("--no-checkpoint", action="store_true", help="Disable automatic classified checkpoint saving")
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
    p_query.add_argument("question", nargs="?", type=str, help="The question to ask")
    p_query.add_argument("-k", "--top-k", type=int, default=5, help="Number of documents to retrieve")
    p_query.add_argument("--no-expand", action="store_true", help="Disable multi-query expansion")

    # eval-dataset
    p_evd = sub.add_parser("eval-dataset", help="Generate a synthetic gold set anchored to indexed chunks")
    p_evd.add_argument("--sample-size", type=int, default=60, help="Total number of questions to generate")
    p_evd.add_argument("--types", type=str, default=None,
                       help="Comma-separated query types (single_party,comparison,topic_exploration,general)")
    p_evd.add_argument("--model", type=str, default=None, help="OpenRouter model for question generation")
    p_evd.add_argument("--out", type=str, default="data/eval/questions/synthetic.json",
                       help="Output path for the generated dataset")

    # eval
    p_ev = sub.add_parser("eval", help="Run the evaluation harness over one or more variants")
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

    if args.command == "parse":
        cmd_parse(args)
    elif args.command == "clean":
        cmd_clean(args)
    elif args.command == "index":
        cmd_index(args)
    elif args.command == "query":
        cmd_query(args)
    elif args.command == "eval-dataset":
        cmd_eval_dataset(args)
    elif args.command == "eval":
        cmd_eval(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
