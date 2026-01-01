# Autonomous RAG-Based AI Agent for Document Intelligence

This project implements an autonomous AI agent capable of multi-step reasoning,
tool invocation, and retrieval-augmented generation (RAG) for document-based
question answering.

## Key Features
- Autonomous decision-making using LangGraph
- Tool-based RAG retrieval (agent chooses when to retrieve)
- Stateful memory for follow-up queries
- Groq-hosted LLaMA-3 for low-latency inference
- Modular, production-style architecture

## Architecture Overview
User Query → Agent (Decision) → Tool Invocation (RAG / Direct Answer) → LLM → Response

## Tech Stack
- Python
- LangChain & LangGraph
- Groq (LLaMA-3)
- FAISS Vector Store
- HuggingFace Embeddings
- Gradio UI

## Use Cases
- Enterprise document intelligence
- Policy / legal / technical document Q&A
- Knowledge-grounded AI agents
