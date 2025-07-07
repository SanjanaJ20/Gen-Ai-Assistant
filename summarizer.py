from transformers import pipeline

# Load summarizer model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_document(text):
    text = text.strip().replace("\n", " ")
    text = text[:4000]  # limit input size
    result = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return result[0]['summary_text']

