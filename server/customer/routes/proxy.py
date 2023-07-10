'''
proxy server의 역할
1) embedding server에 embedding 요청 -> embedding model과 client 요청 필요
2) search server(faiss)에 search 요청 -> embedding model과 client 요청 필요
3) meta_db에 search 요청 -> 몽고db연결 -> connection.py 작성
'''

from typing import Annotated
from fastapi import APIRouter, UploadFile, Form
import uuid
import os
import httpx

from infra.embedding.client import EmbeddingClient
from infra.search.client import SearchClient
from infra.storage.client import LocalStorageClient

from models.proxy import ImageP, TextP, FilterP

proxy_router = APIRouter(
    tags=["Proxy"],
)

embedding_client = EmbeddingClient()
search_client = SearchClient()
storage_client = LocalStorageClient("queries")

@proxy_router.post("/search-by-image")
# async def search_by_image(file: UploadFile, thresh: float) -> dict:
async def search_by_image(file: UploadFile, thresh: Annotated[float, Form()]) -> dict:
    # -- input_image를 storage/queries 저장
    print(f"proxy server 여기까지는 왔니? - 1, thresh - {thresh}")
    
    content = await file.read()
    rid = str(uuid.uuid4())
    filename = f"{rid}.png" # --uuid로 유니크한 파일명으로 변경(중복방지)
    storage_client.save(filename, content)
    print("여기 도착했나요??")
    embedding = await embedding_client.get_image_embedding(rid)
    
    dists, ids = await search_client.search(embedding, thresh)
    
    return {
        "msg": "OK",
        "embedding": embedding,
        "dists": dists,
        "ids": ids,
    }
    

@proxy_router.post("/search-by-text")
async def search_by_text(textp: TextP)-> dict:
    print("proxy server 여기까지는 왔니? - 2")
    
    text = textp.text
    thresh = textp.thresh
    
    print(text)
    print(thresh)
    
    embedding = await embedding_client.get_text_embedding(text)
    
    dists, ids = await search_client.search(embedding, thresh)
    
    return {
        "msg": "OK",
        "embedding": embedding,
        "dists": dists,
        "ids": ids,
    }
    

@proxy_router.post("/search-by-filter")
async def search_by_filter(file: UploadFile, text: Annotated[str, Form()], thresh: Annotated[float, Form()]) -> dict:
    # -- input_image를 storage/queries 저장
    content = await file.read()
    rid = str(uuid.uuid4())
    filename = f"{rid}.png"
    storage_client.save(filename, content)
        
    embedding = await embedding_client.get_image_embedding(rid)
    
    filter_embedding = await embedding_client.get_text_embedding(text)
    
    dists, ids = await search_client.search_with_filter(embedding, filter_embedding, thresh)
    
    return {
        "msg": "OK",
        "embedding": embedding,
        "dists": dists,
        "ids": ids,
    }