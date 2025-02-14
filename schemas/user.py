from pydantic import BaseModel
from typing import Optional

class UserRequest(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

class UserResponse(BaseModel):  # Pydantic model for response
    id: int
    name: str
    email: str
    age: Optional[int] = None

    class Config:
        from_attributes = True  # Allows conversion from SQLAlchemy model
