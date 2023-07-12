from fastapi import APIRouter, UploadFile, File, Form
from io import StringIO
import pandas as pd

from typing import Annotated
from dotenv import dotenv_values
from pymongo import MongoClient

from infra.client import DataBaseClient
from .utils import makeJsonList

config = dotenv_values(".env")

proxy_router = APIRouter(
    tags=["Proxy"],
)

database_client = DataBaseClient()

client = MongoClient(config["ATLAS_URI"],connect=False)
mydb = client[config["DB_NAME"]]

@proxy_router.post('/products-upload')
async def upload(file: UploadFile = File(...), type: str = Form(...)):
    # csv 읽기
    contents = file.file.read()
    s = str(contents,'utf-8')
    data = StringIO(s)
    df = pd.read_csv(data)
    data.close()
    file.file.close()
    
    # collection ex) Top, Bottom
    collection = mydb[type]
    metadata_json = makeJsonList(df, type)
    collection.insert_many(metadata_json)
    total_item = collection.count_documents({})
    
    # key - 기본키, 중복된 키 찾기
    duplicates = collection.aggregate([
    {"$group": {"_id": "$key", "count": {"$sum": 1}}},
    {"$match": {"count": {"$gt": 1}}}
        ])
    
    # 중복된 키 제거
    duplication_keys = []
    for duplicate in duplicates:
        key = duplicate['_id']
        duplication_keys.append(key)
        duplicates_to_remove = collection.find({"key": key})
        for duplicate_to_remove in duplicates_to_remove[1:]:
            collection.delete_one({"_id": duplicate_to_remove["_id"]})
            
    # 중복된 키 df에서 제거
    df = df[~df['key'].isin(duplication_keys)]
    
    # 임베딩 저장
    keys = df['key'].to_list()
    paths = df['path'].to_list() # image_path 의미
    
    if len(keys) != 0:
        num_pickles = await database_client.make_pickle(keys, paths)
    else:
        num_pickles = 0
        
    return {
        "등록한 총 상품의 수": total_item,
        "이미 등록된 상품의 수": len(duplication_keys),
        "META DB에 최종 등록된 상품의 수": total_item - len(duplication_keys),
        "생성된 임베딩의 수": num_pickles,
        "최종 저장된 상품의 수와 생성된 임베딩의 수의 차가 0인 경우 정상": total_item - len(duplication_keys) - num_pickles
            }
