from pydantic import BaseModel
from datetime import date
class Category(BaseModel):
    name: str
    description:str
    img:str
    date:date
    status:bool
    location:str
    members: list