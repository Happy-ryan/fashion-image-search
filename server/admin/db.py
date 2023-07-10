from fastapi import FastAPI
import uvicorn

app = FastAPI()

from routes.db import db_router

app.include_router(db_router, prefix="/db")

@app.get("/")
async def servercheck() -> dict:
    return {
            "message": "db server is OK!"
        }
       
        
if __name__ == "__main__":
    uvicorn.run("db:app", port=8003, host="0.0.0.0", reload=True)


