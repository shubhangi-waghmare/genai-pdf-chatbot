RAG_PROMPT = """
Use the following context to answer the user's question.

Context:
{context}

Question:
{question}

Rules:
1. Answer only from the given context.
2. If the answer is not available in the context, say "I don't know."
3. Do not make up information.

Answer:
"""