"""
CLI entry-point for the RAG System for Political Programs Analysis.

Commands:
    python main.py parse   [--input-dir ...] [--output-dir ...]
    python main.py index   [--party X] [--all] [--drop] [--no-llm] [--summaries]
    python main.py query   "question" [--top-k 5] [--no-expand]
"""

import argparse
import logging
import sys

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


def cmd_index(args):
    from src.rag.indexing.pipeline import index_documents

    party_filter = None if args.all else args.party
    count = index_documents(
        party_filter=party_filter,
        use_llm_classification=not args.no_llm,
        generate_chunk_summaries=args.summaries,
        drop_existing=args.drop,
    )
    logger.info("Indexed %d chunks total.", count)


def cmd_query(args):
    from src.rag.retrieval.pipeline import retrieve
    from src.rag.generation.pipeline import generate

    if not args.question:
        logger.error("Please provide a question with: python main.py query \"your question\"")
        sys.exit(1)

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
            print(f"  • {s['party']} – {s.get('section', '')} (sim={s['similarity']})")


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
    p_parse.add_argument("--output-dir", default="data/1_markdown", help="Markdown output directory")

    # index
    p_index = sub.add_parser("index", help="Run the indexing pipeline (chunk → classify → embed → store)")
    p_index.add_argument("--party", type=str, default=None, help="Only index files matching this party key (e.g. 'livre')")
    p_index.add_argument("--all", action="store_true", help="Index all parties")
    p_index.add_argument("--drop", action="store_true", help="Drop existing table before indexing")
    p_index.add_argument("--no-llm", action="store_true", help="Use keyword fallback instead of LLM for classification")
    p_index.add_argument("--summaries", action="store_true", help="Generate LLM summaries for multi-representation indexing")

    # query
    p_query = sub.add_parser("query", help="Ask a question to the RAG system")
    p_query.add_argument("question", nargs="?", type=str, help="The question to ask")
    p_query.add_argument("-k", "--top-k", type=int, default=5, help="Number of documents to retrieve")
    p_query.add_argument("--no-expand", action="store_true", help="Disable multi-query expansion")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "parse":
        cmd_parse(args)
    elif args.command == "index":
        cmd_index(args)
    elif args.command == "query":
        cmd_query(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
