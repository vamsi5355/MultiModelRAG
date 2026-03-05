from sentence_transformers import SentenceTransformer
from PIL import Image
import numpy as np


class EmbeddingModel:

    def __init__(self):
        self.model = SentenceTransformer("clip-ViT-B-32")

    def embed_text(self, text: str):
        embedding = self.model.encode(text)
        return np.array(embedding)

    def embed_image(self, image_path: str):
        image = Image.open(image_path).convert("RGB")

        # sentence-transformers CLIP accepts images through encode()
        embedding = self.model.encode(image)  # type: ignore

        return np.array(embedding)