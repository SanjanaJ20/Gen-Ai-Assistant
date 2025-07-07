import fitz  # PyMuPDF
import re

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def clean_text(text):
    # Remove extra whitespaces, newlines, and strange characters
    text = re.sub(r'\s+', ' ', text)        # Collapse multiple spaces
    text = re.sub(r'\n+', '\n', text)       # Normalize newlines
    return text.strip()
