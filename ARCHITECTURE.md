System Architecture

Overview

MultiModelRag is a Multimodal Retrieval-Augmented Generation (RAG) system that allows users to ask questions about PDF documents containing both text and images.

The system extracts information from documents, generates embeddings, retrieves relevant content using vector search, and uses a Large Language Model (Gemini) to generate answers.

---

Architecture Flow

PDF Documents
      │
      ▼
Document Processing
(Text Extraction + OCR)
      │
      ▼
Embedding Generation
(CLIP / Sentence Transformers)
      │
      ▼
Vector Storage
(FAISS)
      │
      ▼
User Query
      │
      ▼
Query Embedding
      │
      ▼
Similarity Search
(Top-K Retrieval)
      │
      ▼
Retrieved Context
      │
      ▼
LLM (Gemini)
      │
      ▼
Generated Answer + Sources

---

Components

1. Document Processing

PDF documents are processed to extract text and images.
OCR (Tesseract) is used to extract text from images inside PDFs.

2. Embedding Model

Extracted text and image content are converted into vector embeddings using CLIP via Sentence Transformers.

3. Vector Database

Embeddings are stored in FAISS, which allows efficient similarity search.

4. Retriever

When a user asks a question, the query is converted into an embedding and FAISS retrieves the most relevant document chunks.

5. LLM Generation

The retrieved context and the user query are passed to Gemini LLM, which generates the final answer.

6. API Layer

The system exposes a FastAPI endpoint ("/query") where users can send questions and receive answers along with document sources.

---