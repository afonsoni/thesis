import pymupdf
import argparse
from pathlib import Path

def extract_pdf(path, output_filename, output_folder=None, start_page=0, end_page=None):
    """
    Extract text from PDF in the specified path and save as txt file.
    
    Args:
        path (str): Path to the PDF file
        output_filename (str): Name of the PDF file
        output_folder (str, optional): Path to save the txt file. 
                                    If None, saves in the same folder as PDF
        start_page (int, optional): Page number to start extraction (default: 0)
        end_page (int, optional): Page number to end extraction (default: None)
        
    Returns:
        filename: PDF filename
        text: Extracted text from the PDF
    """
    
    # Convert the folder paths to Path objects
    pdf_path = Path(path)
    if output_folder is None:
        output_folder = pdf_path.parent
    else:
        output_folder = Path(output_folder)
        output_folder.mkdir(parents=True, exist_ok=True)
    
    # Check if the PDF file exists
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    # Extract text from the PDF
    with pymupdf.open(pdf_path) as pdf:
        text = ""
        for page_num in range(start_page-1, pdf.page_count if end_page is None else end_page):
            page = pdf.load_page(page_num)
            text += page.get_text()
    
    # Create txt filename
    txt_filename = f"{output_filename}.txt"
    txt_path = output_folder / txt_filename
    
    # Save text to txt file
    with open(txt_path, 'w', encoding='utf-8') as file:
        file.write(text)
    
    return pdf_path.name, text

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Extract text from PDFs and save as txt files.')
    parser.add_argument('pdf_path', help='Path to the PDF file')
    parser.add_argument('--filename', '-f', help='Name of the PDF file')
    parser.add_argument('--output', '-o', help='Output folder path for txt files (optional)')
    parser.add_argument('--start_page', '-s', type=int, help='Page number to start extraction (optional)')
    parser.add_argument('--end_page', '-e', type=int, help='Page number to end extraction (optional)')
    
    # Parse the arguments
    args = parser.parse_args()
    
    try:
        filename, text = extract_pdf(args.pdf_path, args.filename, args.output, args.start_page, args.end_page)
        print(f"Successfully processed: {filename}")
        print(f"Saved as: txt_{filename}.txt")
        print(f"Text preview (first 100 chars): {text[:100]}")
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()