from pdfminer.high_level import extract_text
import os
from pathlib import Path
import argparse

def extract_pdfs_from_folder(folder_path, output_folder=None):
    """
    Extract text from all PDF files in the specified folder and save as txt files.
    
    Args:
        folder_path (str): Path to the folder containing PDF files
        output_folder (str, optional): Path to save the txt files. 
                                    If None, saves in the same folder as PDFs
        
    Returns:
        dict: Dictionary with PDF filenames as keys and extracted text as values
    """
    # Convert the folder paths to Path objects
    folder = Path(folder_path)
    if output_folder is None:
        output_folder = folder
    else:
        output_folder = Path(output_folder)
        output_folder.mkdir(parents=True, exist_ok=True)
    
    # Dictionary to store filename and extracted text
    extracted_texts = {}
    
    # Check if the folder exists
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")
    
    # Iterate through all files in the folder
    for file in folder.glob("*.pdf"):
        try:
            # Extract text from the PDF
            text = extract_text(file)
            # Store the text with the filename as key
            extracted_texts[file.name] = text
            
            # Create txt filename
            txt_filename = f"txt_{file.stem}.txt"
            txt_path = output_folder / txt_filename
            
            # Save text to txt file
            with open(txt_path, 'w', encoding='utf-8') as file:
                file.write(text)
            
            print(f"Successfully processed: {file.name}")
            print(f"Saved as: {txt_filename}")
            
        except Exception as e:
            print(f"Error processing {file.name}: {str(e)}")
    
    return extracted_texts

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Extract text from PDFs and save as txt files.')
    parser.add_argument('folder_path', help='Path to the folder containing PDF files')
    parser.add_argument('--output', '-o', help='Output folder path for txt files (optional)')
    
    # Parse arguments
    args = parser.parse_args()
    
    try:
        texts = extract_pdfs_from_folder(args.folder_path, args.output)
        print(f"\nProcessed {len(texts)} PDF files")
        
        # Example of accessing the extracted text
        for filename, text in texts.items():
            print(f"\nFilename: {filename}")
            print(f"Text preview (first 100 chars): {text[:100]}")
            
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
        
if __name__ == "__main__":
    main()