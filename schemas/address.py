from pydantic import BaseModel

class AddressBase(BaseModel):
    street: str
    city: str
    state: str

class AddressCreate(AddressBase):
    user_id: int  

class AddressResponse(AddressBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
