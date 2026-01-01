from langchain_community.vectorstores import FAISS
from rag.embeddings import get_embedding_model
import os

VECTOR_DB_PATH = "data/vectorstore"

def create_vectorstore(docs):
    """
    Creates and saves a FAISS vector store.
    """
    embeddings = get_embedding_model()
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(VECTOR_DB_PATH)
    return vectorstore


def load_vectorstore():
    """
    Loads existing FAISS vector store.
    """
    embeddings = get_embedding_model()
    if not os.path.exists(VECTOR_DB_PATH):
        raise FileNotFoundError("Vector store not found. Run ingestion first.")
    return FAISS.load_local(
    VECTOR_DB_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)
