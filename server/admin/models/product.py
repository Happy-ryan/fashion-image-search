from beanie import Indexed, Document
from typing import Optional
from pydantic import BaseModel


class Category(BaseModel):
    type: Optional[str] = None
    price: Optional[int] = None
    tags: Optional[list[str]] = None
    
    
class Item(Document):
    key: Indexed(int)
    name: str
    link: str
    category: Category = None

    class Config:
        schema_extra = {
            "example":{
                        "key": 11,
                        "name": "yale short pants",
                        "link": "https://www.musinsa.com/app/goods/3180786?loc=goods_rank",
                        "category": {
                            "type": "Top",
                            "price": 10000,
                            "tags": ["반팔", "로고", "명품"]
                        }
                        }}
    
    class Settings:
        name = "products"