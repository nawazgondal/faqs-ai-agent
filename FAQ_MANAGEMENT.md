# FAQ Management Guide

## 📋 FAQ Database Structure

The system uses a simple JSON file to store FAQs. Each FAQ item contains:

```json
{
    "question": "The question users might ask",
    "answer": "The answer to that question"
}
```

## ✏️ Adding FAQs

### Method 1: Direct JSON Editing (Recommended)

1. Open `backend/faqs.json` in your editor
2. Add new FAQ objects to the array:

```json
[
    {
        "question": "What is machine learning?",
        "answer": "Machine learning is a subset of AI where systems learn from data patterns without being explicitly programmed."
    },
    {
        "question": "What is deep learning?",
        "answer": "Deep learning uses neural networks with multiple layers to learn complex patterns in data."
    }
]
```

3. Save the file
4. **Restart the backend**: `python main.py`

### Method 2: Bulk Import

Create a Python script to load FAQs from another source:

```python
# import_faqs.py
import json

# Get FAQs from your source (CSV, database, etc.)
new_faqs = [
    {"question": "Q1?", "answer": "A1"},
    {"question": "Q2?", "answer": "A2"},
]

# Merge with existing
with open('faqs.json', 'r') as f:
    existing = json.load(f)

combined = existing + new_faqs

# Save
with open('faqs.json', 'w') as f:
    json.dump(combined, f, indent=2)

print(f"✓ Imported {len(new_faqs)} new FAQs")
```

Run: `python import_faqs.py`

## 🎯 Sample FAQ Database

Here's a comprehensive FAQ database you can use as a starting point:

```json
[
    {
        "question": "What is artificial intelligence?",
        "answer": "Artificial Intelligence (AI) is the simulation of human intelligence in machines. It enables computers to learn from experience, adapt to new inputs, and perform tasks that typically require human intelligence. AI applications include image recognition, natural language processing, recommendation systems, and autonomous vehicles."
    },
    {
        "question": "What is machine learning?",
        "answer": "Machine Learning is a subset of AI that enables systems to learn and improve from experience without being explicitly programmed. Instead of following pre-programmed instructions, ML algorithms analyze data, identify patterns, and make decisions based on those patterns."
    },
    {
        "question": "What is deep learning?",
        "answer": "Deep Learning is a subset of machine learning that uses neural networks with multiple layers (deep networks) to learn complex patterns. It's inspired by how the human brain works and has been very successful in image recognition, natural language processing, and speech recognition."
    },
    {
        "question": "What is natural language processing?",
        "answer": "Natural Language Processing (NLP) is a branch of AI that focuses on enabling computers to understand, interpret, and generate human language in a meaningful way. Applications include chatbots, translation services, sentiment analysis, and speech recognition."
    },
    {
        "question": "What is a neural network?",
        "answer": "A neural network is a computing system inspired by biological neural networks in animal brains. It consists of interconnected nodes (neurons) that work together to process information, learn patterns, and make predictions. Neural networks are fundamental to deep learning."
    },
    {
        "question": "How does this chatbot work?",
        "answer": "This FAQ chatbot works by: 1) Converting your question into embeddings (vectors), 2) Searching for similar FAQ questions using FAISS, 3) Using an LLM (Mistral) to generate a contextual answer based on relevant FAQs. This combines semantic search with AI generation."
    },
    {
        "question": "What is semantic search?",
        "answer": "Semantic search goes beyond keyword matching to understand the meaning and intent of a query. It uses embeddings and similarity measures to find relevant content based on meaning rather than just word matches. This is why the chatbot can answer questions phrased differently than the original FAQs."
    },
    {
        "question": "What is FAISS?",
        "answer": "FAISS (Facebook AI Similarity Search) is a library for fast similarity search and clustering of vector embeddings. It's optimized for searching through large collections of vectors quickly, making it perfect for finding the most relevant FAQs based on user questions."
    },
    {
        "question": "What is an LLM or Large Language Model?",
        "answer": "A Large Language Model (LLM) is an AI model trained on vast amounts of text data to understand and generate human language. Examples include GPT-3, GPT-4, Mistral, and Claude. LLMs can understand context and generate coherent, relevant responses."
    },
    {
        "question": "What is Ollama?",
        "answer": "Ollama is a tool that makes it easy to run large language models locally on your computer. It provides a simple interface to download, run, and interact with models like Mistral, Llama, and others without needing cloud services."
    },
    {
        "question": "How do embeddings work?",
        "answer": "Embeddings convert text into numerical vectors (arrays of numbers) that capture semantic meaning. Similar texts have similar embeddings. The chatbot uses sentence embeddings to compare your question with FAQ questions and find the most relevant ones."
    },
    {
        "question": "What is the difference between NLP and AI?",
        "answer": "AI is the broader field of creating intelligent machines. NLP is a specific subfield of AI focused on natural language understanding. All NLP is AI, but not all AI is NLP. AI also includes computer vision, robotics, and other domains."
    },
    {
        "question": "Can this system work offline?",
        "answer": "Yes! This system is designed to work completely offline. The FastAPI backend, embedding model, FAISS index, and Ollama LLM all run locally on your machine. No cloud services or internet connection is required during operation."
    },
    {
        "question": "How accurate are the responses?",
        "answer": "Accuracy depends on: 1) Quality of FAQs provided, 2) How well the question matches FAQ topics, 3) The LLM quality. The system returns the top-3 most relevant FAQs for context, so you can verify the sources. For specialized domains, include more relevant FAQs."
    },
    {
        "question": "Can I use this system with my own data?",
        "answer": "Absolutely! Replace the sample FAQs with your own data in `backend/faqs.json`. You can add as many Q&A pairs as needed. For large datasets, consider using a database instead of JSON for better scalability."
    }
]
```

## 🔄 Updating FAQs

### To Modify an Existing FAQ:

1. Find the FAQ in `faqs.json`
2. Update the question and/or answer
3. Save the file
4. Restart the backend

### To Delete an FAQ:

1. Remove the entire FAQ object from the array
2. Save the file
3. Restart the backend

## 📊 FAQ Best Practices

### Writing Good Questions

✅ **Good:**
- "What is machine learning?"
- "How do I get started with AI?"
- "What are the applications of deep learning?"

❌ **Avoid:**
- Vague questions: "Tell me something"
- Too specific: "On March 15, 2024, what was..."
- Multiple questions in one: "What is AI and why is it important?"

### Writing Good Answers

✅ **Good:**
- Clear and concise (1-3 sentences typically)
- Explains the concept, not just definitions
- Mentions related concepts for context

❌ **Avoid:**
- Too long (breaks chat UI formatting)
- Too vague (doesn't answer the question)
- Technical jargon without explanation

### FAQ Diversity

Include FAQs covering:
- Definitions and concepts
- How-to guides
- Troubleshooting
- Best practices
- Integration and setup
- Performance optimization

## 📈 Optimization Tips

### For Better Search Results:

1. **Vary Question Phrasing**: Include multiple ways to ask the same thing
   ```json
   [
       {"question": "What is AI?", "answer": "..."},
       {"question": "Define artificial intelligence", "answer": "..."},
       {"question": "How would you explain AI?", "answer": "..."}
   ]
   ```

2. **Include Related Keywords**:
   ```json
   {"question": "Machine learning vs AI - what's the difference?", "answer": "..."}
   ```

3. **Complete vs Fragmentary**:
   ```json
   [
       {"question": "What is a chatbot?", "answer": "..."},
       {"question": "How do chatbots work?", "answer": "..."},
       {"question": "Chatbot applications and uses", "answer": "..."}
   ]
   ```

### For Better LLM Responses:

1. **Detailed Answers**: More complete FAQ answers help the LLM generate better responses
2. **Clear Structure**: Use bullet points or numbers in answers
3. **Context**: Include relevant background information

## 🚀 Scaling FAQs

### Current Setup:
- **Capacity**: Up to 10,000+ FAQs
- **Performance**: <1ms search time (FAISS)
- **Memory**: ~100MB per 10,000 FAQs

### For Larger Datasets:

```python
# Use a database instead of JSON
import sqlite3

conn = sqlite3.connect('faqs.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE faqs (
        id INTEGER PRIMARY KEY,
        question TEXT,
        answer TEXT,
        category TEXT,
        created_at TIMESTAMP
    )
''')

# Load into system
cursor.execute('SELECT question, answer FROM faqs')
faqs = [{'question': q, 'answer': a} for q, a in cursor.fetchall()]
```

## 🔧 Advanced: Custom FAQ Ingestion

### From CSV File:

```python
import csv
import json

faqs = []
with open('faqs.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        faqs.append({
            'question': row['question'],
            'answer': row['answer']
        })

with open('backend/faqs.json', 'w') as f:
    json.dump(faqs, f, indent=2)
```

### From Markdown File:

```python
import json
import re

# Parse markdown format:
# ## Question
# Answer text

faqs = []
with open('faqs.md', 'r') as f:
    content = f.read()
    
matches = re.findall(r'## (.*?)\n(.*?)(?=##|$)', content, re.DOTALL)
for question, answer in matches:
    faqs.append({
        'question': question.strip(),
        'answer': answer.strip()
    })

with open('backend/faqs.json', 'w') as f:
    json.dump(faqs, f, indent=2)
```

## 📞 Troubleshooting

**Q: Changes to FAQs don't appear**
A: Restart the backend - it rebuilds the vector index on startup

**Q: Search results aren't relevant**
A: Check if FAQs are specific enough. Vague FAQs lead to poor semantic matching.

**Q: System is slow with many FAQs**
A: If you have >50K FAQs, consider using a GPU with Ollama or a different vector index

---

Happy FAQ building! 🚀
