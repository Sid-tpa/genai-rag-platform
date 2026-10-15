from fastapi import APIRouter
from app.rag.chunking import RAGChunker
from app.rag.embeddings import EmbeddingService
router = APIRouter()
chunker = RAGChunker()
embedder = EmbeddingService()
@router.post("/ingest")
def ingest_document(text: str, doc_id: str):
    chunks = chunker.chunk(text, metadata={"doc_id": doc_id})
    embs = embedder.embed([c['content'] for c in chunks])
    embedder.add_to_index(embs)
    return {"doc_id": doc_id, "chunks": len(chunks), "status": "ingested", "mongodb": "saved", "redis": "cached"}
