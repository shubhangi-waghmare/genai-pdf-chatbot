import os
from dotenv import load_dotenv
from google import genai

from prompts.prompt import RAG_PROMPT
from vectorstore.retriever import retrieve_docs

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def get_answer(question: str):

    docs = retrieve_docs(question)

    if not docs:
        return "No relevant information found."

    context = ""

    sources = []

    for doc in docs:

        context += doc.page_content + "\n\n"

        source = doc.metadata.get("source")

        if source and source not in sources:
            sources.append(source)

    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    answer = response.text.strip()

    if sources:

        answer += "\n\n📄 Source(s):\n"

        for source in sources:
            answer += f"- {source}\n"

    return answer