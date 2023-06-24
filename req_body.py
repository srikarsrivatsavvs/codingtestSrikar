from pydantic import BaseModel

class Item(BaseModel):
    repo: str
    email: str 
    token: str