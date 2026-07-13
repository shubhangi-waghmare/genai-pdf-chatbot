from config import PDF_PATH, CHUNK_SIZE, CHUNK_OVERLAP

from loaders.pdf_loader import load_pdf_text
from langchain_text_splitters import RecursiveCharacterTextSplitter

# PDF Path
pdf_path = PDF_PATH

# Step 1 - Load PDF
text = load_pdf_text(pdf_path)

print("=" * 50)
print("PDF Loaded Successfully")
print("=" * 50)

print(f"\nTotal Characters : {len(text)}")

# Step 2 - Split Text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
)

chunks = splitter.split_text(text)

print(f"\nTotal Chunks : {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])