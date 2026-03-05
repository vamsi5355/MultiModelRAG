import os
from PIL import Image
import uuid
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class ImageProcessor:
    def __init__(self):
        pass

    def process_image(self, image_path):
        """
        Process standalone image:
        - Perform OCR
        - Return structured content
        """

        if not os.path.exists(image_path):
            raise FileNotFoundError(f"{image_path} not found")

        image = Image.open(image_path)

        # OCR extraction
        extracted_text = pytesseract.image_to_string(image)

        content_id = str(uuid.uuid4())

        return {
            "id": content_id,
            "content_type": "image",
            "document_id": os.path.basename(image_path),
            "page_number": 0,
            "raw_reference": image_path,
            "text": extracted_text.strip()
        }