# GenAI RAG Platform - Production Grade
![Python](https://img.shields.io/badge/Python-3.11-3776AB) ![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688) ![MongoDB](https://img.shields.io/badge/MongoDB-4.6-47A248) ![Redis](https://img.shields.io/badge/Redis-5.0-DC382D)

> Built for Genesis10 #26-09549 - Global Financial Institution - Jersey City, NJ Hybrid

Enterprise RAG platform implementing: Chunking, Embedding, Retrieval, Reranking, Summarization + MLOps + JWT + API Gateway

## Architecture
[React/Angular] -> [FastAPI + JWT + API Gateway] -> [RAG Core] -> [MongoDB + Redis + FAISS]

## Genesis10 Requirements - 100% Covered
- RAG Process: chunking, embedding, retrieval, reranking, summarization
- FastAPI, JWT, API Gateway
- MongoDB, Redis, Angular/React, Containerization
- MLOps, Fine-tuning, Inference Frameworks
- DevOps: GIT, Jenkins, SonarQube, pytest, Artifactory, Ansible

## Quick Start (PowerShell)
pip install -r requirements.txt
uvicorn app.main:app --reload
# Docs at http://localhost:8000/docs

## Test
pytest tests/ -v
