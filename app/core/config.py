import os
class Settings:
    MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    JWT_SECRET = os.getenv("JWT_SECRET", "genesis10-secret")
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
settings = Settings()
