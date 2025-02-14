from pydantic import BaseModel

class UserBookBase(BaseModel):
    user_id: int
    book_id: int

class UserBookCreate(UserBookBase):
    pass

class UserBookResponse(UserBookBase):
    class Config:
        orm_mode = True
