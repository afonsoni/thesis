import subprocess
import os

def process_pdfs():
    input_dir = "programs"
    output_dir = "md_programs"
    output_format = "markdown"

    pdf_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith(".pdf")]

    for pdf in pdf_files:
        command = [
            "marker_single",
            pdf,
            "--output_dir", output_dir,
            "--output_format", output_format,
            "--disable_image_extraction"
        ]
        subprocess.run(command, check=True)
