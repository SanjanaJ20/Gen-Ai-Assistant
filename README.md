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
