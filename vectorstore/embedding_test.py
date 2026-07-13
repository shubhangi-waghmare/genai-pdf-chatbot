import os
from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_keys=os.getenv("GOOGLE_API_KEY")
)

text = "Python is used for Machine Learning"

vector = embeddings.embed_query(text)

print("Embedding Created Successfully")
print(f"Vector Length : {len(vector)}")
print(vector[:10])  #first 10 numbers