from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import get_db
from services.user_service import UserService
from schemas.user import UserRequest, UserResponse
from models import user as user_model
from typing import List

router = APIRouter()
user_service = UserService()

# Create User
@router.post("/users", response_model=UserResponse)
async def create_user(request: UserRequest, db: Session = Depends(get_db)):
    user = user_service.create_user(db, request)
    return UserResponse.model_validate(user)

# Read All Users
@router.get("/users", response_model=List[UserResponse])
async def read_all_users(db: Session = Depends(get_db)):
    users = user_service.fetch_all_users(db)
    return [UserResponse.model_validate(user) for user in users]

# Read a Single User by ID
@router.get("/users/{user_id}", response_model=UserResponse)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.model_validate(user)

# Update a User
@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, request: UserRequest, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in request.dict().items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return UserResponse.model_validate(user)

# Delete a User
@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

