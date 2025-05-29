"""
Module for extracting text content from PDF files and converting to markdown using marker
"""
import subprocess
import os
import json
from datetime import datetime

def process_pdfs(pdf_dir="data/raw", output_dir="data/processed", output_format="markdown"):
    """
    Process all PDF files in a directory and convert them to markdown using marker_single
    
    Args:
        pdf_dir: Directory containing PDF files
        output_dir: Directory to save markdown files
        output_format: Output format (usually markdown)
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all PDF files
    pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print(f"No PDF files found in {pdf_dir}")
        return
    
    print(f"Found {len(pdf_files)} PDF files to process")
    
    # Process each PDF file
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_dir, pdf_file)
        file_name = os.path.splitext(pdf_file)[0]
        
        print(f"Processing {pdf_file}...")
        
        # Create output directory for this file if using subdirectories
        file_output_dir = os.path.join(output_dir, file_name)
        os.makedirs(file_output_dir, exist_ok=True)
        
        # Run marker_single for PDF extraction
        command = [
            "marker_single",
            pdf_path,
            "--output_dir",
            file_output_dir,
            "--output_format",
            output_format,
            "--disable_image_extraction",
        ]
        
        try:
            subprocess.run(command, check=True)
            print(f"Processed {pdf_file} successfully")
            
            # Create metadata file
            markdown_path = os.path.join(file_output_dir, f"{file_name}.md")
            metadata = {
                "source": pdf_file,
                "title": file_name,
                "extraction_date": datetime.now().isoformat(),
                "extraction_tool": "marker"
            }
            
            metadata_path = os.path.join(file_output_dir, f"{file_name}_meta.json")
            with open(metadata_path, 'w', encoding='utf-8') as meta_file:
                json.dump(metadata, meta_file, ensure_ascii=False, indent=2)
                
        except subprocess.CalledProcessError as e:
            print(f"Error processing {pdf_file}: {e}")
    
    print(f"Processed {len(pdf_files)} PDF files")

if __name__ == "__main__":
    process_pdfs()
