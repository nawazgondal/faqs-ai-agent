# Quick Reference Card

## 🚀 30-Second Quick Start

### Prerequisites: Python 3.9+, Node.js 18+, Ollama
```bash
ollama pull mistral  # Download Mistral model
```

### Terminal 1 - Start Ollama
```bash
ollama serve
```

### Terminal 2 - Start Backend
```bash
cd backend
pip install -r requirements.txt
python main.py
```

### Terminal 3 - Start Frontend
```bash
cd frontend
npm install
npm start
```

### Open Browser
```
http://localhost:4200
```

---

## 📍 Important URLs

| Service | URL | Purpose |
|---------|-----|---------|
| Frontend | http://localhost:4200 | Chat UI |
| Backend | http://localhost:8000 | API server |
| API Docs | http://localhost:8000/docs | Swagger |
| Health | http://localhost:8000/health | Status check |

---

## 🔌 API Endpoints

### Query FAQs
```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question":"What is AI?"}'
```

### Health Check
```bash
curl http://localhost:8000/health
```

### System Info
```bash
curl http://localhost:8000/info
```

---

## 📝 File Locations

| Component | Path | Purpose |
|-----------|------|---------|
| FAQ Data | `backend/faqs.json` | Add/edit FAQs here |
| Backend Logic | `backend/main.py` | API endpoints |
| Frontend UI | `frontend/src/app/` | Chat interface |
| API Service | `frontend/src/app/services/faq.service.ts` | Backend calls |

---

## 🎯 Common Tasks

### Add FAQs
1. Edit `backend/faqs.json`
2. Restart backend: `python main.py`

### Change LLM Model
In `backend/main.py` line 58:
```python
model='neural-chat'  # Change 'mistral' to another model
```
Available: `ollama list`

### Customize UI
Edit `frontend/src/app/app.component.css` for styles
Edit `frontend/src/app/app.component.html` for layout

### Change Backend URL
In `frontend/src/app/services/faq.service.ts` line 9:
```typescript
private apiUrl = 'http://localhost:8000';
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| "ModuleNotFoundError" | `pip install -r requirements.txt` |
| "Cannot connect to Ollama" | Start: `ollama serve` |
| "Model not found: mistral" | Run: `ollama pull mistral` |
| "Port 4200 in use" | `ng serve --port 4300` |
| "CORS error" | Backend should have CORS enabled |

---

## 📊 How It Works (Simple)

```
1. You ask: "What is AI?"
    ↓
2. Frontend sends to Backend
    ↓
3. Backend finds similar FAQs (Semantic Search)
    ↓
4. Uses FAQ answers as context for LLM
    ↓
5. Mistral generates smart response
    ↓
6. Shows answer + related FAQs
```

---

## 💡 Pro Tips

1. **First query is slow** - Model loading, ~5-10 seconds. Subsequent queries: 2-5 seconds
2. **Use smaller models** for faster responses: `ollama pull orca-mini`
3. **Monitor memory** - Ollama uses 2-4GB RAM
4. **Customize FAQs** - More/better FAQs = better responses
5. **Check logs** - Terminal shows detailed processing steps

---

## 🔄 Typical Development Workflow

```bash
# Window 1: Start services
ollama serve

# Window 2
cd backend && python main.py

# Window 3
cd frontend && npm start

# Edit files and see changes:
# - Backend: Restart python main.py
# - Frontend: Auto-reload on file change
# - FAQs: Restart python main.py

# Build for production
npm run build  # Frontend dist/ ready to deploy
```

---

## 📦 Deployment Quick Links

| Platform | Command |
|----------|---------|
| Docker (Backend) | `docker build -t faq-backend . && docker run -p 8000:8000 faq-backend` |
| Firebase (Frontend) | `npm run build && firebase deploy` |
| GitHub Pages | `npm run build && git push` |

---

## 🔐 Security Checklist

- [ ] CORS configured for your domain (not `*` in production)
- [ ] Input validation enabled (Pydantic)
- [ ] Error messages don't leak system details
- [ ] Rate limiting added (optional)
- [ ] Authentication implemented (optional)
- [ ] Ollama not exposed to internet

---

## 📚 Documentation Map

| Document | What's Inside |
|----------|---------------|
| README.md | Complete overview |
| SETUP.md | Installation steps |
| ARCHITECTURE.md | Technical design |
| FAQ_MANAGEMENT.md | FAQ updates |
| FILES.md | File structure |
| This file | Quick reference |

---

## 🎓 Key Concepts

- **Semantic Search**: Finding meaning-based matches, not keyword matches
- **Embeddings**: Converting text to numerical vectors
- **FAISS**: Fast similarity search tool
- **LLM**: Large Language Model (Mistral in this case)
- **Ollama**: Local LLM server
- **SentenceTransformer**: Model that converts sentences to embeddings

---

## ⏱️ Performance Targets

| Operation | Time |
|-----------|------|
| Embedding | 50-100ms |
| Search | <1ms |
| LLM Response | 2-5s |
| Total | 3-6s |

---

## ✅ Verification Checklist

After setup, verify:
- [ ] Backend running: `curl http://localhost:8000/`
- [ ] Frontend running: Visit `http://localhost:4200`
- [ ] Ollama running: `ollama list` shows mistral
- [ ] FAQs loaded: Frontend loads without errors
- [ ] Query works: Ask "What is AI?" and get response
- [ ] Related FAQs show: See FAQ cards in response

---

## 🆘 Emergency Help

**System won't start?**
1. Check all terminals for error messages
2. Verify prerequisites installed
3. Check ports: 8000, 4200, Ollama default
4. Read SETUP.md troubleshooting section

**Responses are slow?**
1. First query is always slower
2. Check Ollama is running
3. Monitor system resources
4. Consider smaller LLM model

**Frontend not connecting?**
1. Verify backend running on :8000
2. Check faq.service.ts URL
3. Open browser console for errors
4. Check CORS is enabled

---

**Happy Building! 🚀🤖**
