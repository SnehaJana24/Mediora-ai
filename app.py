import os
import joblib
import streamlit as st

from dotenv import load_dotenv
from google import genai

from vector_store import search
from prompts import SYSTEM_PROMPT

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
model = os.getenv("GEMINI_GEN_MODEL")

vector_db = joblib.load("vector_store.pkl")

st.set_page_config(
    page_title="Mediora AI",
    page_icon="🩺",
    layout="wide"
)
st.markdown("""
<style>

.main{
    background-color:#f5f9fc;
}

h1{
    color:#0B6E99;
    text-align:center;
}

.block-container{
    padding-top:2rem;
}

div[data-testid="stSidebar"]{
    background:#0B6E99;
}

div[data-testid="stSidebar"] *{
    color:white;
}

.stChatMessage{
    border-radius:15px;
    padding:10px;
    margin-bottom:10px;
    box-shadow:0 2px 10px rgba(0,0,0,.08);
}

.stButton>button{
    width:100%;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)
with st.sidebar:

    st.image(
        "https://img.icons8.com/color/96/stethoscope.png",
        width=80
    )

    st.title("Mediora AI")

    st.success("System Ready")

    st.markdown("---")

    st.subheader("Health Topics")

    st.write("🩸 Diabetes")

    st.write("🦟 Dengue")

    st.write("❤️ Hypertension")

    st.write("🫁 Asthma")

    st.write("🩹 First Aid")

    st.write("🥗 Nutrition")

    st.markdown("---")

    st.subheader("Example Questions")

    st.write("• What is Dengue?")

    st.write("• Symptoms of Diabetes")

    st.write("• First aid for burns")

    st.write("• How to prevent hypertension?")

    st.markdown("---")

    st.info("Educational Purposes Only")
st.markdown("""
<h1>🩺 Mediora AI</h1>

<h4 style="text-align:center;color:gray;">
Your Intelligent Medical Assistant
</h4>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

st.markdown("### 💬 Example Questions")

st.markdown("""
- What is dengue?
- What are the symptoms of diabetes?
- How to prevent hypertension?
- What should I do for burns?
""")
st.info(
    "👋 Welcome! Ask any health-related question. "
    "Mediora AI will provide educational information based on its medical knowledge base."
)
question = st.chat_input("Ask your medical question...")

if question:

    st.session_state.messages.append(
        {"role":"user","content":question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    results = search(question, vector_db, top_k=3)

    context = ""

    for score, text in results:
      context += f"\n[Similarity: {score:.3f}]\n{text}\n"

    prompt = SYSTEM_PROMPT.format(
      context=context,
      question=question
   )

    with st.chat_message("assistant"):

      with st.spinner("🔍 Processing your question..."):

        try:

            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            answer = response.text if response.text else "No response received from Gemini."

            st.markdown(answer)

        except Exception as e:
            print("Gemini Error:", e)
            if "503" in str(e):

                answer = "⚠️ Gemini server is currently busy. Please try again in a few seconds."

                st.warning(answer)

            elif "429" in str(e):
                answer=("⚠️ AI service is temporarily unavailable because the free API quota has been reached.")

            

                st.warning(answer)

            elif "ConnectError" in str(e):

                answer = "⚠️ Unable to connect to Gemini. Please check your internet connection."

                st.warning(answer)

            else:

                answer = f"Error: {e}"

                st.error(answer)

        st.session_state.messages.append(
           {
            "role": "assistant",
             "content": answer
            }
       )
st.markdown("---")

st.caption( 
        "This application is for educational purposes only and should not replace professional medical advice."
        )