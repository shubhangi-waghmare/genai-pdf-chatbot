from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Python is a programming language.
It is used for AI and Machine Learning.
LangChain is used to build RAG applications.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 50,
    chunk_overlap=20
)

chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}:")
    print(chunk)