from typing import List, Optional

from pydantic import BaseModel


class CategorieBase(BaseModel):
    slug: str
    name: str


class CategorieCreate(CategorieBase):
    pass


class Categorie(CategorieBase):
    id: int

    class Config:
        orm_mode = True
