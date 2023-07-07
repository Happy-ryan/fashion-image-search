from pydantic import BaseModel
from fastapi import UploadFile


class ImageP(BaseModel):
    
    file: UploadFile
    thresh: float
    
    
class TextP(BaseModel):
    
    text: str
    thresh: float


class FilterP(BaseModel):
    
    file: UploadFile
    text: str
    thresh: float