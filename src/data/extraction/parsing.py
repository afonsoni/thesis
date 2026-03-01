"""
Module for extracting text content from PDF files and converting to markdown using marker
"""

import subprocess
import os


def parse_pdfs(
    pdf_dir="data/0_raw", output_dir="data/1_markdown", output_format="markdown"
):
    """
    Parse all PDF files in a directory and convert them to markdown using marker_single

    Args:
        pdf_dir: Directory containing PDF files
        output_dir: Directory to save markdown files
        output_format: Output format (usually markdown)
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Get all PDF files
    pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print(f"No PDF files found in {pdf_dir}")
        return

    print(f"Found {len(pdf_files)} PDF files to process")

    # Process each PDF file
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_dir, pdf_file)

        print(f"Processing {pdf_file}...")

        # Run marker_single for PDF extraction
        command = [
            "marker_single",
            pdf_path,
            "--output_dir",
            output_dir,
            "--output_format",
            output_format,
            "--use_llm",
        ]

        try:
            subprocess.run(command, check=True)
            print(f"Processed {pdf_file} successfully")

            # Erase image files if they exist
            image_files = [f for f in os.listdir(output_dir) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
            for image_file in image_files:
                image_path = os.path.join(output_dir, image_file)
                os.remove(image_path)

        except subprocess.CalledProcessError as e:
            print(f"Error processing {pdf_file}: {e}")

    print(f"Processed {len(pdf_files)} PDF files")


if __name__ == "__main__":
    parse_pdfs()
