from pydantic import BaseModel

class Category(BaseModel):
    name: str
    color: str
    icon: str

class CategoryOut(Category):
    id: str