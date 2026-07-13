import os
from dotenv import load_dotenv

from loaders.pdf_loader import load_pdf_text
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

from config import (
    DATA_FOLDER,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    EMBEDDING_MODEL,
    CHROMA_DB_PATH,
)

load_dotenv()


def create_vector_db():
    """
    Rebuild ChromaDB from all PDFs inside the data folder.
    """

    all_chunks = []
    metadatas = []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    pdf_files = [
        f for f in os.listdir(DATA_FOLDER)
        if f.lower().endswith(".pdf")
    ]

    if not pdf_files:
        raise Exception("No PDF files found inside data folder.")

    for pdf in pdf_files:

        pdf_path = os.path.join(DATA_FOLDER, pdf)

        print(f"Loading: {pdf}")

        text = load_pdf_text(pdf_path)

        chunks = splitter.split_text(text)

        all_chunks.extend(chunks)

        metadatas.extend(
            [{"source": pdf} for _ in chunks]
        )

    print(f"\nTotal Chunks Before Embedding: {len(all_chunks)}")

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    vector_db = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embeddings
    )

    # Clear old collection
    vector_db.reset_collection()

    # Add fresh documents
    vector_db.add_texts(
        texts=all_chunks,
        metadatas=metadatas
    )

    print("\n✅ ChromaDB Updated Successfully")
    print(f"Total Chunks Stored: {len(all_chunks)}")

    return vector_db


if __name__ == "__main__":
    create_vector_db()