from fastapi import FastAPI
import uvicorn

app = FastAPI()

# app.include_router(router=, prefix=)

@app.get("/")
async def servercheck() -> dict:
    return {
        "message": "Proxy server is OK!"
    }
    

if __name__ == "__main__":
    uvicorn.run("proxy:app", port=8000, host="0.0.0.0", reload=False)