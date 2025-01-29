import re
import argparse
from pathlib import Path

def clean_text(txt_path, output_folder, output_filename):
    # Get the text from the txt file
    with open(txt_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Remove headers, footers, and page numbers
    text = re.sub(r'Pág\.\s*\d+', '', text)  # Remove "Pág. X"
    text = re.sub(r'\d+\s+PLANO DE AÇÃO.*2024', '', text)  # Remove repeating headers
    text = re.sub(r'\n\s*\n', '\n', text)  # Remove empty lines
    
    # Handle repeated words (example logic, may need refinement)
    text = re.sub(r'(\b\w+\b)(\s+\1\b)+', r'\1', text)  # Remove repeated words
    
    # Normalize line breaks
    text = re.sub(r'(?<!\.)\n(?!\n)', ' ', text)  # Merge single line breaks
    
    # Create cleaned txt filename
    txt_filename = f"{output_filename}.txt"
    txt_path = output_folder / txt_filename
    
    # Save cleaned text to txt file
    with open(txt_path, 'w', encoding='utf-8') as file:
        file.write(text)
    
    return txt_filename

def clean_manifesto(folder_path, output_folder=None):
    """
    Clean text in the specified folder path and save all as cleaned txt file.
    
    Args:
        folder_path (str): Path to the txt folder file
        output_folder (str, optional): Path to save the txt file. 
                                    If None, saves in the same folder as txt file.
        
    Returns:
        filename: txt filename
    """
    
    # Convert the folder paths to Path objects
    folder = Path(folder_path)
    if output_folder is None:
        output_folder = folder.parent
    else:
        output_folder = Path(output_folder)
        output_folder.mkdir(parents=True, exist_ok=True)
    
    # Get files from folder
    txt_files = list(folder.glob("*.txt"))
    
    # Check if there are txt files in the folder
    if not txt_files:
        raise FileNotFoundError(f"No txt files found in the folder: {folder}")
    
    # Create output filename
    output_filename = f"{folder.stem}-cleaned"

    # Iterate through all txt files in the folder
    for txt_file in txt_files:
        try:
            # Clean text from the txt file
            txt_filename = clean_text(txt_file, output_folder, output_filename)
            print(f"Successfully cleaned text: {txt_file.name}")
            print(f"Saved as: {txt_filename}")
        except Exception as e:
            print(f"Error cleaning text: {str(e)}")
    
    return output_filename


def main():
    parser = argparse.ArgumentParser(description='Clean text extracted from PDFs.')
    parser.add_argument('txt_folder_path', help='Path to the folder with raw text file')
    parser.add_argument('--output', '-o', help='Output folder path for txt files (optional)')
    
    # Parse the arguments
    args = parser.parse_args()
    
    try:
        clean_manifesto(args.txt_folder_path, args.output)
        print(f"Successfully cleaned txt folder: {args.txt_folder_path}")
    except Exception as e:
        print(f"Error cleaning txt folder: {str(e)}")

if __name__ == '__main__':
    main()
