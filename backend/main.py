from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import ollama
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="FAQS AI Agent",
    description="A complete FAQ chatbot using FastAPI, Ollama/Mistral LLM, semantic search, and FAISS vector database",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (configure for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variables for FAQ data and models
faqs = []
model = None
index = None

def initialize_system():
    """Initialize FAQ data and AI models"""
    global faqs, model, index
    
    try:
        logger.info("Initializing FAQS AI Agent...")
        
        # Load FAQs
        logger.info("Loading FAQs from file...")
        with open("faqs.json", "r") as f:
            faqs = json.load(f)
        logger.info(f"✓ Loaded {len(faqs)} FAQs")
        
        # Initialize sentence transformer for embeddings
        logger.info("Loading SentenceTransformer model...")
        model = SentenceTransformer('all-MiniLM-L6-v2')
        logger.info("✓ SentenceTransformer loaded")
        
        # Prepare embeddings
        logger.info("Generating embeddings for FAQs...")
        questions = [faq["question"] for faq in faqs]
        embeddings = model.encode(questions)
        embeddings = np.array(embeddings).astype('float32')
        logger.info(f"✓ Generated {len(embeddings)} embeddings")
        
        # Create FAISS index
        logger.info("Building FAISS vector index...")
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatIP(dimension)
        faiss.normalize_L2(embeddings)
        index.add(embeddings)
        logger.info(f"✓ FAISS index created with {index.ntotal} vectors")
        
        logger.info("✓ System initialized successfully!")
        
    except Exception as e:
        logger.error(f"✗ Initialization failed: {str(e)}")
        raise

# Initialize on startup
try:
    initialize_system()
except Exception as e:
    logger.error("Failed to initialize system on startup. Continuing anyway...")
    faqs = []
    model = None
    index = None

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    relevant_faqs: list
    search_scores: list = None

@app.post("/query", response_model=QueryResponse)
async def query_faqs(request: QueryRequest):
    """
    Query the FAQ system with semantic search and LLM-based response generation.
    
    - **question**: The user's question
    
    Returns:
    - **answer**: AI-generated answer based on relevant FAQs
    - **relevant_faqs**: Top 3 most relevant FAQ items found
    - **search_scores**: Similarity scores for each FAQ
    """
    try:
        if not request.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")
        
        logger.info(f"Processing query: {request.question[:100]}...")
        
        # Validate system is initialized
        if model is None or index is None or not faqs:
            raise HTTPException(status_code=500, detail="System not properly initialized. Check FAQ data and models.")
        
        # Step 1: Embed the query using SentenceTransformer
        logger.info("Step 1: Generating query embedding...")
        query_embedding = model.encode([request.question])
        query_embedding = np.array(query_embedding).astype('float32')
        faiss.normalize_L2(query_embedding)
        
        # Step 2: Search for top-3 similar questions in FAISS index
        logger.info("Step 2: Searching FAISS index for similar FAQs...")
        k = 3
        distances, indices = index.search(query_embedding, k)
        
        # Step 3: Get relevant FAQs with similarity scores
        logger.info("Step 3: Retrieving relevant FAQ details...")
        relevant_faqs = []
        search_scores = []
        for idx, distance in zip(indices[0], distances[0]):
            if idx < len(faqs):
                relevant_faqs.append(faqs[int(idx)])
                search_scores.append(float(distance))
        
        logger.info(f"Found {len(relevant_faqs)} relevant FAQs")
        
        # Step 4: Prepare context for LLM
        logger.info("Step 4: Building LLM prompt context...")
        context = "\n".join([f"Q: {faq['question']}\nA: {faq['answer']}" for faq in relevant_faqs])
        
        # Step 5: Generate response using Ollama/Mistral
        logger.info("Step 5: Generating AI response using Ollama/Mistral...")
        prompt = f"""Based on the following FAQ knowledge base:

{context}

User Question: {request.question}

Provide a helpful, informative response based on the FAQs above. If the FAQs contain relevant information, use it to create a comprehensive answer. Be friendly and clear."""
        
        try:
            response = ollama.chat(
                model='mistral',
                messages=[{'role': 'user', 'content': prompt}],
                stream=False
            )
            answer = response['message']['content']
        except Exception as ollama_error:
            logger.error(f"Ollama error: {str(ollama_error)}")
            # Fallback: Return relevant FAQ answers if LLM fails
            answer = f"I found relevant information: {relevant_faqs[0]['answer'] if relevant_faqs else 'Unable to generate response.'}"
        
        logger.info("✓ Query processed successfully")
        
        return {
            "answer": answer,
            "relevant_faqs": relevant_faqs,
            "search_scores": search_scores
        }

    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "FAQS AI Agent Backend",
        "status": "running",
        "faqs_loaded": len(faqs),
        "model_initialized": model is not None,
        "index_ready": index is not None
    }

@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy" if faqs and model and index else "not_ready",
        "faq_count": len(faqs),
        "model": "SentenceTransformer (all-MiniLM-L6-v2)" if model else None,
        "index": "FAISS IndexFlatIP" if index else None,
        "faiss_vector_count": index.ntotal if index else 0
    }

@app.get("/info")
async def info():
    """System information"""
    return {
        "name": "FAQS AI Agent",
        "version": "1.0.0",
        "description": "A complete FAQ chatbot using FastAPI, Ollama/Mistral LLM, semantic search, and FAISS vector database",
        "components": {
            "api": "FastAPI",
            "embedding_model": "SentenceTransformer (all-MiniLM-L6-v2)",
            "vector_db": "FAISS",
            "llm": "Ollama with Mistral"
        },
        "endpoints": {
            "query": "POST /query - Query FAQs",
            "health": "GET /health - Health check",
            "info": "GET /info - System information",
            "docs": "GET /docs - Swagger documentation"
        }
    }

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting FAQS AI Agent Backend...")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")