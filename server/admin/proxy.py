from fastapi import FastAPI
import uvicorn
from infra.connection import Setting

app = FastAPI()
setting = Setting()

from routes.proxy import proxy_router

app.include_router(proxy_router, prefix="/proxy")

@app.get("/")
async def servercheck() -> dict:
    return {
        "message": "Proxy server is OK!"
    }


@app.on_event("startup")
async def init_db():
    await setting.initialize_database()


if __name__ == "__main__":
    uvicorn.run("proxy:app", port=8005, host="0.0.0.0", reload=True)
