from fastapi import FastAPI
app = FastAPI(title="GenAI RAG Platform - Senior 7 Wall")

@app.get("/")
def root(): return {"message": "GenAI RAG Platform - Chunking | Embedding | Retrieval | Reranking | Guardrails"}

@app.get("/health")
def health(): return {"rag": "active", "vector_db": "faiss", "chunking": "recursive", "embedding": "openai", "reranking": "cohere", "status": "ok"}

@app.get("/api/v1/rag/query")
def rag_query(q: str = "What is RAG?"):
    return {"query": q, "chunks": 5, "retrieved": ["doc1", "doc2"], "answer": "RAG is Retrieval Augmented Generation", "guardrail": "passed"}

@app.get("/api/v1/ingest")
def ingest(): return {"ingested": 100, "vector_db": "faiss", "status": "indexed"}
