from fastapi import APIRouter, UploadFile, File
from io import StringIO
import pandas as pd

from infra.client import DataBaseClient

from infra.connection import DB
from models.product import Item

proxy_router = APIRouter(
    tags=["Proxy"],
)

database_client = DataBaseClient()
db_crud = DB(Item)

@proxy_router.post('/products-upload')
async def upload(file: UploadFile = File(...)):
    print("여기는 products-upload 라우터 위치다!")

    contents = file.file.read()
    s = str(contents,'utf-8')
    data = StringIO(s)
    df = pd.read_csv(data)
    data.close()
    file.file.close()
    
    keys = df['key'].to_list()[:2]
    paths = df['path'].to_list()[:2]
    links = df['link'].to_list()[:2]
    names = df['name'].to_list()[:2]
    
    print("key는 여기다!!",  keys)
    pickles = await database_client.make_pickle(keys, paths)
    
    datas = []
    for idx in range(len(keys)):
        data = {
            'key': keys[idx],
            'name': names[idx],
            'link': links[idx]
        }
        datas.apped(data)
    
    await db_crud.insert_one(datas[0])
    
    return f"등록하신 상품의 개수는 {len(pickles)} 입니다."
