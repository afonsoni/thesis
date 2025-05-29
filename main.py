import argparse

# Import the components of the base RAG implementation
from src.embeddings.embedding_generator import generate_and_store_embeddings
from src.rag.base.base_rag import rag_query

def setup_data_pipeline():
    """Run the initial data processing pipeline"""
    print("Setting up data pipeline...")
    generate_and_store_embeddings()
    print("Data pipeline setup complete.")

def run_rag(query=None, top_k=5, implementation="base", system_prompt=None):
    """Run the RAG implementation"""
    if implementation == "base":
        # Generate and store embeddings for the base implementation
        return rag_query(query, top_k, system_prompt)
    elif implementation == "corrective":
        print("In the works...")
        # Placeholder for corrective implementation
    elif implementation == "agentic":
        print("In the works...")
        # Placeholder for agentic implementation
    else:
        raise ValueError(f"Unknown implementation: {implementation}")

def main():
    parser = argparse.ArgumentParser(
        description="RAG System for Political Programs Analysis"
    )
    parser.add_argument(
        "--setup", action="store_true", help="Run the initial data processing pipeline"
    )
    parser.add_argument(
        "--implementation",
        type=str,
        choices=["base", "corrective", "agentic"],
        default="base",
        help="Choose which RAG implementation to use (default: base)",
    )
    parser.add_argument("--query", type=str, help="The question to ask the RAG system")
    parser.add_argument(
        "-k",
        "--top-k",
        type=int,
        default=5,
        help="Number of documents to retrieve (default: 5)",
    )
    parser.add_argument(
        "-s", "--system", type=str, help="Custom system prompt for the LLM"
    )

    args = parser.parse_args()

    # If setup flag is provided, run the data processing pipeline
    if args.setup:
        setup_data_pipeline()

    # Run the selected RAG implementation
    if args.implementation == "base":
        run_rag(query=args.query, top_k=args.top_k, system_prompt=args.system)
    elif args.implementation == "corrective":
        run_rag(query=args.query, top_k=args.top_k, implementation="corrective", system_prompt=args.system)
    elif args.implementation == "agentic":
        run_rag(query=args.query, top_k=args.top_k, implementation="agentic", system_prompt=args.system)
    else:
        print(f"Unknown implementation: {args.implementation}")

if __name__ == "__main__":
    main()
