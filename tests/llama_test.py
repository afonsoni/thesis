import os
import json
import requests
import argparse

# Configuration
OLLAMA_API_URL = "http://localhost:11434/api/generate"
PROMPT_TEMPLATE = """
You are a text cleanup specialist tasked with improving the readability and organization of the following text. Your goal is to:

1. Remove redundant elements:
   - Eliminate repeated headers
   - Remove page numbers
   - Delete duplicate content or unnecessary repetitions

2. Preserve text integrity:
   - Maintain the original wording
   - Keep the original meaning and sequence of information
   - Do not add or remove content

3. Clean-up guidelines:
   - Remove running headers or footers
   - Strip out page break indicators
   - Eliminate unnecessary whitespace
   - Consolidate fragmented paragraphs

Text to clean:
{text}

IMPORTANT: Return ONLY the cleaned and reorganized text. Do not add commentary or explanations.
"""

def send_to_ollama(text, model="llama3.1"):
    """
    Sends text to the Ollama LLM for contextual cleanup.
    """
    payload = {
        "model": model,
        "prompt": PROMPT_TEMPLATE.format(text=text),
        "stream": False,
    }
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        
        # Debug: print full response
        print("Full API Response:")
        print(json.dumps(response.json(), indent=2))
        
        # Extract text based on the actual response structure
        response_data = response.json()
        
        # Adjust these lines based on the actual response structure
        full_text = response_data.get('response', '')
        
        return full_text
    except Exception as e:
        print(f"Error in API call: {e}")
        return None

def process_txt_files(input_folder, output_folder="cleaned"):
    """
    Processes all .txt files in a folder, sends them to the Ollama LLM, and saves the cleaned content.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_folder, filename)
            print(f"Processing file: {file_path}")

            # Read the file
            with open(file_path, "r", encoding="utf-8") as file:
                original_text = file.read()

            # Send text to Ollama
            cleaned_text = send_to_ollama(original_text)
            if cleaned_text:
                # Save cleaned text
                cleaned_file_path = os.path.join(output_folder, filename)
                with open(cleaned_file_path, "w", encoding="utf-8") as cleaned_file:
                    cleaned_file.write(cleaned_text)
                print(f"Saved cleaned text to {cleaned_file_path}")
            else:
                print(f"Failed to process file: {file_path}")

def main():
    parser = argparse.ArgumentParser(description='Process .txt files with Ollama LLM.')
    parser.add_argument('folder', help='Path to the folder containing .txt files')
    parser.add_argument('--output', '-o', help='Output folder path for cleaned txt files (optional)')
    args = parser.parse_args()
    
    process_txt_files(args.folder, args.output)


if __name__ == "__main__":
    main()
