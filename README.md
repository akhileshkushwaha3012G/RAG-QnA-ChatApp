# rag-chromadb

RAG application scaffold using ChromaDB for vector storage and SentenceTransformer for embeddings.

Quick start

```bash
# create & activate venv
python3 -m venv .venv
source .venv/bin/activate

# (one-time) install UV package manager
python -m pip install --upgrade pip
python -m pip install uv

# manage & lock dependencies with UV (recommended for reproducible installs)
uv build        # resolve deps from pyproject.toml
uv lock          # write uv.lock
uv install --locked   # install exactly the locked graph (CI / reproducible installs)

pip freeze > requirements.txt # generate requirement.txt

# OR install with pip from a pinned requirements file (simple environments / Docker)
pip install -r requirements.txt

# optional: editable install for local development
pip install -e .

# ingest your data (place source files under data/raw)
python scripts/ingest_documents.py --data-dir data/raw --db-dir data/chroma

# GeetaUpdeshForKidsRAGChat

GeetaUpdeshForKidsRAGChat is an educational, child-friendly Retrieval-Augmented Generation (RAG) application that uses short, age-appropriate teachings inspired by the Bhagavad Gita to help children think through everyday feelings and choices.

Key goals
- Help children relate classical teachings to simple, practical actions in daily life (school, friendships, family, homework).
- Offer supportive language and small, actionable steps for feelings like sadness, anger, confusion, or lack of motivation.
- Encourage reflection, simple habits (breathing, mini-routines), and asking trusted adults for help when needed.

How it works (high level)
1. Ingest: curated, kid-appropriate source texts are stored under `data/raw/`.
2. Chunk & embed: text is split into small chunks, embedded with `sentence-transformers`, and stored in ChromaDB for semantic search.
3. Retrieve & generate: when a child asks a question, the system searches for the most relevant chunks and uses a lightweight generation model to produce a concise, supportive answer grounded in the source material.

How this helps children
- Translates lessons into relatable suggestions: e.g., breaking big tasks into five-minute steps, breathing exercises, or asking a teacher for help.
- Uses stories and analogies children understand to explain why certain actions help (motivation, resilience, emotional regulation).
- Avoids giving professional, medical, or legal advice — when appropriate, the app suggests talking to a trusted adult or a professional.

Kid-facing examples
- Child: "I'm scared about a test."  → App: "Try studying one small part for 10 minutes, then take a break. Small steps help build confidence."
- Child: "My friend ignored me and I feel sad." → App: "It's okay to feel sad. Try telling your friend how you felt calmly, or talk to an adult you trust about it." 
- Child: "I get angry with my sibling." → App: "When you notice anger, try counting to five and breathing slowly. Then talk about how you felt." 

How kids can use the app
1. Open the interactive CLI or app UI and ask naturally: e.g., "What should I do if I'm sad?" or "How do I stop worrying about a test?"
2. Read the short advice and try a suggested small action (breathing, a 5-minute task, asking for help).
3. Ask follow-up questions like "Can you give a story about that?" or "What's one thing I can try now?"

Developer quick start

```bash
# create & activate venv
python3 -m venv .venv
source .venv/bin/activate

# install runtime dependencies and the package
pip install -r requirements.txt
pip install -e .

# ingest curated content into the vector DB
python scripts/ingest_documents.py --data-dir data/raw --db-dir data/chroma

# interactive query
python -m rag_app.cli --data-dir data/raw --db-dir data/chroma
```

Notes:
- If you prefer not to perform an editable install, run the CLI with `PYTHONPATH=src` so the local package is importable, for example:
	- `PYTHONPATH=src python -m rag_app.cli --data-dir data/raw --db-dir data/chroma`
- The service requires an LLM API key for generation (set `GROQ_API_KEY`):
	- `export GROQ_API_KEY="your_key_here"`
- This project requires Python >=3.12 as declared in `pyproject.toml`.

Notes for maintainers
- Keep `data/raw/` curated and age-appropriate. Add metadata where helpful (source, age-range, notes).
- Use the lockfile (`uv.lock`) or `requirements.txt` to pin reproducible dependency sets.
- Store any LLM/API keys (e.g., `GROQ_API_KEY`) in environment variables or CI secrets — never commit keys to the repo.

Privacy & safety
- The tool is intended for supportive guidance only. For mental health, safety, or crisis situations, the app will recommend talking to a trusted adult or contacting local emergency services.

Next improvements (ideas)
- Add a small web UI with kid-friendly design and read-aloud support.
- Include a curated prompt set and example responses for common child concerns in `notebooks/`.
- Add a moderation filter and parental/guardian controls for production use.

If you'd like, I can also draft kid-facing sample dialogs, sample data files for `data/raw/`, or a simple web UI prototype.
