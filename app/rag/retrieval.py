from app.rag.embeddings import EmbeddingService
from sentence_transformers import CrossEncoder
class RAGPipeline:
    def __init__(self):
        self.embedder = EmbeddingService()
        self.reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
    def retrieve_and_rerank(self, query: str, documents: list, top_k=5):
        query_emb = self.embedder.embed([query])[0]
        doc_embs = self.embedder.embed([d['content'] for d in documents])
        scores = [float((query_emb * d).sum()) for d in doc_embs]
        ranked = sorted(zip(documents, scores), key=lambda x: x[1], reverse=True)[:top_k*2]
        pairs = [[query, doc[0]['content']] for doc in ranked]
        rerank_scores = self.reranker.predict(pairs)
        final = sorted(zip([r[0] for r in ranked], rerank_scores), key=lambda x: x[1], reverse=True)[:top_k]
        return final
    def summarize(self, query, contexts):
        context_str = "\n".join([c[0]['content'] for c in contexts])
        return f"Based on {len(contexts)} docs: Answer to '{query}' summarized: {context_str[:500]}..."
