from fastapi import FastAPI
from pydantic import BaseModel

from src.vector_store.faiss_manager import FAISSManager
from src.retrieval.retriever import Retriever
from src.generation.generator import Generator
from src.ingestion.document_parser import DocumentParser
from src.embeddings.model_loader import EmbeddingModel


app = FastAPI()

vector_db = FAISSManager()
embedding_model = EmbeddingModel()

# parse document
parser = DocumentParser()
documents = parser.parse_pdf("sample_documents/test.pdf")

# add each document chunk to FAISS
for doc in documents:

    text = doc.get("text", "")

    if not text:
        continue

    embedding = embedding_model.embed_text(text)

    vector_db.add_vector(embedding, doc)


retriever = Retriever(vector_db)
generator = Generator()


class QueryRequest(BaseModel):
    query: str


@app.post("/query")
def query(request: QueryRequest):

    retrieved_context = retriever.retrieve(request.query)

    result = generator.generate_answer(
        request.query,
        retrieved_context
    )

    return result