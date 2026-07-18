import os
from dotenv import load_dotenv
from google import genai
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader

load_dotenv()

# Gemini (used only for answer generation)
api_key = os.getenv("GEMINI_API_KEY")
generation_model = os.getenv("GEMINI_GEN_MODEL")

client = genai.Client(api_key=api_key)

# Local embedding model (FREE)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def extract_text_from_all_pdfs():

    docs_folder = "docs"

    all_text = ""

    for file in os.listdir(docs_folder):

        if file.endswith(".pdf"):

            print(f"Reading: {file}")

            pdf_path = os.path.join(docs_folder, file)

            reader = PdfReader(pdf_path)

            for page in reader.pages:

                text = page.extract_text()

                if text:

                    all_text += text + "\n"

    return all_text


def create_chunks(text, chunk_size=250, overlap=50):

    words = text.split()

    chunks = []

    step = chunk_size - overlap

    for i in range(0, len(words), step):

        chunk = words[i:i + chunk_size]

        chunks.append(" ".join(chunk))

    return chunks


def generate_embedding(text):

    return embedding_model.encode(text).tolist()