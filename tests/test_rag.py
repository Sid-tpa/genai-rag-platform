import pytest
from app.rag.chunking import RAGChunker
from app.rag.embeddings import EmbeddingService
def test_chunking():
    chunker = RAGChunker(chunk_size=100, overlap=10)
    chunks = chunker.chunk("This is a long financial document. " * 20)
    assert len(chunks) > 1
def test_embedding():
    service = EmbeddingService()
    embs = service.embed(["test query"])
    assert len(embs[0]) == 384
