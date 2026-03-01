"""
Main embedding generator module - orchestrates the processing pipeline.
"""
import os
import glob
from src.embeddings.text_processor import get_markdown_content, split_markdown_by_headers
from embeddings.database import DB

def generate_and_store_embeddings():
    """Main function to process all markdown files and store embeddings in Milvus"""
    
    # Initialize vector database
    db = DB()
    
    # Find all markdown files in the processed data directory
    data_dir = "data/processed"
    md_pattern = os.path.join(data_dir, "**", "*.md")
    md_files = glob.glob(md_pattern, recursive=True)
    
    if not md_files:
        print(f"No markdown files found in {data_dir}")
        return
    
    print(f"Found {len(md_files)} markdown files to process")
    
    # Collect all chunks from all files
    all_chunks = []
    
    # Process each markdown file
    for md_file in md_files:
        print(f"Processing {md_file}...")
        
        # Get content of the markdown file
        content = get_markdown_content(md_file)
        file_name = os.path.basename(md_file)
        
        # Split content into chunks based on headers
        chunks = split_markdown_by_headers(content, file_name)
        
        print(f"  Created {len(chunks)} chunks from {file_name}")
        all_chunks.extend(chunks)
    
    # Insert all chunks into vector database
    if all_chunks:
        all_data = db.insert_embeddings(all_chunks)

        print(f"All embeddings successfully stored in Milvus!")
        
        # Print summary statistics
        print_summary_statistics(all_data)
        
    else:
        print("No content found to process.")

def search_embeddings(query_text, top_k=5, filter_party=None, filter_topic=None, filter_affiliation=None):
    """Search for similar content based on a query text with optional filters"""
    vector_db = VectorDB()
    return vector_db.search_embeddings(query_text, top_k, filter_party, filter_topic, filter_affiliation)

def print_summary_statistics(all_data):
    """Print summary statistics about the processed data"""
    party_counts = {}
    topic_counts = {}
    affiliation_counts = {}
    
    for entry in all_data:
        party = entry['party_name']
        topic = entry['topic']
        affiliation = entry['affiliation']
        
        party_counts[party] = party_counts.get(party, 0) + 1
        topic_counts[topic] = topic_counts.get(topic, 0) + 1
        affiliation_counts[affiliation] = affiliation_counts.get(affiliation, 0) + 1
    
    print("\nSummary Statistics:")
    print(f"Total chunks: {len(all_data)}")
    print(f"Parties: {', '.join(party_counts.keys())}")
    print(f"Topics distribution: {topic_counts}")
    print(f"Affiliation distribution: {affiliation_counts}")

# Maintain backward compatibility
if __name__ == "__main__":
    generate_and_store_embeddings()
