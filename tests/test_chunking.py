import os
import sys
import json
from pathlib import Path

# Add src to path so we can import our module
sys.path.append(str(Path(__file__).parent.parent / "src"))

from data.preprocessing.chunking import chunk_political_manifesto

def test_chunking_with_sample_files():
    """Test chunking with actual political manifesto files"""
    
    # Paths to your sample files
    data_dir = Path(__file__).parent.parent / "data" / "1_markdown"
    ad_file = data_dir / "ad" / "ad-2024-manual.md"
    livre_file = data_dir / "livre" / "livre-2024-manual.md"
    
    # Test both files
    test_files = [
        ("AD", ad_file),
        ("LIVRE", livre_file)
    ]
    
    for party_name, file_path in test_files:
        if file_path.exists():
            print(f"\n{'='*60}")
            print(f"Testing {party_name} manifesto: {file_path.name}")
            print(f"{'='*60}")
            
            # Read file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Chunk the content
            chunks = chunk_political_manifesto(content)
            
            # Print summary
            print(f"Original file size: {len(content):,} characters")
            print(f"Number of chunks: {len(chunks)}")
            print(f"Average chunk size: {sum(c['size'] for c in chunks) // len(chunks):,} characters")
            print(f"Chunk size range: {min(c['size'] for c in chunks)} - {max(c['size'] for c in chunks)} characters")
            
            # Print first few chunks with details
            print(f"\nFirst 3 chunks preview:")
            print("-" * 40)
            
            for i, chunk in enumerate(chunks[:3]):
                print(f"\nChunk {i+1}:")
                print(f"Size: {chunk['size']} chars, {chunk['word_count']} words")
                print(f"Metadata: {chunk['metadata']}")
                print(f"Content preview (first 200 chars):")
                print(f"'{chunk['content'][:200]}...'")
                print("-" * 40)
            
            # Save detailed output to file
            output_file = Path(__file__).parent / f"chunking_output_{party_name.lower()}.json"
            save_chunks_to_file(chunks, output_file, party_name)
            
            # Save human-readable version
            readable_file = Path(__file__).parent / f"chunking_output_{party_name.lower()}.txt"
            save_chunks_readable(chunks, readable_file, party_name)
            
        else:
            print(f"File not found: {file_path}")

def save_chunks_to_file(chunks, output_file, party_name):
    """Save chunks to JSON file for detailed inspection"""
    output_data = {
        'party': party_name,
        'total_chunks': len(chunks),
        'chunks': chunks
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"Detailed chunks saved to: {output_file}")

def save_chunks_readable(chunks, output_file, party_name):
    """Save chunks in human-readable format"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"CHUNKING ANALYSIS - {party_name}\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Total chunks: {len(chunks)}\n")
        f.write(f"Average size: {sum(c['size'] for c in chunks) // len(chunks)} characters\n\n")
        
        for i, chunk in enumerate(chunks):
            f.write(f"CHUNK {i+1}\n")
            f.write("-" * 20 + "\n")
            f.write(f"Size: {chunk['size']} chars, {chunk['word_count']} words\n")
            f.write(f"Metadata: {chunk['metadata']}\n")
            f.write(f"Content:\n{chunk['content']}\n\n")
            f.write("=" * 60 + "\n\n")
    
    print(f"Human-readable chunks saved to: {output_file}")

def save_chunks_with_analysis(chunks, analysis, output_file, party_name):
    """Save chunks with analysis to JSON file"""
    output_data = {
        'party': party_name,
        'analysis': analysis,
        'chunks': chunks
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"Results saved to: {output_file}")

if __name__ == "__main__":
    # Run tests
    test_chunking_with_sample_files()
