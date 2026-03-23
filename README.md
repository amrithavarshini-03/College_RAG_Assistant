# College Student Knowledge Assistant (RAG)

## Overview
This project is a Retrieval-Augmented Generation (RAG) system that helps students query college-related documents such as handbooks, syllabus, and policies.

## Features
- Semantic Search (Embeddings)
- Keyword Search (TF-IDF)
- Hybrid Search
- Document-based Answers with Citations
- Streamlit UI

## Tech Stack
- Python
- LangChain
- ChromaDB
- Sentence Transformers
- Ollama

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run ingestion:
python ingestion.py

3. Start app:
streamlit run app.py








#terminal 1

ollama pull phi3
ollama run phi3

#terminal 2

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python ingestion.py
python query.py
streamlit run app.py