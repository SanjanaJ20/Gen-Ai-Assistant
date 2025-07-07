import re
from transformers import pipeline



# Load the Hugging Face model
qa_model = pipeline("text2text-generation", model="google/flan-t5-small")

# Optional: Clean up raw text before prompt
def clean_text(text):
    text = re.sub(r"\[\d+\]", "", text)        # Remove [16], [1], etc.
    text = re.sub(r"\b\d+\.", "", text)        # Remove "16.", "27.", etc.
    text = text.replace("et al.", "")          # Remove "et al."
    text = re.sub(r"\s+", " ", text)           # Collapse multiple whitespaces
    return text.strip()

# Answer a user question using extracted PDF content
def answer_question(text, question):
    prompt = (
        f"You are a helpful assistant. Answer the following question clearly using the given context. "
        f"If the context is not enough, you may use general knowledge.\n\n"
        f"Context:\n{text[:3000]}\n\nQuestion:\n{question}"
    )
    result = qa_model(prompt, max_length=150, do_sample=False)
    return result[0]['generated_text']

# Generate 3 MCQs from the extracted document text
def generate_questions(text):
    cleaned_text = clean_text(text[:3000])

    prompt = (
        "Based on the following context, generate 3 multiple choice questions. "
        "Each question must have exactly 4 options labeled A), B), C), D), and clearly state the correct answer in the end like this: Answer: A\n\n"
        f"Context:\n{cleaned_text}"
    )

    result = qa_model(prompt, max_length=512, do_sample=False)
    output = result[0]['generated_text'].strip()

    print("=== MODEL OUTPUT ===")
    print(output)

    questions = []
    blocks = output.split("Answer:")

    for i in range(len(blocks) - 1):
        q_block = blocks[i].strip()
        answer_block = blocks[i + 1].strip()

        lines = q_block.split("\n")
        if len(lines) < 5:
            continue

        question = lines[0].strip()
        options = []

        for line in lines[1:5]:
            if line.startswith(("A)", "B)", "C)", "D)")):
                options.append(line[2:].strip())
            else:
                options.append("")

        answer_letter = answer_block[0].upper()
        if answer_letter not in "ABCD":
            continue

        try:
            correct_answer = options[ord(answer_letter) - ord("A")]
        except IndexError:
            correct_answer = options[0]

        questions.append({
            "question": question,
            "options": options,
            "answer": correct_answer
        })

    return questions



    

   
