'''
proxy server의 역할
1) embedding server에 embedding 요청 -> embedding model과 client 요청 필요
2) search server(faiss)에 search 요청 -> embedding model과 client 요청 필요
3) meta_db에 search 요청 -> 몽고db연결 -> connection.py 작성
'''

from typing import Annotated
from fastapi import APIRouter, UploadFile, Form, File
import uuid
import os
import httpx, time

from infra.embedding.client import EmbeddingClient
from infra.search.client import SearchClient
from infra.storage.client import LocalStorageClient, GCStorageClient

from models.proxy import ImageP, TextP, FilterP

from dotenv import dotenv_values
from pymongo import MongoClient
from pprint import pprint

from .utils import objectIdDecoder

# config = dotenv_values("/opt/ml/fashion-image-search/server/admin/.env")
import yaml
with open('../config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    
proxy_router = APIRouter(
    tags=["Proxy"],
)

embedding_client = EmbeddingClient()
search_client = SearchClient()
storage_client = LocalStorageClient("queries", config_path="../config.yaml")

client = MongoClient(config["mongodb"]["url"],connect=False)
mydb = client[config["mongodb"]["name"]]

@proxy_router.post("/search-by-image")
# async def search_by_image(file: UploadFile, thresh: float) -> dict:
async def search_by_image(file: Annotated[UploadFile, File()], thresh: Annotated[float, Form()]) -> dict:
    # -- input_image를 storage/queries 저장
    print(f"proxy server 여기까지는 왔니? - 1, thresh - {thresh}")
    
    content = await file.read()
    rid = str(uuid.uuid4())
    filename = f"{rid}.png" # --uuid로 유니크한 파일명으로 변경(중복방지)
    storage_client.save(filename, content)
    print("여기 도착했나요??")
    embedding = await embedding_client.get_image_embedding(rid)
    
    dists, ids = await search_client.search(embedding, thresh)
    
    # fine_one의 Execution time: 3.6651980876922607 seconds > 실제 검색 시 8.37s
    # find의 Execution time: 0.20023798942565918 seconds
    # find + ids의 순서로 정렬한 것의 Execution time: 0.20313620567321777 seconds > 실제 검색 시 6.11s
    # ids의 순서는 곧 유사도의 순위 >find_one이 find보다 18배나 느림 하지만 유사도 순으로 정렬되어있음.
    # find 후 정렬을 사용하는 것이 find만 사용하는 것보다 0.0003s 차이지만 find_one보다는 압도적 성능을 지닌다.
    # 빠른 검색이 목적: find / 유사도 정렬이 목적: find_one
 
    collection = mydb[config["mongodb"]["collection"]]
    documents = collection.find({'key': {'$in': ids}})
    sorted_documents = sorted(documents, key=lambda doc: ids.index(doc['key']))

    # product_list = []
    # for doc in sorted_documents:
    #     print(doc['meta'])

    # print("여기를 살펴보자!", sorted_documents)
    return {
        # "msg": "OK",
        # "embedding": embedding,
        # "dists": dists,
        # "ids": ids,
        "상품목록": objectIdDecoder(sorted_documents)
    }
    

@proxy_router.post("/search-by-text")
async def search_by_text(textp: TextP)-> dict:
    print("proxy server 여기까지는 왔니? - 2")
    
    text = textp.text
    thresh = textp.thresh
    
    embedding = await embedding_client.get_text_embedding(text)
    
    dists, ids = await search_client.search(embedding, thresh)
    
    collection = mydb["Top"]
    documents = collection.find({'key': {'$in': ids}})
    sorted_documents = sorted(documents, key=lambda doc: ids.index(doc['key']))

    for doc in sorted_documents:
        print(doc)
    
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
    
    collection = mydb[config["mongodb"]["collection"]]
    documents = collection.find({'key': {'$in': ids}})
    sorted_documents = sorted(documents, key=lambda doc: ids.index(doc['key']))

    # print("list", type(sorted_documents))
    # print("찾은 상품의 수", len(list(sorted_documents)))
    # print("첫 번째", sorted_documents[0])
    # print("뭐가 나올까요?", objectIdDecoder(sorted_documents))
    # for doc in sorted_documents:
    #     print(doc)
  
    return {
        # "msg": "OK",
        # "embedding": embedding,
        # "dists": dists,
        # "ids": ids,
        "상품목록": objectIdDecoder(sorted_documents)
    }