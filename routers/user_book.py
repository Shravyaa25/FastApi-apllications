from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import get_db
from models.user import User
from models.book import Book
from models.user_book import user_book_association

router = APIRouter(prefix="/user-books", tags=["User-Books"])

@router.post("/{user_id}/{book_id}")
def associate_user_book(user_id: int, book_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    book = db.query(Book).filter(Book.id == book_id).first()

    if not user or not book:
        raise HTTPException(status_code=404, detail="User or Book not found")

    user.books.append(book)
    db.commit()
    return {"message": "User and Book associated successfully"}

@router.get("/{user_id}")
def get_user_books(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {"user_id": user_id, "books": [book.id for book in user.books]}