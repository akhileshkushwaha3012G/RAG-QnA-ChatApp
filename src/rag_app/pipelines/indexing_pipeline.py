from pathlib import Path
from rag_app.ingestion.document_loader import iter_files, read_text, extract_metadata
from rag_app.ingestion.chunker import parse_word_chunks
from rag_app.embeddings.embedding_factory import get_embedding_service
from rag_app.vectorstore.collection_manager import get_store


def embeding_pipeline(data_dir: str | Path = "data/raw", db_dir: str | None = None):
    data_dir = Path(data_dir)
    emb = get_embedding_service()
    store = get_store(db_dir)
    ids = []
    documents = []
    metadatas = []
    texts = []
    idx = 0
    for p in iter_files(data_dir):
        #Read each file, extract metadata, chunk text, and prepare for embedding and storage
        txt = read_text(p)
        meta = extract_metadata(p)
        for chunk in parse_word_chunks(txt):
            ids.append(f"doc-{idx}")
            documents.append(chunk)
            metadatas.append(meta)
            texts.append(chunk)
            idx += 1
    embeddings = emb.embed_texts(texts)
    store.upsert(ids=ids, embeddings=embeddings, metadatas=metadatas, documents=documents)
    print(f"Indexed {len(ids)} chunks into the vector store of file {p} with metadata and embeddings.")
    return len(ids)
