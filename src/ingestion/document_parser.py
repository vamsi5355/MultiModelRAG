import fitz  # PyMuPDF
import pdfplumber
import os
import uuid
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class DocumentParser:
    def __init__(self):
        pass

    def parse_pdf(self, pdf_path):
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"{pdf_path} not found")

        results = []

        # ---------- TEXT & IMAGES (PyMuPDF) ----------
        doc = fitz.open(pdf_path)

        for page_number in range(len(doc)):
            page = doc[page_number]

            # Extract text
            text = page.get_text("text").strip()
            if text:
                results.append({
                    "id": str(uuid.uuid4()),
                    "content_type": "text",
                    "document_id": os.path.basename(pdf_path),
                    "page_number": page_number + 1,
                    "raw_reference": None,
                    "text": text
                })

            # Extract images
            image_list = page.get_images(full=True)

            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]

                image_filename = f"extracted_{uuid.uuid4()}.{image_ext}"
                image_path = os.path.join("sample_documents", image_filename)

                with open(image_path, "wb") as f:
                    f.write(image_bytes)

                # OCR on embedded image
                pil_image = Image.open(image_path)
                extracted_text = pytesseract.image_to_string(pil_image)

                results.append({
                    "id": str(uuid.uuid4()),
                    "content_type": "image",
                    "document_id": os.path.basename(pdf_path),
                    "page_number": page_number + 1,
                    "raw_reference": image_path,
                    "text": extracted_text.strip()
                })

        doc.close()

        # ---------- TABLE EXTRACTION (pdfplumber) ----------
        with pdfplumber.open(pdf_path) as pdf:
            for page_number, page in enumerate(pdf.pages):
                tables = page.extract_tables()

                for table in tables:
                    structured_table = []
                    for row in table:
                        structured_table.append(row)

                    results.append({
                        "id": str(uuid.uuid4()),
                        "content_type": "table",
                        "document_id": os.path.basename(pdf_path),
                        "page_number": page_number + 1,
                        "raw_reference": None,
                        "text": str(structured_table)
                    })

        return results