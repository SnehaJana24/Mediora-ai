import os
from dotenv import load_dotenv
from google import genai

from vector_store import build_vector_store, search
from prompts import SYSTEM_PROMPT

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
model = os.getenv("GEMINI_GEN_MODEL")
print("Model from .env:", model)

print("Building Medical Knowledge Base...")
import joblib

vector_db = joblib.load("vector_store.pkl")
print("Knowledge Base Ready!\n")

while True:

    question = input("Ask your medical question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    results = search(question, vector_db)

    context = "\n\n".join([text[:500] for _, text in results[:3]])

    prompt = SYSTEM_PROMPT.format(
        context=context,
        question=question
    )
    print("Context length:", len(context))
    print("Prompt length:", len(prompt))

    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt
        )

        print("\nMediora AI:\n")
        print(response.text)
        print("\n" + "-" * 80 + "\n")

    except Exception as e:
        print(f"\nError: {e}\n")