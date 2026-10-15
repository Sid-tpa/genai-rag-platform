from langchain.text_splitter import RecursiveCharacterTextSplitter
class RAGChunker:
    def __init__(self, chunk_size=512, overlap=50):
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap, separators=["\n\n", "\n", ".", " "])
    def chunk(self, text: str, metadata: dict = None):
        chunks = self.splitter.split_text(text)
        return [{"content": c, "metadata": metadata, "chunk_id": i} for i, c in enumerate(chunks)]
