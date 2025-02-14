from sqlalchemy.orm import Session
from models.book import Book
from schemas.book import BookRequest
from fastapi import HTTPException

class BookService:

    def fetch_all_books(self, db: Session):
        return db.query(Book).all()

    def fetch_book_by_id(self, db: Session, book_id: int):
        book = db.query(Book).filter(Book.id == book_id).first()
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return book

    def create_book(self, db: Session, request: BookRequest):
        new_book = Book(**request.dict())
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return new_book
