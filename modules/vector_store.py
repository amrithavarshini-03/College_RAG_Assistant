from langchain_community.vectorstores import Chroma
from modules.embeddings import get_embedding_model

DB_PATH = "db"

def create_vector_db(chunks):

    embedding = get_embedding_model()

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory=DB_PATH
    )

    vector_db.persist()

    return vector_db


def load_vector_db():

    embedding = get_embedding_model()

    vector_db = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding
    )

    return vector_db