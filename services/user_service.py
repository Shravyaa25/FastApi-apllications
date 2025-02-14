from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserRequest
from fastapi import HTTPException

class UserService:

    def fetch_all_users(self, db: Session):
        return db.query(User).all()

    def create_user(self, db: Session, request: UserRequest):
        new_user = User(**request.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
