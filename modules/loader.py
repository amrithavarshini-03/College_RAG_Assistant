import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader

def load_documents(data_path="data"):
    documents = []

    for file in os.listdir(data_path):
        file_path = os.path.join(data_path, file)

        if file.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
            documents.extend(loader.load())

        elif file.endswith(".txt"):
            loader = TextLoader(file_path)
            documents.extend(loader.load())

        elif file.endswith(".docx"):
            loader = Docx2txtLoader(file_path)
            documents.extend(loader.load())

    return documents