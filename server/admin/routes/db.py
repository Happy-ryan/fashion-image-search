from fastapi import APIRouter, File, UploadFile, Response, Form
from typing import Annotated

from infra.model import DataBase
from models.db import DbParm

db_router = APIRouter(
    tags=["DB"]
)

db = DataBase(config_path="../config.yaml")

@db_router.post("/make-pickle")
async def make_pickle(parm: DbParm) -> dict:
    pickles = db.MakePickle(parm.keys, parm.paths)

    return {
        "msg": "pickle 저장 성공!",
        "pickles": pickles
    }
