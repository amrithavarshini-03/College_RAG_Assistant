from modules.vector_store import load_vector_db
from modules.rag_generator import generate_answer

vector_db = load_vector_db()

while True:

    query = input("\nAsk a question: ")

    docs = vector_db.similarity_search(query, k=3)

    answer, sources = generate_answer(query, docs)

    print("\nAnswer:\n", answer)

    print("\nSources:")

    for s in sources:
        print("-", s)