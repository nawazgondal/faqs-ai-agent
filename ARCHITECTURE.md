# Architecture & System Design

## 🏛️ High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERFACE                           │
│                   (Angular Frontend)                        │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Chat Window                                       │    │
│  │  ┌──────────────────────────────────────────┐     │    │
│  │  │ Bot: AI generated response               │     │    │
│  │  │ Related FAQs: [Q1] [Q2] [Q3]             │     │    │
│  │  └──────────────────────────────────────────┘     │    │
│  │                                                    │    │
│  │  Input: [User Question] [Send]                    │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                          ↓ HTTP POST /query
                          ↑ JSON Response
┌─────────────────────────────────────────────────────────────┐
│                   API LAYER                                 │
│              (FastAPI Backend Server)                       │
│  ┌────────────────────────────────────────────────────┐    │
│  │ POST /query: {"question": "What is AI?"}           │    │
│  │ GET /: Health check                               │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│              SEMANTIC SEARCH PIPELINE                       │
│  ┌────────────────────────────────────────────────────┐    │
│  │  1. Embedding Generation                          │    │
│  │     Input: "What is AI?"                          │    │
│  │     Model: SentenceTransformer (all-MiniLM-L6-v2)│    │
│  │     Output: 384-dim vector                        │    │
│  └────────────────────────────────────────────────────┘    │
│                          ↓                                  │
│  ┌────────────────────────────────────────────────────┐    │
│  │  2. Vector Search (FAISS)                         │    │
│  │     Query Vector + FAQ Vectors                    │    │
│  │     Similarity: Inner Product (Cosine)            │    │
│  │     Output: Top-3 Most Similar FAQs               │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                LLM GENERATION LAYER                         │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Prompt Engineering:                              │    │
│  │  ┌─────────────────────────────────────────┐      │    │
│  │  │ Context: [Top-3 FAQ Q&A]               │      │    │
│  │  │ Query: "What is AI?"                   │      │    │
│  │  │ Instruction: Generate helpful response│      │    │
│  │  └─────────────────────────────────────────┘      │    │
│  │                    ↓                              │    │
│  │  Ollama/Mistral Model                            │    │
│  │  Output: Natural language answer                 │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                  RESPONSE ASSEMBLY                          │
│  {                                                          │
│    "answer": "AI is artificial intelligence...",           │
│    "relevant_faqs": [                                       │
│      {"question": "What is AI?", "answer": "..."},         │
│      {"question": "Benefits of AI?", "answer": "..."}      │
│    ]                                                        │
│  }                                                          │
└─────────────────────────────────────────────────────────────┘
```

## 🔄 Data Flow Diagram

```
User Question
    │
    ├─→ [FastAPI Endpoint] → Validate Input
    │
    ├─→ [SentenceTransformer] → Generate 384-D Embedding
    │
    ├─→ [FAISS Index] → Find Top-3 Similar FAQs
    │      │
    │      └─→ [FAQ Database] → Retrieve Answer Texts
    │
    ├─→ [Prompt Builder] → Create Context + Query
    │
    ├─→ [Ollama/Mistral] → Generate Response
    │
    ├─→ [Response Builder] → Package Answer + Related FAQs
    │
    └─→ [HTTP Response] → Send to Frontend
        │
        └─→ [Angular] → Render in Chat UI
```

## 💾 Data Structure

### FAQ Item (JSON)
```json
{
  "question": "What is artificial intelligence?",
  "answer": "AI is the simulation of human intelligence in machines..."
}
```

### Embedding Vector
```
[0.123, -0.456, 0.789, ..., 0.321]  // 384 dimensions
```

### FAISS Index
```
IndexFlatIP(dimension=384)
    ↓
[FAQ1 embedding, FAQ2 embedding, FAQ3 embedding, ...]
    ↓
Cosine similarity search
```

### API Request/Response

**Request:**
```json
{
  "question": "How does machine learning work?"
}
```

**Response:**
```json
{
  "answer": "Machine learning works by training algorithms on data to discover patterns and make predictions without being explicitly programmed for each scenario...",
  "relevant_faqs": [
    {
      "question": "How does machine learning work?",
      "answer": "Machine learning works by training algorithms on data..."
    },
    {
      "question": "What is AI?",
      "answer": "AI stands for Artificial Intelligence..."
    }
  ]
}
```

## 🔧 Component Architecture

### Backend Components

```
FastAPI App
├── Route: POST /query
│   └── Handler: async query_faqs()
│       ├── Input Validation (Pydantic)
│       ├── Query Embedding (SentenceTransformer)
│       ├── Vector Search (FAISS)
│       ├── LLM Prompt Building
│       ├── LLM Inference (Ollama)
│       └── Response Assembly
├── Route: GET /
│   └── Health Check
└── Configuration
    ├── Model Loading
    ├── Embedding Generation
    └── FAISS Index Building
```

### Frontend Components

```
Angular App
├── AppComponent (Standalone)
│   ├── Template (app.component.html)
│   │   ├── Title
│   │   ├── Chat Window
│   │   │   ├── Messages Display
│   │   │   ├── Message (User Type)
│   │   │   ├── Message (Bot Type)
│   │   │   └── Related FAQs Card
│   │   └── Input Area
│   │       ├── Input Field
│   │       └── Send Button
│   │
│   ├── Component Logic (app.component.ts)
│   │   ├── Messages Array
│   │   ├── Loading State
│   │   ├── sendQuestion() Method
│   │   └── Error Handling
│   │
│   ├── Styles (app.component.css)
│   │   ├── Gradients
│   │   ├── Chat Bubbles
│   │   └── Responsive Layout
│   │
│   └── Services (Dependency Injection)
│       └── FaqService
│           └── queryFaq() → HTTP POST to Backend
```

## 🚀 Performance Characteristics

| Operation | Time | Notes |
|-----------|------|-------|
| Query Embedding | 50-100ms | SentenceTransformer inference |
| FAISS Search | <1ms | In-memory vector search |
| LLM Inference | 2-5 seconds | Ollama + Mistral (first call slower) |
| HTTP Overhead | 100-200ms | Network latency |
| **Total** | **3-6 seconds** | Per user query |

## 📊 Scalability Considerations

### Current Setup (Single Machine)
- FAQ Database: Up to 10,000 FAQs (FAISS handles this easily)
- Concurrent Users: 1-5 (single backend instance)
- Memory Usage: ~2-4GB (Ollama + embeddings)
- GPU: Auto-detected and used by Ollama

### Production Scaling

**Option 1: Multiple Backend Instances**
```
Load Balancer
├── Backend Instance 1
├── Backend Instance 2
└── Backend Instance 3
    ↓
Shared FAQ Database (JSON/DB)
```

**Option 2: Dedicated LLM Server**
```
Frontend → FastAPI Backend → Ollama Server (Different Machine)
```

**Option 3: Cloud Deployment**
- FastAPI → AWS/GCP/Azure
- FAISS → Redis/Elasticsearch
- Ollama → GPU instance or OpenAI API

## 🔐 Security Architecture

```
User Input
    ↓
[Input Validation] - Sanitize query
    ↓
[Rate Limiting] - Prevent abuse
    ↓
[Authentication] - (Optional) Verify user
    ↓
[Processing]
    ↓
[Response] - Only answer data, no system prompts
```

### Security Best Practices

1. **Input Validation**: Pydantic models with constraints
2. **Error Handling**: Generic error messages (no internal details)
3. **CORS Configuration**: Restrict to trusted domains
4. **Rate Limiting**: (Can be added) - Prevent DDoS
5. **Logging**: Monitor queries for abuse patterns

---

## 📝 Integration Points

### How to Add Authentication

```python
# In main.py
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer

security = HTTPBearer()

@app.post("/query")
async def query_faqs(request: QueryRequest, credentials = Depends(security)):
    # Verify token
    return response
```

### How to Add Database Backend

```python
# Replace JSON with database
import sqlite3
conn = sqlite3.connect('faqs.db')
faqs = conn.execute("SELECT * FROM faqs").fetchall()
```

### How to Add Conversation Memory

```python
# Store conversation history
conversations = {}

@app.post("/query")
async def query_faqs(request: QueryRequest, session_id: str):
    # Retrieve conversation history
    history = conversations.get(session_id, [])
    # Use history for context-aware responses
```

---

This architecture is designed to be simple yet powerful, suitable for learning and production use cases.
