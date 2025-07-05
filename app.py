
import streamlit as st
from utils.parser import extract_text_from_pdf
from utils.summarizer import summarize_document
from utils.qa_engine import answer_question, generate_questions

st.set_page_config(page_title="GenAI Smart Assistant")
st.title("📚 Smart Assistant for Research Summarization")
st.markdown(
    """
    <style>
    body {
        background-color: #0f0f0f;
        color: white;
    }
    .stApp {
        background: transparent;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Upload a PDF or TXT file
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    # Extract text
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = uploaded_file.read().decode("utf-8")

    # Show extracted text (toggle)
    with st.expander("📄 Show Extracted Text from PDF"):
        st.text_area("Extracted Text", text, height=300)

    # Auto Summary Section
    st.subheader("🔍 Auto Summary")
    try:
        summary = summarize_document(text)
        st.write(summary)
    except Exception as e:
        st.error(f"❌ Summary failed: {e}")

    # Ask Anything Section
    st.subheader("💬 Ask Anything")
    user_q = st.text_input("Enter your question here:")
    if st.button("Get Answer"):
        try:
            answer = answer_question(text, user_q)
            st.success(answer)
        except Exception as e:
            st.error(f"❌ Question answering failed: {e}")

    # Challenge Section
    st.subheader("🧠 Challenge Me")
    if st.button("Generate Questions"):
        try:
            questions = generate_questions(text)
            st.success("Here are your questions:")
            st.write(questions)
        except Exception as e:
            st.error(f"❌ Failed to generate questions: {e}")
    else:
        st.warning("Please upload a PDF or TXT file to begin.")
