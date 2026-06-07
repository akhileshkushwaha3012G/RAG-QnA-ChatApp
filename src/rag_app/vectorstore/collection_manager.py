from .chroma_store import ChromaStore


def get_store(persist_dir: str = None) -> ChromaStore:
    from rag_app.config.settings import settings

    return ChromaStore(persist_directory=persist_dir or settings.chroma_db_dir)
