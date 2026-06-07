from typing import List

from rag_app.utils.logger import get_logger

logger = get_logger(__name__)


class EmbeddingService:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model_name = model_name
        self._model: SentenceTransformer | None = None

    def _ensure_model(self):
        if self._model is None:
            logger.info("Loading embedding model: %s", self.model_name)
            from sentence_transformers import SentenceTransformer

            self._model = SentenceTransformer(self.model_name)

    def _text_from_item(self, item) -> str:
        # Accept either a raw string or a dict containing common text keys
        if isinstance(item, str):
            return item
        if isinstance(item, dict):
            for key in ("content", "text", "body", "raw"):
                v = item.get(key)
                if isinstance(v, str):
                    return v
            raise TypeError("EmbeddingService: dict input missing text field (content/text/body/raw)")
        raise TypeError(f"EmbeddingService: unsupported item type {type(item)!r}")

    def embed_texts(self, items: list, batch_size: int = 64) -> List[List[float]]:
        """Embed a list of texts or document dicts and return list of vectors.

        Each item may be either a `str` or a `dict` containing one of the keys
        `content`, `text`, `body`, or `raw`.
        """
        if not items:
            return []

        texts: list[str] = []
        for it in items:
            texts.append(self._text_from_item(it))

        self._ensure_model()

        logger.info("Embedding %d texts (batch_size=%d)", len(texts), batch_size)
        embeddings = self._model.encode(texts, show_progress_bar=True, batch_size=batch_size)

        try:
            return embeddings.tolist()
        except Exception:
            return [list(e) for e in embeddings]
