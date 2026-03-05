MultiModelRag

MultiModelRag is a Multimodal Retrieval-Augmented Generation (RAG) system that allows users to query information from PDF documents containing both text and images.

The system processes documents, extracts textual and visual information, generates embeddings, stores them in a vector database, retrieves relevant context, and uses a Large Language Model (LLM) to generate answers.

---

Key Features

- PDF document ingestion
- OCR extraction from document images
- Multimodal embeddings using CLIP
- Vector similarity search with FAISS
- Retrieval-Augmented Generation pipeline
- FastAPI REST API
- Source attribution in responses
- LLM-based answer generation using Gemini

---

System Architecture

PDF Documents
      ↓
Text Extraction (PyMuPDF / pdfplumber)
      ↓
OCR Processing (Tesseract)
      ↓
Embedding Generation (CLIP / Sentence Transformers)
      ↓
Vector Database (FAISS)
      ↓
Retriever
      ↓
LLM (Gemini) Answer Generation
      ↓
FastAPI API

---

Project Structure

MultiModelRag
│
├── sample_documents
│   └── test.pdf
│
├── src
│   ├── api
│   │   └── main.py
│   │
│   ├── embeddings
│   │   └── model_loader.py
│   │
│   ├── ingestion
│   │   └── document_processor.py
│   │
│   ├── retrieval
│   │   └── retriever.py
│   │
│   ├── generation
│   │   └── generator.py
│   │
│   └── vector_store
│       └── faiss_manager.py
│
├── tests
│
├── ARCHITECTURE.md
├── evaluation.py
├── requirements.txt
├── submission.yml
├── .env.example
└── README.md

---

Installation

1. Clone the repository

git clone <repository-url>
cd MultiModelRag

---

2. Install dependencies

pip install -r requirements.txt

---

3. Install Tesseract OCR

The project uses pytesseract for OCR.

Download and install Tesseract:

https://github.com/UB-Mannheim/tesseract/wiki

Ensure the Tesseract executable is added to your system PATH.

---

Configure API Key

This project requires a Gemini API key for answer generation.

Create a ".env" file in the project root:

GEMINI_API_KEY=your_api_key_here

---

Running the API

Start the FastAPI server:

uvicorn src.api.main:app --reload

The API will be available at:

http://127.0.0.1:8000

---

Query API

Endpoint:

POST /query

Example request:

{
  "query": "Who completed the course?"
}

Example response:

{
  "answer": "Madhu Vamsi Anupoju completed the course.",
  "confidence": 0.9,
  "sources": [
    {
      "document_id": "test.pdf",
      "page_number": 1,
      "content_type": "text",
      "snippet": "Madhu Vamsi Anupoju Introduction to Artificial Intelligence..."
    }
  ]
}

---

Running Evaluation

To run the evaluation script:

python evaluation.py

This script sends predefined queries to the API and prints the responses.

---

Important Note

This project uses Gemini LLM for answer generation.
If the API quota is exceeded or the API key is not configured, the system may return an error from the LLM service.

---

Technologies Used

- FastAPI
- FAISS
- Sentence Transformers
- CLIP embeddings
- PyMuPDF
- pdfplumber
- Tesseract OCR
- Google Gemini API
- NumPy
- Python

---
