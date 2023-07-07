from fastapi import FastAPI
import uvicorn

app = FastAPI()

from routes.embedding import embedding_router

app.include_router(embedding_router, prefix="/embedding")

@app.get("/")
async def servercheck() -> dict:
    return {
        "message": "Embedding server is OK!"
    }
    

if __name__ == "__main__":
    uvicorn.run("embedding:app", port=9000, host="0.0.0.0", reload=False)