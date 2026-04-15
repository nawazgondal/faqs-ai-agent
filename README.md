# FAQS AI Agent

![FAQS AI Agent](thumbnail.svg)

**A production-ready semantic search FAQ chatbot with FastAPI backend, Angular frontend, and Ollama/Mistral LLM integration.**

---
## Use Cases
- Customer support chatbot
- Website FAQ assistant
- Internal knowledge base chatbot
- Documentation assistant

## 🎯 Quick Start

```bash
# Terminal 1: Ollama
ollama serve

# Terminal 2: Backend
cd backend && pip install -r requirements.txt && python main.py

# Terminal 3: Frontend
cd frontend && npm install && npm start

# Open http://localhost:4200
```

## ✨ Features

- 🧠 **Semantic Search** - Understands meaning, not just keywords
- ⚡ **Lightning Fast** - <1ms FAISS vector search
- 🤖 **AI Powered** - Mistral LLM for intelligent responses
- 🎨 **Beautiful UI** - Modern gradient design, fully responsive
- 🔒 **Offline** - No cloud required, local processing only
- 📚 **Well Documented** - 3000+ lines of comprehensive guides
- 🚀 **Production Ready** - Error handling, logging, validation

## 🏗️ Architecture

```
User Question
    ↓
Convert to Vector (384-D embedding)
    ↓
Search FAISS Index (top-3 FAQs)
    ↓
Get FAQ Context
    ↓
Send to Mistral LLM
    ↓
Display Answer + Related FAQs
```

## 📦 What's Included

✅ **Backend**: FastAPI server with vector search & LLM  
✅ **Frontend**: Angular chat interface  
✅ **Documentation**: 12 comprehensive guides  
✅ **Configuration**: All configs ready  
✅ **Sample Data**: FAQ database included  
✅ **Scripts**: Quick start scripts  

## 📚 Documentation

| Guide | Purpose | Time |
|-------|---------|------|
| [00_READ_ME_FIRST.md](00_READ_ME_FIRST.md) | Start here | 5 min |
| [START_HERE.md](START_HERE.md) | Overview | 5 min |
| [QUICK_REFERENCE.md](QUICK_REFERENCE.md) | Commands | 5 min |
| [SETUP.md](SETUP.md) | Installation | 20 min |
| [ARCHITECTURE.md](ARCHITECTURE.md) | How it works | 15 min |
| [FAQ_MANAGEMENT.md](FAQ_MANAGEMENT.md) | Managing FAQs | 15 min |

## 🚀 Technology Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| API | FastAPI | 0.104.1 |
| Embeddings | SentenceTransformer | 2.2.2 |
| Vector DB | FAISS | 1.7.4 |
| LLM | Ollama + Mistral | Latest |
| Frontend | Angular | 17.0.0 |
| Language | TypeScript | 5.2.0 |

## 📊 Project Stats

- **31 Files** created
- **3500+ Lines** of code
- **3000+ Lines** of documentation
- **12 Guides** included
- **5 API Endpoints**
- **Production Ready** ✅

## 🎓 What You'll Learn

✅ FastAPI development  
✅ Angular framework  
✅ Semantic search  
✅ Vector embeddings  
✅ LLM integration  
✅ Full-stack development  
✅ Production best practices  

## 🆘 Need Help?

- **Quick start**: [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
- **Installation**: [SETUP.md](SETUP.md)
- **How it works**: [ARCHITECTURE.md](ARCHITECTURE.md)
- **All guides**: [INDEX.md](INDEX.md)

---

## 📄 License

MIT

---

**Version**: 1.0.0  
**Status**: ✅ Production Ready  
**Last Updated**: April 15, 2026
