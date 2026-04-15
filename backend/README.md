# FAQS AI Agent - Backend Configuration

This is the backend FastAPI server for the FAQ AI Agent system.

## Components

- **main.py** - FastAPI application with vector search and LLM integration
- **faqs.json** - Sample FAQ database
- **requirements.txt** - Python dependencies

## Key Features

✅ FastAPI REST API
✅ Semantic embeddings with SentenceTransformers
✅ Vector database with FAISS
✅ Ollama + Mistral LLM integration
✅ CORS enabled for frontend communication

## Running the Backend

```bash
# Install dependencies
pip install -r requirements.txt

# Ensure Ollama is running
ollama serve

# In another terminal, start the backend
python main.py
```

The API will be available at http://localhost:8000

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Architecture

The system uses a three-layer approach:

1. **Embedding Layer** - Converts FAQ questions to semantic vectors
2. **Search Layer** - FAISS finds top-3 most similar FAQs
3. **Generation Layer** - Ollama/Mistral generates contextual answers
