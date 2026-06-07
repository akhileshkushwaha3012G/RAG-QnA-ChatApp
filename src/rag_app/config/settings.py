from pydantic_settings import BaseSettings
from dotenv import load_dotenv

class Settings(BaseSettings):
    #GROQ_API_KEY: str = ""
    CHROMA_DB_DIR: str = "data/chroma"
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"
    GEN_AI_MODEL: str = "openai/gpt-oss-safeguard-20b"
    CHUNK_SIZE: int = 50
    SYSTEM_PROMPT: str = """You are a spritual guide who has depth understanding of the subject Bhagvat gita and able to explain the meaning with analogy to everyday life to anyone of age of 7 or older as per their occupation, work and situation.
                    Answer the user's question positively using ONLY the context provided below and based on user prompt. If the context does not contain enough information, say so — do not make things up and keep the answer concise and to the point and related to Bhagvat Gita
                    """
    class Config:
        env_file = ".env"


settings = Settings()
load_dotenv()  # Load environment variables from .env file