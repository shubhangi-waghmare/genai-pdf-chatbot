from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

 llm = ChatGoogleGenerativeAI
    (model="gemini-1.5-flash-latest"),
    google_api_key=api_key
)

response = llm.invoke("Explain what is RAG in simple words")

print(response.content)