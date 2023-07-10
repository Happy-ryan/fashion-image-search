from pydantic import BaseModel

class DbParm(BaseModel):
    keys: list[int]
    paths: list[str]
    