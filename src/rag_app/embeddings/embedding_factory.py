from .embedding_service import EmbeddingService


def get_embedding_service(model_name: str = None) -> EmbeddingService:
    from rag_app.config.settings import settings

    return EmbeddingService(model_name or settings.EMBEDDING_MODEL)
