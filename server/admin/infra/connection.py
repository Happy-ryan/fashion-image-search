from beanie import init_beanie, Document
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
from pydantic import BaseSettings

from models.product import Item


class Setting(BaseSettings):
    DATABASE_URL = Optional[str] = None
    
    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(),
                        document_models=[Item])
        
    class Config:
        env_file = ".env"
        
        
class DB:
    def __init__(self, model):
        self.model = model
        

    async def insert_one(self, document) -> None:
        await self.model.insert_one(document)
        return
    
    
    async def insert_many(self, documents: list[Document]) -> None:
        await self.model.insert_many(documents)
        return
    
    