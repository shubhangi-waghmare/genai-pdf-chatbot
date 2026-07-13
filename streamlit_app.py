import streamlit as st

from services.rag_service import get_answer
from services.pdf_service import save_uploaded_file
from vectorstore.vector_store import create_vector_db

st.set_page_config(
    page_title="GenAI PDF Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 GenAI PDF Chatbot")

st.divider()

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    save_uploaded_file(uploaded_file)

    st.success(f"{uploaded_file.name} uploaded successfully.")

    if st.button("Update Knowledge Base"):

        with st.spinner("Creating Embeddings..."):

            create_vector_db()

        st.success("Knowledge Base Updated Successfully!")

st.divider()

question = st.text_input("Ask your question")

if st.button("Get Answer"):

    if question.strip():

        with st.spinner("Thinking..."):

            answer = get_answer(question)

        st.subheader("Answer")

        st.write(answer)

    else:

        st.warning("Please enter a question.")