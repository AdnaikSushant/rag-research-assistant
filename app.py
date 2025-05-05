import streamlit as st
from retriever import retrieve_top_documents
from generator import generate_answer



st.title("🔍 Intelligent Research Assistant")

query = st.text_input("Enter your question:")

if st.button("Ask"):
    docs = retrieve_top_documents(query)
    answer = generate_answer(query, docs)
    st.write("### 📖 Answer:")
    st.write(answer)
