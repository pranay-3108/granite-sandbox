import time

import ollama
from PyPDF2 import PdfReader


PDF_FILE = "sample_resume.pdf"
MODEL = "granite3.3:2b"


def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text.append(page_text.strip())
    return "\n".join(text)


def run_model(text):
    prompt = f"""
Extract only technical skills from this resume.

Return short bullet points.

Resume:
{text}
"""

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]


def main():
    text = extract_text(PDF_FILE)

    start = time.time()
    print("running model...\n")

    answer = run_model(text)

    print(answer)
    print(f"\ntook {round(time.time() - start, 2)}s")


if __name__ == "__main__":
    main()
