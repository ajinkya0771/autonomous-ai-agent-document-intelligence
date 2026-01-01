# 🤖 Autonomous AI Agent for Document Intelligence
RAG-Powered | FAISS | Groq LLaMA 3.1 | LangGraph
<p align="center"> <img src="https://img.shields.io/badge/AI-Agent-blueviolet?style=for-the-badge" /> <img src="https://img.shields.io/badge/RAG-Enabled-success?style=for-the-badge" /> <img src="https://img.shields.io/badge/FAISS-VectorDB-orange?style=for-the-badge" /> <img src="https://img.shields.io/badge/Groq-LLM-black?style=for-the-badge" /> <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge" /> </p> <p align="center"> <b>An end-to-end Autonomous AI Agent that performs document-grounded reasoning using Retrieval-Augmented Generation (RAG).</b> </p>

## 📑 Table of Contents

👉 Clicking any item below will auto-scroll on GitHub

- [Project Overview](#-project-overview)
- [Project Structure](#-project-structure)
- [Key Capabilities](#-key-capabilities)
- [System Architecture](#-system-architecture)
- [Tech Stack](#️-tech-stack)
- [Setup Instructions](#️-setup-instructions)
- [Document Ingestion](#-document-ingestion-vector-store-creation)
- [Running the Autonomous AI Agent](#-run-the-autonomous-ai-agent)
- [Execution Screenshots](#-execution-screenshots)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)


## 🚀 Project Overview

This project implements a production-style Autonomous AI Agent capable of answering questions strictly based on uploaded documents.

Instead of relying only on model memory, the agent:

Retrieves relevant document context

Grounds responses using a vector database

Uses LLM reasoning only after retrieval

This mirrors real enterprise GenAI systems used in:

Document intelligence

Compliance & policy Q&A

Research assistants

Internal knowledge systems

📂 Project Structure
```
autonomous-ai-agent-document-intelligence/
│
├── agent/               # Agent logic & orchestration
│   ├── graph.py
│   ├── prompts.py
│   ├── state.py
│   └── tools.py
│
├── rag/                 # RAG pipeline
│   ├── ingest.py
│   ├── retriever.py
│   ├── vectorstore.py
│   └── embeddings.py
│
├── llm/                 # Groq LLM configuration
├── data/
│   ├── sample_docs/
│   └── vectorstore/
├── screenshots/
├── ui/
├── main.py
├── requirements.txt
└── README.md
```
## ✨ Key Capabilities

Autonomous agent orchestration using LangGraph

Retrieval-Augmented Generation (RAG)

Semantic document ingestion and chunking

FAISS vector search for fast retrieval

HuggingFace MiniLM embeddings

Groq LLaMA 3.1 for low-latency inference

Modular, extensible architecture

CLI-based interactive querying

## 🧠 System Architecture
User Query
   ↓
Autonomous AI Agent
   ↓
RAG Tool Invocation
   ↓
FAISS Vector Store
   ↓
Relevant Document Chunks
   ↓
Groq LLM (Grounded Answer)


✔ Prevents hallucination
✔ Answers strictly from documents
✔ Agent decides when to retrieve

## 🛠️ Tech Stack
Layer	Technology
Language	Python 3.10+
Agent Framework	LangGraph
RAG Framework	LangChain
Vector Database	FAISS
Embeddings	HuggingFace (all-MiniLM-L6-v2)
LLM	Groq – LLaMA 3.1
Environment	Virtualenv
Version Control	Git & GitHub

## ⚙️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/ajinkya0771/autonomous-ai-agent-document-intelligence.git
cd autonomous-ai-agent-document-intelligence

2️⃣ Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key_here

📥 Document Ingestion (Vector Store Creation)
python -m rag.run_ingest


Loads documents

Splits into chunks

Generates embeddings

Stores vectors in FAISS

🤖 Run the Autonomous AI Agent
python main.py


Example:

Ask a question:
Based only on the uploaded document, explain what Retrieval-Augmented Generation is.


✔ Agent invokes retrieval tool
✔ Fetches relevant context
✔ Generates grounded answer

## 📸 Execution Screenshots
Step	Description
01	Project structure
02	Virtual environment activated
03	Vector store created
04	Autonomous agent started
05	Direct LLM response
06	RAG tool invocation
07	Document-grounded answer
🔮 Future Enhancements

Multi-Level / Hierarchical RAG

Tool routing based on intent

Metadata-aware retrieval

Memory-enabled agents

Web UI (Streamlit / FastAPI)

Enterprise document pipelines

## 📌 Author

Ajinkya Dhote
AI / GenAI Engineer
GitHub: https://github.com/ajinkya0771
