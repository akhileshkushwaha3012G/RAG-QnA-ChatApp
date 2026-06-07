class ChromaStore:
    def __init__(self, persist_directory: str = "data/chroma"):
        try:
            import chromadb
            from chromadb.config import Settings
        except Exception as e:
            raise RuntimeError("chromadb is required for ChromaStore; install the package or run in an environment with chromadb available") from e

        # Initialize client lazily using the installed chromadb
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection("rag_collection")

    def upsert(self, ids, embeddings, metadatas, documents):
        self.collection.upsert(ids=ids, embeddings=embeddings, metadatas=metadatas, documents=documents)

    def query(self, query_embeddings, n_results=5):
        return self.collection.query(query_embeddings=query_embeddings, n_results=n_results)
