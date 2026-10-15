# GenAI RAG Platform - Production Ready
Enterprise RAG platform for Financial Services.

## Architecture
[React] -> [FastAPI + JWT + API Gateway] -> [RAG Core] -> [MongoDB + Redis + FAISS]

## Features
- RAG: Chunking, Embedding, Retrieval, Reranking, Summarization
- MLOps: Fine-tuning (LoRA), Inference, CI/CD/CT
- Stack: FastAPI, MongoDB, Redis, FAISS, JWT, Docker, pytest, Jenkins ready

## Run
pip install -r requirements.txt
uvicorn app.main:app --reload
