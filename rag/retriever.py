from rag.vectorstore import load_vectorstore

def retrieve_context(query: str, k: int = 4) -> str:
    """
    Retrieves top-k relevant document chunks for a query.
    """
    vectorstore = load_vectorstore()
    docs = vectorstore.similarity_search(query, k=k)
    return "\n".join([doc.page_content for doc in docs])
