from fastapi import APIRouter, UploadFile, File, Form
from io import StringIO
import pandas as pd

from infra.build.client import BuildClient
from infra.meta.client import MetaClient

proxy_router = APIRouter(
    tags=["Proxy"],
)

build_client = BuildClient()
meta_client = MetaClient(collection_name="products", config_path="../config.yaml")

@proxy_router.post('/products-upload')
async def upload(file: UploadFile = File(...)):
    # csv 읽기
    contents = file.file.read()
    s = str(contents,'utf-8')
    data = StringIO(s)
    df = pd.read_csv(data)
    # key에 대해서 중복제거
    df = df.drop_duplicates(subset=["key"])
    data.close()
    file.file.close()
    
    num_inserted_items, num_modified_items = meta_client.insert(df)
    num_total_items = meta_client.num_total_items()
    
    # 임베딩 저장
    keys = df['key'].to_list()
    paths = df['path'].to_list() # image_path 의미
    
    if len(keys) != 0:
        num_pickles = await build_client.make_pickle(keys, paths)
    else:
        num_pickles = 0
        
    return {
        "등록한 총 상품의 수": num_total_items,
        "추가된 상품의 수": num_inserted_items,
        "수정된 상품의 수": num_modified_items,
        "생성된 임베딩의 수": num_pickles,
        "최종 저장된 상품의 수와 생성된 임베딩의 수의 차가 0인 경우 정상": num_inserted_items + num_modified_items - num_pickles
    }
