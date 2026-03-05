from src.embeddings.model_loader import EmbeddingModel
from src.vector_store.faiss_manager import FAISSManager


class Retriever:

    def __init__(self, vector_db: FAISSManager):
        self.vector_db = vector_db
        self.embedding_model = EmbeddingModel()

    def retrieve(self, query: str, top_k: int = 5):

        # create embedding
        query_embedding = self.embedding_model.embed_text(query)

        # FAISS expects shape (n_queries, dim)
        query_embedding = query_embedding.reshape(1, -1)

        results = self.vector_db.search(query_embedding, top_k)

        return results