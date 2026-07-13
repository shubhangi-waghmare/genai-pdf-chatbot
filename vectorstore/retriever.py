import os
from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

from config import CHROMA_DB_PATH, TOP_K, EMBEDDING_MODEL

load_dotenv()


def retrieve_docs(query: str, k: int = TOP_K):

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    vector_db = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embeddings
    )

    results = vector_db.max_marginal_relevance_search(
        query=query,
        k=k,
        fetch_k=10
    )

    return results


if __name__ == "__main__":

    docs = retrieve_docs("experience")

    for doc in docs:
        print(doc.metadata)