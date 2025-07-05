# Gen-Ai-Assistant
# 🧠 GenAI Research Assistant by Sanjana Jain

A smart, research-focused GenAI assistant built using Streamlit and Hugging Face Transformers.  
It helps users upload documents (PDF/TXT), extract text, generate summaries, answer questions, and create MCQs — all in one elegant web app.

---

## 🚀 Features

✅ Upload PDF or TXT documents  
✅ Extract and display clean text from files  
✅ Auto-summarize content in under 150 words  
✅ Ask natural language questions based on the file  
✅ Generate 3 multiple choice questions (MCQs) with 4 options  
✅ Minimalist and clean user interface  
✅ Local model: no OpenAI required  
✅ Custom styling and error handling included

---

## 🎯 Tech Stack

- Python 3.9+
- Streamlit
- Hugging Face Transformers
- PyMuPDF (`fitz`)
- Torch
- SentencePiece

---

## 📁 Folder Structure
genai-assistant/
│
├── app.py # Main Streamlit app
├── requirements.txt # All required Python libraries
├── README.md # Project documentation
├── .env # (Optional) for OpenAI API key
└── utils/ # Core functionality
├── parser.py # PDF/Text extraction
├── summarizer.py # Text summarization
└── qa_engine.py # Question answering and MCQ generation
### 🔧 Step 1: Clone or Download

```bash
git clone https://github.com/SanjanaJ20/genai-assistant.git
cd genai-assistant
Open Git Bash or CMD in your project folder:
bash
Copy
Edit
cd "C:\Users\sanja\OneDrive\Desktop\genai-assistant"
🔧 Step 2: Set up virtual environment (Windows)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
🔧 Step 3: Install required packages
bash
Copy
Edit
pip install -r requirements.txt
🔧 Step 4: Run the app
bash
Copy
Edit
streamlit run app.py

#qa_engine.py
from transformers import pipeline
import re

# Load text generation model
qa_model = pipeline("text2text-generation", model="google/flan-t5-small")

def answer_question(text, question):
    prompt = (
        f"You are a helpful assistant. Answer the following question clearly using the given context. "
        f"If the context is not enough, you may use general knowledge.\n\n"
        f"Context:\n{text[:3000]}\n\nQuestion:\n{question}"
    )
    result = qa_model(prompt, max_length=150, do_sample=False)
    return result[0]['generated_text']

def clean_text(raw_text):
    import re
    # Remove citations like [16], [21]
    cleaned = re.sub(r"\[\d+\]", "", raw_text)
    
    # Remove numbered bullets like "16.", "27.", etc.
    cleaned = re.sub(r"\b\d+\.", "", cleaned)

    # Remove author blocks like "et al."
    cleaned = cleaned.replace("et al.", "")

    # Replace multiple line breaks or spaces with single space
    cleaned = re.sub(r"\s+", " ", cleaned)

    # Trim to safe length and return
    return cleaned.strip()

def generate_questions(text):
    cleaned_text = clean_text(text[:3000])
    
    prompt = (
        "Based on the following context, generate 3 multiple choice questions. "
        "Each question must have exactly 4 options labeled A), B), C), D), and clearly state the correct answer in the end like this: Answer: A\n\n"
        f"Context:\n{cleaned_text}"
    )

    result = qa_model(prompt, max_length=400, do_sample=False)
    output = result[0]['generated_text'].strip()
    
    # Optional cleanup (to remove extra spacing)
    output = result[0]['generated_text'].strip()
    output = re.sub(r"\n{2,}", "\n", output)

    if len(output.strip()) < 30:
        return "📝 Not enough content to generate proper MCQs. Please upload a more detailed PDF."
    return output

#summarizer.py   
from transformers import pipeline

# Load summarizer model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_document(text):
    text = text.strip().replace("\n", " ")
    text = text[:4000]  # limit input size
    result = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return result[0]['summary_text']
#parser.py
import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

🙋‍♀️ Author
Sanjana Jain
📍 B.Tech (Data Science), AKTU
🔗 LinkedIn:https://www.linkedin.com/in/sanjana-jain-a55927298
📧 sanjanajain206@gmail.com

