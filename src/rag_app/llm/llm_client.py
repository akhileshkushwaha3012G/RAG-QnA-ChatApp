from groq import Groq
from rag_app.config.settings import settings

groq_client = Groq() 

def call_groq(prompt: str) -> str:
    model = getattr(settings, "GEN_AI_MODEL", None)
    system_prompt = getattr(settings, "SYSTEM_PROMPT", "")
    temperature = getattr(settings, "GROQ_TEMPERATURE", 0.6)

    response = groq_client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": prompt},
        ],
        temperature=temperature,
    )
    return response.choices[0].message.content