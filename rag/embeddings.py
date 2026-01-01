from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_model():
    """
    Returns a sentence-transformer embedding model.
    """
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
