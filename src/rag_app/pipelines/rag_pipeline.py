import getpass
import os
from rag_app.retrieval.search_service import search
from rag_app.llm.response_generator import generate_answer



def run_rag(query: str, db_dir: str | None = None, top_k: int = 5):
    if "GROQ_API_KEY" not in os.environ:
        os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")
    res = search(query, top_k=top_k, db_dir=db_dir)
    # Chroma query results format adaptation may be needed - placeholder
    # Try to collect document texts from results
    contexts = []
    try:
        for r in res.get("results", []) or []:
            # adapt to collection.query response structure
            contexts.append(r.get("documents", [])[0])
    except Exception:
        # fallback if result is a dict
        if isinstance(res, dict) and res.get("documents"):
            contexts = res.get("documents")
    return generate_answer(query, contexts)
