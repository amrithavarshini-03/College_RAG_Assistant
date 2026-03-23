from modules.loader import load_documents
from modules.chunker import split_documents
from modules.vector_store import create_vector_db

def run_ingestion():

    print("Loading documents...")

    docs = load_documents()

    print("Chunking documents...")

    chunks = split_documents(docs)

    print("Creating vector database...")

    create_vector_db(chunks)

    print("Ingestion completed!")


if __name__ == "__main__":

    run_ingestion()