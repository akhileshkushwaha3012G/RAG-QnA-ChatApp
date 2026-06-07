from pathlib import Path
from typing import Iterator


SUPPORTED_EXTS = {".txt", ".md"}


def iter_files(path: Path) -> Iterator[Path]:
    for p in path.rglob("*"):
        if p.is_file() and p.suffix.lower() in SUPPORTED_EXTS:
            yield p


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")

def extract_metadata(path):
    return {"source": str(path)}
