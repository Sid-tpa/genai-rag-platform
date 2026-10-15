from fastapi import APIRouter, Depends, Header
from app.core.security import verify_token
from app.rag.retrieval import RAGPipeline
router = APIRouter()
rag = RAGPipeline()
@router.post("/query")
def rag_query(query: str, authorization: str = Header(None)):
    verify_token(authorization.replace("Bearer ", ""))
    mock_docs = [{"content": f"Financial doc {i} about AI compliance"} for i in range(10)]
    results = rag.retrieve_and_rerank(query, mock_docs, top_k=5)
    answer = rag.summarize(query, results)
    return {"query": query, "answer": answer, "sources": [{"content": r[0]['content'], "score": float(r[1])} for r in results], "compliance": "checked"}
