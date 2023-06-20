from fastapi import APIRouter
from infra.embedding.model import EmbeddingModel

embedding_router = APIRouter(
    tags=["Embedding"]
)

model = EmbeddingModel()

@embedding_router.get("/{rid}")
async def get_embedding(rid: str) -> dict:
    print("rid는 여기다!:", rid)
    embedding = model.get_embedding(rid)
    return {
        "msg": "OK!",
        "embedding": embedding
    }

