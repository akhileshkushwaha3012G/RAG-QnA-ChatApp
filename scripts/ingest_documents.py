#!/usr/bin/env python3
"""Ingest documents into the project's vector store.

This script is a thin wrapper around `rag_app.pipelines.indexing_pipeline.embeding_pipeline`.
"""
import argparse
from pathlib import Path

from rag_app.pipelines.indexing_pipeline import embeding_pipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest documents into the vector store")
    parser.add_argument("--data-dir", default="data/raw", help="Directory with source documents")
    parser.add_argument("--db-dir", default="data/chroma", help="Directory for ChromaDB files")
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    count = embeding_pipeline(data_dir, args.db_dir)
    print(f"Ingested {count} chunks from {data_dir} into {args.db_dir}")


if __name__ == "__main__":
    main()
