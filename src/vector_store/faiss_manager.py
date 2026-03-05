import faiss
import numpy as np
import json
import os


class FAISSManager:

    def __init__(self, dim=512):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []

    def add_vector(self, embedding, metadata):
        embedding = np.array([embedding]).astype("float32")
        self.index.add(embedding)
        self.metadata.append(metadata)

    def search(self, query_embedding, top_k=5):
        D, I = self.index.search(query_embedding, top_k)
        results = []
        for idx in I[0]:
            # skip invalid FAISS results
            if idx < 0 or idx >= len(self.metadata):
                continue
            results.append(self.metadata[idx])
        return results

    def save(self, path="faiss_index"):
        os.makedirs(path, exist_ok=True)

        faiss.write_index(self.index, f"{path}/index.faiss")

        with open(f"{path}/metadata.json", "w") as f:
            json.dump(self.metadata, f)

    def load(self, path="faiss_index"):
        self.index = faiss.read_index(f"{path}/index.faiss")

        with open(f"{path}/metadata.json") as f:
            self.metadata = json.load(f)