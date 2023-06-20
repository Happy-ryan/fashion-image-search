from fastapi import FastAPI
import uvicorn

app = FastAPI()

# app.include_router(router=, prefix=)

@app.get("/")
async def servercheck() -> dict:
    return {
        "message": "Search server is OK!"
    }
    

if __name__ == "__main__":
    uvicorn.run("embedding:app", port=9001, host="0.0.0.0", reload=False)