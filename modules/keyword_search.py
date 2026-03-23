from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class KeywordSearch:

    def __init__(self, chunks):

        self.texts = [doc.page_content for doc in chunks]

        self.vectorizer = TfidfVectorizer(stop_words="english")

        self.matrix = self.vectorizer.fit_transform(self.texts)

        self.chunks = chunks


    def search(self, query, k=3):

        query_vec = self.vectorizer.transform([query])

        scores = cosine_similarity(query_vec, self.matrix).flatten()

        top_indices = scores.argsort()[-k:][::-1]

        results = [self.chunks[i] for i in top_indices]

        return results