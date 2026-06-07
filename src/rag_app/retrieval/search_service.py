from .retriever import retrieve


def search(query: str, top_k: int = 5, db_dir: str = None):
    return retrieve(query, top_k=top_k, db_dir=db_dir)
