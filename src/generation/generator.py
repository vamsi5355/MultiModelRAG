import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key=api_key)


class Generator:

    def generate_answer(self, query, retrieved_context):

        context_text = ""
        sources = []

        for item in retrieved_context:

            text = item.get("text", "")

            if text:
                context_text += text + "\n"

            sources.append({
                "document_id": item.get("document_id"),
                "page_number": item.get("page_number"),
                "content_type": item.get("content_type"),
                "snippet": text[:200]
            })

        if not context_text.strip():
            return {
                "answer": "No relevant information found.",
                "confidence": 0.0,
                "sources": sources
            }

        prompt = f"""
Answer the question ONLY using the context.

Context:
{context_text}

Question:
{query}

Give a short answer.
"""

        try:

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )

            answer = response.text

        except Exception as e:

            answer = f"LLM generation failed: {str(e)}"

        return {
            "answer": answer,
            "confidence": 0.9,
            "sources": sources
        }