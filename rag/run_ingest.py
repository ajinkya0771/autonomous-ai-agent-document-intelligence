from rag.ingest import load_documents, chunk_documents
from rag.vectorstore import create_vectorstore

DATA_PATH = "data/sample_docs"

def main():
    print("Loading documents...")
    docs = load_documents(DATA_PATH)

    if not docs:
        raise ValueError(
            "No documents found. Add .txt files to data/sample_docs"
        )

    print("Chunking documents...")
    chunks = chunk_documents(docs)

    print("Creating vector store...")
    create_vectorstore(chunks)

    print("Vector store created successfully.")

if __name__ == "__main__":
    main()
