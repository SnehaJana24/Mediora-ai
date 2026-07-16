import joblib
from embedding import (
    extract_text_from_all_pdfs,
    create_chunks,
    generate_embedding
)

import numpy as np


def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def build_vector_store():
    print("Reading PDFs...")

    text = extract_text_from_all_pdfs()

    print("Creating Chunks...")

    chunks = create_chunks(text)

    print(f"Total Chunks: {len(chunks)}")

    store = []

    for i, chunk in enumerate(chunks):

        print(f"Embedding Chunk {i+1}/{len(chunks)}")

        vector = generate_embedding(chunk)

        store.append({
            "text": chunk,
            "vector": vector
        })

    print("\nVector Store Ready!")

    joblib.dump(store, "vector_store.pkl")

    print("\nVector Store Saved Successfully!")

    return store


def search(query, vector_store, top_k=5):

    query_vector = np.array(generate_embedding(query))
    query_vector = query_vector / np.linalg.norm(query_vector)

    scores = []

    for item in vector_store:

       doc_vector = np.array(item["vector"])
       doc_vector = doc_vector / np.linalg.norm(doc_vector)

       score = np.dot(query_vector, doc_vector)

       scores.append((score, item["text"]))

    scores.sort(reverse=True)
    print("\nTop Retrieved Chunks:\n")

    for score, text in scores[:5]:
      print("=" * 80)
      print(round(score, 3))
      print(text[:300])
      print()

    filtered = []

    for score, text in scores:
       if score > 0.40:
           filtered.append((score, text))

    return filtered[:top_k]


if __name__ == "__main__":

    vector_db = build_vector_store()

    question = input("\nAsk a Medical Question: ")

    results = search(question, vector_db)

    print("\nTop Relevant Chunks\n")

    for score, text in results:

        print("=" * 80)
        print("Similarity:", round(score, 3))
        print(text[:600])
        print()