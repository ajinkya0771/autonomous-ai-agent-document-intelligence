from langchain_core.tools import Tool
from rag.retriever import retrieve_context


def get_rag_tool():
    """
    RAG retrieval tool callable by the AI agent.
    """
    return Tool(
        name="document_retrieval",
        func=retrieve_context,
        description=(
            "Use this tool to retrieve relevant information "
            "from documents when answering factual or document-based questions."
        )
    )
