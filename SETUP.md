# FAQS AI Agent - Complete Setup Guide

## 📋 System Overview

This is a production-ready FAQ chatbot system with:
- **Backend:** FastAPI + Ollama/Mistral LLM + FAISS vector search
- **Frontend:** Angular standalone components with modern UI
- **AI:** Semantic search + LLM-based answer generation

## 🔧 Prerequisites Installation

### Windows Setup

#### 1. Python Installation
```bash
# Download from https://www.python.org/downloads/ (3.9+)
# Or use WSL2 with Ubuntu
python --version  # Should be 3.9+
```

#### 2. Node.js Installation
```bash
# Download from https://nodejs.org/ (18+)
node --version   # Should be 18+
npm --version    # Should be 9+
```

#### 3. Ollama Installation
```bash
# Download from https://ollama.ai
# Run the installer and follow prompts
ollama --version

# Pull Mistral model (required)
ollama pull mistral

# Verify installation
ollama list  # Should show mistral
```

## 🚀 Step-by-Step Setup

### Phase 1: Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Verify Ollama is running in another terminal/window
ollama serve

# Start backend (in backend directory)
python main.py
```

**Expected output:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

**Test the backend:**
```bash
# In another terminal
curl http://localhost:8000/

# Should return:
# {"message":"FAQS AI Agent Backend"}
```

### Phase 2: Frontend Setup

```bash
# Navigate to frontend
cd frontend

# Install Node dependencies (first time only)
npm install

# Start development server
npm start
```

**Expected output:**
```
✔ Compiled successfully.
Local: http://localhost:4200/
```

### Phase 3: Test the System

1. Open http://localhost:4200 in your browser
2. Type a question: "What is AI?"
3. Wait for response (2-5 seconds)
4. View the AI response and related FAQs

## 📁 Project Structure

```
faqs-ai-agent/
│
├── backend/
│   ├── main.py                    # FastAPI server
│   ├── faqs.json                  # FAQ database (editable)
│   ├── requirements.txt           # Python packages
│   └── README.md                  # Backend docs
│
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── app.component.ts   # Main component
│   │   │   ├── app.component.html # Chat template
│   │   │   ├── app.component.css  # Styles
│   │   │   └── services/
│   │   │       └── faq.service.ts # API client
│   │   ├── main.ts                # Bootstrap
│   │   └── index.html             # Root HTML
│   ├── package.json               # npm config
│   ├── angular.json               # Angular config
│   ├── tsconfig.json              # TypeScript config
│   └── README.md                  # Frontend docs
│
├── .gitignore
└── README.md                      # This file
```

## 🎯 Using the System

### Adding More FAQs

Edit `backend/faqs.json`:

```json
[
    {
        "question": "What is machine learning?",
        "answer": "Machine learning is a subset of AI where systems learn from data."
    },
    {
        "question": "How does the chatbot work?",
        "answer": "It uses semantic search to find relevant FAQs and an LLM to generate responses."
    }
]
```

**⚠️ Important:** Restart the backend after editing FAQs!

### Changing the LLM Model

Edit `backend/main.py` (line ~58):

```python
# Change from:
response = ollama.chat(model='mistral', messages=[...])

# To:
response = ollama.chat(model='neural-chat', messages=[...])  # Other available models
```

**Available models:**
```bash
ollama list
ollama pull neural-chat  # Download new models
```

### Adjusting Search Results

Edit `backend/main.py` (line ~40):

```python
k = 3  # Top 3 results
# Change to:
k = 5  # Top 5 results
```

### Changing Frontend Port

Edit `angular.json` or run:

```bash
ng serve --port 4300
```

## 🔍 How the AI Works

### Step 1: User Sends Question
```
"What is artificial intelligence?"
```

### Step 2: Semantic Embedding
```
Question → SentenceTransformer → 384-dimensional vector
```

### Step 3: Vector Search (FAISS)
```
Find top-3 most similar FAQ questions using cosine similarity
```

### Step 4: LLM Enhancement
```
Context (FAQ answers) + Question → Ollama/Mistral → Smart response
```

### Step 5: Response Display
```
AI answer + Related FAQs shown in UI
```

## 🐛 Troubleshooting

### Backend Won't Start

**Error:** `ModuleNotFoundError: No module named 'fastapi'`
```bash
pip install -r requirements.txt
```

**Error:** `Connection refused` (when calling Ollama)
```bash
# Ensure Ollama is running in another terminal
ollama serve
```

**Error:** `Model not found: mistral`
```bash
ollama pull mistral
```

### Frontend Won't Start

**Error:** `npm ERR! code ERESOLVE`
```bash
npm install --legacy-peer-deps
```

**Error:** `Port 4200 already in use`
```bash
ng serve --port 4300
```

### API Connection Issues

**Error:** `CORS error` or `Connection refused`

Make sure:
- ✅ Backend is running (`python main.py`)
- ✅ Backend is on port 8000
- ✅ Frontend is on port 4200
- ✅ Both running on same machine OR update URL in `faq.service.ts`

### LLM Response is Slow

This is normal! Ollama running locally:
- First query: 5-10 seconds (model loading)
- Subsequent: 2-5 seconds
- For faster responses: Use smaller models like `orca-mini`

```bash
ollama pull orca-mini
# Then update model name in main.py
```

## 📊 Performance Optimization

### For Development (Quick Testing)
Use smaller model:
```bash
ollama pull orca-mini  # ~4GB
# Update in main.py to: model='orca-mini'
```

### For Production (Better Responses)
Use larger model:
```bash
ollama pull mistral   # ~7GB
ollama pull neural-chat  # ~5GB
```

### Reduce Search Results
```python
k = 2  # Only top 2 FAQs instead of 3
```

### Use GPU (if available)
Ollama automatically uses GPU. Check:
```bash
ollama ps  # Shows model and GPU usage
```

## 📝 API Testing

### Using cURL

```bash
# Test backend health
curl http://localhost:8000/

# Query FAQ
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question":"What is AI?"}'
```

### Using Python

```python
import requests

response = requests.post('http://localhost:8000/query', json={
    'question': 'What is machine learning?'
})

print(response.json())
```

### Interactive API Docs

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🚢 Deployment

### Simple Local Deployment

**Backend:**
```bash
python main.py
```

**Frontend:**
```bash
npm run build
# Deploy dist/faq-chatbot to any web server
```

### Docker Deployment (Optional)

Create `backend/Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

```bash
docker build -t faq-backend .
docker run -p 8000:8000 faq-backend
```

## 🎓 Learning Resources

- **FastAPI:** https://fastapi.tiangolo.com/
- **Angular:** https://angular.io/docs
- **Ollama:** https://ollama.ai/
- **SentenceTransformers:** https://www.sbert.net/
- **FAISS:** https://ai.facebook.com/tools/faiss/

## 📞 Support & Tips

**General Tips:**
- Keep terminal windows separate for Backend, Ollama, and Frontend
- Check terminal outputs for error messages
- First query is slower (model loading)
- Monitor RAM usage (Ollama uses 2-4GB)

**Common Issues:**
1. "Cannot POST /query" → Backend not running
2. "Cannot read property 'answer'" → Frontend connection failed
3. "Slow responses" → Normal for local LLM, use smaller model

## ✅ Checklist Before Starting

- [ ] Python 3.9+ installed
- [ ] Node.js 18+ installed
- [ ] Ollama installed and running
- [ ] Mistral model downloaded (`ollama pull mistral`)
- [ ] Requirements installed (`pip install -r requirements.txt`)
- [ ] npm packages installed (`npm install`)

## 🎉 You're Ready!

```bash
# Terminal 1: Start Ollama
ollama serve

# Terminal 2: Start Backend
cd backend
python main.py

# Terminal 3: Start Frontend
cd frontend
npm start

# Open browser: http://localhost:4200
# Type a question and chat!
```

---

**Happy Chatting! 🤖💬**

For questions or issues, check the troubleshooting section above.
