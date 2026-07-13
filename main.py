from fastapi import FastAPI
from pydantic import BaseModel

from services.rag_service import get_answer

app = FastAPI(title="GenAI PDF Chatbot API")


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "GenAI PDF Chatbot API is running!"
    }


@app.post("/chat")
def chat(request: QuestionRequest):
    answer = get_answer(request.question)

    return {
        "question": request.question,
        "answer": answer
    }