from rag_app.embeddings.embedding_factory import get_embedding_service
from rag_app.vectorstore.collection_manager import get_store


def retrieve(query: str, top_k: int = 5, db_dir: str = None):
    emb = get_embedding_service()
    q_vec = emb.embed_texts([query])
    store = get_store(db_dir)
    res = store.query(query_embeddings=q_vec, n_results=top_k)
    return res
