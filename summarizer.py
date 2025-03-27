import pdfplumber
from transformers import pipeline

# Load Pretrained NLP Model
summarizer = pipeline("summarization")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# Function to summarize text
def summarize_text(text, max_length=200):
    summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)
    return summary[0]['summary_text']
