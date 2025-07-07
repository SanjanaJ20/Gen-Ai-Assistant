# 🧠 GenAI Research Assistant by Sanjana Jain

A smart, research-focused GenAI assistant built using Streamlit and Hugging Face Transformers.  
It allows users to upload research documents (PDF or TXT), extract text, generate summaries, ask questions, and create multiple-choice quizzes — all within a simple web interface.

---

## 🚀 Features

✅ Upload PDF or TXT documents  
✅ Extract clean text using PyMuPDF  
✅ Auto-summarize with Hugging Face Transformers  
✅ Ask document-based questions  
✅ Generate 3 MCQs with 4 options each  
✅ Shows fallback MCQs if model output fails  
✅ Clean UI with modern styling  
✅ Runs locally — no OpenAI needed  

---

## 🛠 Tech Stack

- Python 3.9+ (tested with 3.10)
- Streamlit
- Hugging Face Transformers
- PyMuPDF (`fitz`)
- Torch
- SentencePiece

---

## 📁 Folder Structure

genai-assistant/
├── app.py
├── requirements.txt
├── .env
├── README.md
├── .streamlit/
│ └── config.toml # Optional: lock Python version
└── utils/
├── parser.py
├── summarizer.py
└── qa_engine.py

yaml
Copy
Edit

---

## 🔧 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/SanjanaJ20/genai-assistant.git
cd genai-assistant
2. Create and Activate a Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows
✅ Recommended: Use Python 3.10
⚠️ Not compatible with Python 3.13 (build issue with sentencepiece)

3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Run the App
bash
Copy
Edit
streamlit run app.py
📦 Deployment Notes
⚠️ This app is currently not deployed on Streamlit Cloud due to sentencepiece build failures in Python 3.13 (Streamlit's default version).
✅ It works perfectly on local machines with Python 3.10.

📂 Optional: .env File (for OpenAI API)
If you want to enable OpenAI-based summarization or question answering:

Create a .env file:

env
Copy
Edit
OPENAI_API_KEY=your-openai-key-here
🧠 Built With
Streamlit

Hugging Face Transformers

PyMuPDF

SentencePiece

🙋‍♀️ Author
Sanjana Jain
📍 B.Tech (Data Science), AKTU
🔗 LinkedIn:https://www.linkedin.com/in/sanjana-jain-a55927298
📧 sanjanajain206@gmail.com
🏁 Final Notes
This project was developed as part of an internship assignment for EZ Labs, Gurugram.
It demonstrates real-world skills in GenAI, document processing, and question generation with fallback handling for robustness.
