# 🤖 GenAI PDF Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF documents and ask questions using Google's Gemini LLM. The application retrieves the most relevant content from the document using vector embeddings before generating accurate responses.

## 🚀 Features

* Upload PDF documents
* Extract text from PDFs
* Intelligent text chunking
* Vector embeddings with Google Gemini Embeddings
* ChromaDB vector database
* Semantic similarity search
* RAG-based question answering
* Streamlit web interface

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Google Gemini API
* ChromaDB
* RecursiveCharacterTextSplitter
* Vector Embeddings

## 📂 Project Structure

```text
genai-pdf-chatbot/
├── app.py
├── streamlit_app.py
├── config.py
├── chatbot.py
├── data/
├── loaders/
├── prompts/
├── services/
├── utils/
├── vectorstore/
├── requirements.txt
└── README.md
```

## ⚙️ Installation

```bash
git clone https://github.com/shubhangi-waghmare/genai-pdf-chatbot.git
cd genai-pdf-chatbot

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run streamlit_app.py
```

## 💡 How It Works

1. Upload a PDF document.
2. Extract text from the PDF.
3. Split text into chunks.
4. Generate embeddings using Gemini.
5. Store embeddings in ChromaDB.
6. Retrieve the most relevant chunks.
7. Generate answers using the Gemini LLM.

## 📸 Screenshots

Add screenshots of:

* Home page
* PDF upload
* Chat interface
* Sample response

## 📌 Future Improvements

* Multi-PDF support
* Chat history
* Source citations
* FAISS support
* Docker deployment
* AWS deployment

## 👩‍💻 Author

**Shubhangi Waghmare**

* GitHub: https://github.com/shubhangi-waghmare
* LinkedIn: https://www.linkedin.com/in/shubhangi-waghmare-2399a8250
