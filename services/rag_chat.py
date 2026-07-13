import os
from dotenv import load_dotenv

from google import genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

#Load API Key
load_dotenv()

#Gemini Client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

#Embedding Model
embeddings = GoogleGenerativeAIEmbeddings(
model="models/gemini-embedding-001",
google_api_key=os.getenv("GOOGLE_API_KEY")
)

#Load ChromaDB
vector_db = Chroma(
persist_directory="chroma_db",
embedding_function=embeddings
)

# User Question
question = input("Ask your question:")

#Retrieve Top 3 Chunks
docs = vector_db.similarity_search(question, k=3)

#Create Context
context = "\n\n".join([doc.page_content for doc in docs])

#Prompt 
prompt = f"""
You are an AI assistant.

Answer ONLY using the context below

Context:
{context}

Question:
{question}

If theanswer is not present in the context,
reply:
"I couldn't find the answer in the uploaded PDF."
"""

#Gemini Response 
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("\nAnswer:\n")
print(response.text)


