from pydantic import BaseModel
from typing import List, Optional

class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    class Config:
        from_attributes = True  # Needed to convert SQLAlchemy models to Pydantic


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None
    rating: int
    

    class Config:
        from_attributes = True  # Ensures compatibility with SQLAlchemy ORM
