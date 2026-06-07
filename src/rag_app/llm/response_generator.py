from .prompt_templates import build_prompt
from .llm_client import call_groq


def generate_answer(query: str, contexts: list[str]) -> str:
    prompt = build_prompt(query, contexts)
    return call_groq(prompt)
