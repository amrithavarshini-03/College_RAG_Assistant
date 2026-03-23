import ollama

def generate_answer(query, documents):

    context = "\n\n".join([doc.page_content for doc in documents])

    prompt = f"""
You are a college knowledge assistant.

Answer ONLY using the provided context.

Context:
{context}

Question:
{query}

Provide a clear answer and reference the sources.
"""

    response = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response["message"]["content"]

    sources = [doc.metadata.get("source","unknown") for doc in documents]

    return answer, sources