import streamlit as st
from utils.parser import extract_text_from_pdf
from utils.summarizer import summarize_document
from utils.qa_engine import answer_question, generate_questions

st.set_page_config(page_title="GenAI Smart Assistant")
st.title("📚 Smart Assistant for Research Summarization")

# Upload a PDF or TXT file
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    # Extract text
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = uploaded_file.read().decode("utf-8")

    st.write("📄 Word count:", len(text.split()))

    with st.expander("📄 Show Extracted Text from PDF"):
        st.text_area("Extracted Text", text, height=300)

    # Auto Summary
    st.subheader("🔍 Auto Summary")
    try:
        summary = summarize_document(text)
        st.write(summary)
    except Exception as e:
        st.error(f"❌ Summary failed: {e}")

    # Ask Anything
    st.subheader("💬 Ask Anything")
    user_q = st.text_input("Enter your question here:")
    if st.button("Get Answer"):
        try:
            answer = answer_question(text, user_q)
            st.success(answer)
        except Exception as e:
            st.error(f"❌ Question answering failed: {e}")

    # ✅ Challenge Me Section — properly indented inside uploaded_file block
    st.subheader("🧠 Challenge Me")
    st.write("📄 Word count:", len(text.split()))

    if st.button("Generate Questions"):
        questions = generate_questions(text)
        st.write("🧠 Debug MCQ Output:", questions)

        if not questions or len(questions) == 0:
            st.warning("⚠️ Model failed to generate MCQs from context. Showing sample MCQs for demo purposes.")
            questions = [
                {
                    "question": "Which gene is most associated with kidney stone formation?",
                    "options": ["ANKRD1", "HO-1", "TP53", "BRCA1"],
                    "answer": "ANKRD1"
                },
                {
                    "question": "Which imaging technique was used in the 2024 study?",
                    "options": ["MRI", "CT Scan", "X-ray", "Ultrasound"],
                    "answer": "CT Scan"
                }
            ]

        st.success("✅ Questions ready!")
        for idx, q in enumerate(questions):
            st.markdown(f"**Q{idx+1}: {q['question']}**")
            user_choice = st.radio("Select your answer:", q['options'], key=f"q{idx}")
            if st.button(f"Submit Answer {idx+1}", key=f"submit_{idx}"):
                if user_choice == q['answer']:
                    st.success("✅ Correct!")
                else:
                    st.error(f"❌ Incorrect. Correct answer: {q['answer']}")

