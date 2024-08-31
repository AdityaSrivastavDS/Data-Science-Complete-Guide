import streamlit as st
from query_engine import query_documents

st.title("Content Engine Chatbot")

user_input = st.text_input("Ask a question about the documents:")

if user_input:
    response = query_documents(user_input)
    st.write(response)
