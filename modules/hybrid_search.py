from modules.vector_store import load_vector_db
from modules.keyword_search import KeywordSearch

class HybridSearch:

    def __init__(self, chunks):

        self.vector_db = load_vector_db()

        self.keyword = KeywordSearch(chunks)


    def search(self, query, k=3):

        semantic_results = self.vector_db.similarity_search(query, k=k)

        keyword_results = self.keyword.search(query, k=k)

        combined = semantic_results + keyword_results

        # remove duplicates
        unique = []
        seen = set()

        for doc in combined:

            text = doc.page_content

            if text not in seen:
                seen.add(text)
                unique.append(doc)

        return unique[:k]