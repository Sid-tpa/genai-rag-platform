from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
class EmbeddingService:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.dimension = 384
        self.index = faiss.IndexFlatL2(self.dimension)
    def embed(self, texts: list):
        return self.model.encode(texts, normalize_embeddings=True)
    def add_to_index(self, embeddings):
        self.index.add(np.array(embeddings).astype('float32'))
    def search(self, query_emb, top_k=5):
        D, I = self.index.search(np.array([query_emb]).astype('float32'), top_k)
        return D[0], I[0]
