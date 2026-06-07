from fastapi import FastAPI
from rag_app.pipelines.rag_pipeline import run_rag

app = FastAPI(title="rag-chromadb")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/query")
def query(q: str):
    return {"answer": run_rag(q)}
