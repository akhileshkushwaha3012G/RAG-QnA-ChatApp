# Privacy

This project is a local, developer-focused Retrieval-Augmented Generation scaffold.
By default it does not transmit or collect user data on remote servers. Notes:

- Embeddings and vector stores are persisted locally under `data/chroma/` by
  default. If you configure a remote storage backend, follow applicable privacy
  laws and obtain consent where required.
- Do not include personal, sensitive, or regulated information in the `data/raw/`
  source files used for ingestion.
- API keys (e.g., `GROQ_API_KEY`) should be stored in environment variables or
  secrets management — never commit them to the repository.

If your deployment collects or processes personal data, create a deployment
privacy notice that describes what is collected, how long it is stored, where it
is stored, and how users can request removal.
