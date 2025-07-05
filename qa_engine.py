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

   
