# 🧠 GenAI Research Assistant by Sanjana Jain

A smart, research-focused GenAI assistant built using Streamlit and Hugging Face Transformers.  
It allows users to upload research documents (PDF or TXT), extract text, generate summaries, ask questions, and create multiple-choice quizzes — all within a simple web interface.

---

## 🚀 Features

✅ Upload PDF or TXT documents  
✅ Extract clean text using PyMuPDF  
✅ Auto-summarize with transformers  
✅ Ask document-based questions  
✅ Generate 3 MCQs with 4 options each  
✅ Clean UI with modern styling  
✅ Runs locally — no OpenAI needed  

---

## 🛠 Tech Stack

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
├── requirements.txt # Required packages
├── .env # Optional: for API keys
├── README.md # This file
└── utils/
├── parser.py # PDF text extraction
├── summarizer.py # Summarization logic
└── qa_engine.py # Q&A and MCQ logic

yaml
Copy
Edit

---

## 🔧 How to Run

### 1. Clone or Download

```bash
git clone https://github.com/SanjanaJ20/genai-assistant.git
cd genai-assistant
2. Create and Activate Virtual Environment (Windows)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
📝 Optional: .env File (For OpenAI Key)
env
Copy
Edit
## 🧠 Built With

- [Streamlit](https://streamlit.io/)
- [OpenAI API](https://platform.openai.com/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)

OPENAI_API_KEY=your-openai-key-here
🙋‍♀️ Author
Sanjana Jain
📍 B.Tech (Data Science), AKTU
🔗 LinkedIn:https://www.linkedin.com/in/sanjana-jain-a55927298
📧 sanjanajain206@gmail.com
