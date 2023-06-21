from pydantic import BaseModel


class ImgEmbedding(BaseModel):
    
    embedding: list[float]