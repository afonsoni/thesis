#!/usr/bin/env python3
"""
Simple example script to classify political chunks with topics.
"""
import json
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from data.preprocessing.topic_classification import classify_political_chunks, save_classified_chunks

def classify_chunks_from_json(input_file: str, output_file: str):
    """
    Load chunks from JSON file, classify them, and save with topics.
    
    Args:
        input_file: Path to chunking output JSON (like chunking_output_livre.json)
        output_file: Path to save classified chunks
    """
    print(f"Loading chunks from {input_file}")
    
    # Load existing chunks
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    chunks = data.get("chunks", [])
    party = data.get("party", "Unknown")
    
    print(f"Found {len(chunks)} chunks for {party}")
    
    # Classify chunks
    classified_chunks = classify_political_chunks(chunks)
    
    # Save classified chunks
    save_classified_chunks(classified_chunks, party, output_file)
    
    # Show summary
    topic_counts = {}
    for chunk in classified_chunks:
        topics = chunk.get("topics", [])
        for topic in topics:
            topic_counts[topic] = topic_counts.get(topic, 0) + 1
    
    print(f"\n📊 Topic Summary for {party}:")
    for topic, count in sorted(topic_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {topic}: {count}")
    
    # Show sample classified chunk
    if classified_chunks:
        sample = classified_chunks[0]
        print(f"\n📄 Sample classified chunk:")
        print(f"  Content: {sample['content'][:100]}...")
        print(f"  Topics: {sample['topics']}")
        print(f"  Classification: {sample['topic_classification']}")

def main():
    """Example usage"""
    # Example with LIVRE chunks
    input_file = "tests/chunking_output_livre.json"
    output_file = "data/2_processed/livre-2024-classified.json"
    
    if Path(input_file).exists():
        classify_chunks_from_json(input_file, output_file)
    else:
        print(f"Input file not found: {input_file}")
        print("Please run chunking first or provide correct path")

if __name__ == "__main__":
    main()