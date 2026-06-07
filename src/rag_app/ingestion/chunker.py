from typing import List
from rag_app.config.settings import settings


def parse_word_chunks(text: str, chunk_size: int = settings.CHUNK_SIZE) -> List[str]:
    """Split `text` into sequential word chunks and return list of chunk strings.

    This returns plain strings (not dicts) to simplify downstream embedding.
    """
    # Strip markdown heading symbols and blank lines
    clean_lines: List[str] = []
    for line in text.splitlines():
        line = line.strip().lstrip("#").strip()
        if line:
            clean_lines.append(line)

    # Join everything into one word list and slice
    words = " ".join(clean_lines).split()
    print(f"Started chunking...words to chunk = {len(words)}")
    chunks: List[str] = []
    if chunk_size <= 0:
        raise ValueError("chunk_size must be > 0")
    for i in range(0, len(words), chunk_size):
        content = " ".join(words[i : i + chunk_size])
        chunks.append(content)

    print(f"Total chunks: {len(chunks)}")
    return chunks

