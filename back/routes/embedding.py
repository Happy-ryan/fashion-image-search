'''
proxy server의 역할
1) embedding server에 embedding 요청 -> embedding model과 client 요청 필요
2) search server(faiss)에 search 요청 -> embedding model과 client 요청 필요
3) meta_db에 search 요청 -> 몽고db연결 -> connection.py 작성
'''

from fastapi import APIRouter, File, UploadFile
import uuid
import os
import httpx

proxy_router = APIRouter(
    tags=["Proxy"],
)

@proxy_router.post("/search-by-image")
async def search_by_image(file: UploadFile) -> dict:
    # -- input_image를 storage/queries 저장
    UPLOAD_DIR = "storage/queries"
    
    content = await file.read()
    rid = str(uuid.uuid4())
    filname = f"{rid}.png" # --uuid로 유니크한 파일명으로 변경(중복방지)
    with open(os.path.join(UPLOAD_DIR, filname), "wb") as fp:
        fp.write(content) # -- 서버 로컬스토리지에 이미지 저장
        
    
    return {
        "msg": "OK"
    }