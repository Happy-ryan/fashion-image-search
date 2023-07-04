from fastapi import APIRouter

from infra.embedding.model import EmbeddingModel
from models.embedding import Text

embedding_router = APIRouter(
    tags=["Embedding"]
)

model = EmbeddingModel()

@embedding_router.get("/image/{rid}")
async def get_image_embedding(rid: str) -> dict:
    print("rid는 여기다!:", rid)
    embedding = model.get_image_embedding(rid)
    return {
        "msg": "OK!",
        "embedding": embedding
    }
    
# url에 query x => post => 요청바디 필요
@embedding_router.post("/text")
async def get_image_embedding(text: Text) -> dict:
    print("내가 넣은 text는 여기다!:", text.text)
    embedding = model.get_text_embedding(text.text)
    return {
        "msg": "OK!",
        "embedding": embedding
    }

