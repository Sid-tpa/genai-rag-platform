from fastapi import FastAPI
from app.api import ingest, query
app = FastAPI(title="GenAI RAG Platform", version="1.0.0")
app.include_router(ingest.router, prefix="/api/v1", tags=["ingest"])
app.include_router(query.router, prefix="/api/v1", tags=["query"])
@app.get("/api/v1/health")
def health():
    return {"status": "ok", "version": "1.0.0", "mongodb": "connected", "redis": "connected"}
