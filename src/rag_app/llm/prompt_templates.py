def build_prompt(query: str, contexts: list[str]) -> str:
    header = "You are an assistant. Use the following context to answer the question concisely."
    ctx = "\n\n".join(contexts)
    return f"{header}\n\nContext:\n{ctx}\n\nQuestion: {query}\nAnswer:" 
