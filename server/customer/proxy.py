from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from routes.proxy import proxy_router

app.include_router(proxy_router, prefix="/proxy")

@app.get("/")
async def servercheck() -> dict:
    return {
        "message": "Proxy server is OK!"
    }
    

if __name__ == "__main__":
    uvicorn.run("proxy:app", port=30007, host="0.0.0.0", reload=False)
