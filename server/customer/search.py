from fastapi import FastAPI
import uvicorn

app = FastAPI()

from routes.search import search_router

app.include_router(search_router, prefix="/search")

@app.get("/")
async def servercheck() -> dict:
    return {
        "message": "Search server is OK!"
    }
    

if __name__ == "__main__":
    uvicorn.run("search:app", port=9001, host="0.0.0.0", reload=False)