from fashion_clip.fashion_clip import FashionCLIP
import numpy as np
import os
import yaml

class EmbeddingModel:
    
    def __init__(self, config_path: str) -> None:
        with open(config_path) as f:
            self.conf = yaml.safe_load(f)
        self.IMG_DIR = os.path.join(self.conf["storage"], "queries")
        self.flip = FashionCLIP("fashion-clip")
        
    
    def get_image_embedding(self, rid: str) -> list[float]:
        filename = f"{rid}.png"
        
        img_path = os.path.join(self.IMG_DIR, filename)
        embedding = self.flip.encode_images([img_path], batch_size=1).flatten() # (1, 512) -> flatten -> (512,)
        embedding /= np.linalg.norm(embedding) # 정규화
        return embedding.tolist()
    
    
    def get_text_embedding(self, text: str) -> list[float]:
        embedding = self.flip.encode_text([text], batch_size=1).flatten() #(1, 512) -> flatten -> (512,)
        embedding /= np.linalg.norm(embedding) # 정규화
        return embedding.tolist()