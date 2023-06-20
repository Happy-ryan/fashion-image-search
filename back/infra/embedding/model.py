from fashion_clip.fashion_clip import FashionCLIP
import numpy as np
import os

class EmbeddingModel:
    IMG_PATH = "storage/queries"
    
    def __init__(self) -> None:
        self.flip = FashionCLIP("fashion-clip")
        
    
    def get_embedding(self, rid: str) -> list[float]:
        filename = f"{rid}.png"
        
        img_path = os.path.join(self.IMG_PATH, filename)
        embedding = self.flip.encode_images([img_path], batch_size=1).flatten() # (1, 512) -> flatten -> (512,)
        return embedding.tolist()