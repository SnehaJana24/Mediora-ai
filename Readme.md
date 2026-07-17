# 🩺 Mediora AI

> **AI-Powered Medical Knowledge Assistant using Retrieval-Augmented Generation (RAG)**

Mediora AI is an intelligent medical chatbot that answers health-related questions using **Retrieval-Augmented Generation (RAG)**. It searches a curated medical knowledge base built from medical PDF documents using semantic search and generates context-aware responses with **Google Gemini AI**.

> **⚠️ Disclaimer:** Mediora AI is intended for educational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment.

---

# ✨ Features

- 🩺 AI-powered medical question answering
- 📚 Knowledge base built from medical PDF documents
- 🔍 Semantic search using Sentence Transformers
- 🤖 Google Gemini AI for natural language responses
- ⚡ Fast retrieval using precomputed vector embeddings
- 💬 ChatGPT-style multi-chat interface
- 📂 Health topic categories with suggested questions
- 📝 Conversation history
- 💡 Clickable example questions
- 🚫 Similarity threshold for improved retrieval accuracy
- 🔄 Automatic fallback to the medical knowledge base when Gemini is unavailable
- ⚠️ Graceful handling of API quota, server, and network errors
- 🎨 Clean and responsive Streamlit interface

---

# 🛠️ Tech Stack

| Technology            | Purpose                  |
| --------------------- | ------------------------ |
| Python                | Backend                  |
| Streamlit             | Web Application          |
| Google Gemini API     | Large Language Model     |
| Sentence Transformers | Text Embeddings          |
| NumPy                 | Cosine Similarity Search |
| Joblib                | Vector Database Storage  |
| python-dotenv         | Environment Variables    |

---

# 🏗️ Architecture

```text
                 User
                   │
                   ▼
          Streamlit Web Interface
                   │
                   ▼
          Sentence Transformer
          (Query Embedding)
                   │
                   ▼
        Vector Database (Joblib)
      Cosine Similarity Search
                   │
                   ▼
      Relevant Medical Chunks
                   │
                   ▼
          Google Gemini AI
          (RAG Prompt)
                   │
                   ▼
            Final Response
```

---

# 📂 Project Structure

```text
Mediora-ai/
│
├── docs/                     # Medical PDF documents
│
├── app.py                    # Streamlit UI & chatbot
├── build_database.py         # Build vector database
├── embedding.py              # PDF processing & embeddings
├── vector_store.py           # Semantic search
├── prompts.py                # Prompt template
├── rag.py                    # RAG pipeline
│
├── vector_store.pkl          # Saved vector database
├── requirements.txt
├── .gitignore
├── LICENSE
├── .env
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Mediora-ai.git

cd Mediora-ai
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv env

env\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv env

source env/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure API Key

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
GEMINI_GEN_MODEL=gemini-2.5-flash
```

---

# 📚 Add Medical Documents

Place your medical PDF files inside the `docs` folder.

Example:

```text
docs/
├── Diabetes.pdf
├── Dengue.pdf
├── Asthma.pdf
├── Hypertension.pdf
├── First_aid.pdf
└── Nutrition and Health.pdf
```

---

# 🧠 Build the Knowledge Base

Run the following command:

```bash
python build_database.py
```

This process:

- Reads all medical PDF documents
- Extracts text
- Splits documents into smaller chunks
- Generates embeddings using Sentence Transformers
- Stores embeddings in `vector_store.pkl`

---

# 🚀 Run the Application

Start the Streamlit application.

```bash
streamlit run app.py
```

---

# 💬 Example Questions

Try asking questions like:

- What is dengue?
- What are the symptoms of diabetes?
- What causes asthma?
- How can hypertension be prevented?
- What should I do for burns?
- What foods are good for heart health?
- How can I maintain a balanced diet?
- What are the symptoms of high blood pressure?

---

# 🔄 How It Works

1. The user enters a medical question.
2. The question is converted into a vector embedding using Sentence Transformers.
3. The embedding is compared against the vector database using cosine similarity.
4. The most relevant medical document chunks are retrieved.
5. Retrieved context and the user's question are combined into a prompt.
6. The prompt is sent to Google Gemini AI.
7. Gemini generates a context-aware response.
8. If Gemini is unavailable (API quota exceeded or server busy), Mediora AI automatically displays the retrieved information from the medical knowledge base.
9. The answer is shown in the Streamlit chatbot interface.

---

---

# 🚀 Future Improvements

- 🎤 Voice input
- 🔊 Voice responses
- 🌍 Multi-language support
- 📱 Mobile-friendly interface
- 📄 Export conversation history
- 👨‍⚕️ Doctor mode
- 📊 Medical analytics dashboard
- ☁️ Cloud deployment
- 🖼️ Medical image understanding
- 🧠 Fine-tuned medical language model

---

# 🎯 Use Cases

- 👨‍🎓 Medical Students
- 👩‍⚕️ Healthcare Professionals
- 🔬 Researchers
- 🏫 Academic Institutions
- 📚 Medical Libraries
- 📖 Educational Learning

---

# ⚠️ Disclaimer

Mediora AI is designed for **educational and informational purposes only**.

It should **not** be used as a replacement for professional medical advice, diagnosis, or treatment.

Always consult a qualified healthcare professional for medical concerns or emergencies.

---

# 👩‍💻 Author

**Sneha Jana** &
**Sneha Singha**

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

# 🙏 Acknowledgements

- Google Gemini API
- Sentence Transformers
- Hugging Face
- Streamlit
- Python Open Source Community

---

# ⭐ Support

If you found this project helpful, please consider giving it a **⭐ Star** on GitHub.

It helps others discover the project and motivates future improvements.
