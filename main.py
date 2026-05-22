from PyPDF2 import PdfReader
import ollama
import time
import tracemalloc

pdf_file = "sample_resume.pdf"

reader = PdfReader(pdf_file)

text = ""

for page in reader.pages:
    text += page.extract_text()

prompt = f"""
Extract only technical skills from this resume.

Return short bullet points.

Resume:
{text}
"""

tracemalloc.start()

start = time.time()

print("running model...\n")

response = ollama.chat(
    model="granite3.3:2b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

current, peak = tracemalloc.get_traced_memory()

tracemalloc.stop()

answer = response["message"]["content"]

print(answer)

print(f"\ntook {round(time.time() - start, 2)}s")
print(f"peak memory: {round(peak / 1024 / 1024, 2)} MB")