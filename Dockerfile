FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies needed by some Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency lists first to leverage Docker cache
COPY requirements.txt pyproject.toml ./

RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy source
COPY . /app

# Default envs (override at runtime via -e or cloud provider settings)
ENV GROQ_API_KEY=""

EXPOSE 8000

CMD ["uvicorn", "rag_app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
