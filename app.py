import streamlit as st
from modules.vector_store import load_vector_db
from modules.rag_generator import generate_answer

vector_db = load_vector_db()

st.title("College Student Knowledge Assistant")

question = st.text_input("Ask your question")

if question:

    docs = vector_db.similarity_search(question, k=3)

    answer, sources = generate_answer(question, docs)

    st.subheader("Answer")

    st.write(answer)

    st.subheader("Sources")

    for s in sources:
        st.write(s)