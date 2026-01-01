from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

def load_documents(data_path: str):
    """
    Loads text documents from a directory.
    """
    documents = []
    for file in os.listdir(data_path):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(data_path, file))
            documents.extend(loader.load())
    return documents


def chunk_documents(documents):
    """
    Splits documents into chunks with overlap.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    return splitter.split_documents(documents)
