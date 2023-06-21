from fastapi import APIRouter

from infra.search.model import SearchModel
from models.search import ImgEmbedding

search_router = APIRouter(
    tags=["Search"],
)

model = SearchModel()

# -- get을 써야해, post를 써야해?
@search_router.post("")
async def search(Imgembedding: ImgEmbedding) -> dict:
    
    dists, ids = model.search(Imgembedding.embedding)
    
    return {
        "msg": "Search OK!",
        "dists": dists,
        "ids": ids,
    }