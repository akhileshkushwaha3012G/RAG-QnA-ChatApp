"""CLI for rag_app"""
import argparse
from rag_app.pipelines.indexing_pipeline import embeding_pipeline
from rag_app.pipelines.rag_pipeline import run_rag


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default="data/raw")
    parser.add_argument("--db-dir", default="data/chroma")
    args = parser.parse_args()

    embeding_pipeline(args.data_dir, args.db_dir)

    while True:
        try:
            q = input("Enter your question (or `exit`): ")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break
        if not q or q.strip().lower() in ("exit", "quit"):
            break
        resp = run_rag(q, args.db_dir)
        print("\nAnswer:\n", resp)


if __name__ == "__main__":
    main()
