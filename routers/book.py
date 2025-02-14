from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from services.book_service import BookService
from schemas.book import BookRequest, BookResponse
from models import book as book_model
from utils.database import get_db

router = APIRouter()
book_service = BookService()

# Create a Book
@router.post("/books", response_model=BookResponse)
async def create_book(request: BookRequest, db: Session = Depends(get_db)):
    return book_service.create_book(db, request)

# Read All Books
@router.get("/books", response_model=List[BookResponse])
async def read_all_books(db: Session = Depends(get_db)):
    books = db.query(book_model.Book).all()
    return [BookResponse.model_validate(book) for book in books]

# Read a Single Book by ID
@router.get("/books/{book_id}", response_model=BookResponse)
async def read_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(book_model.Book).filter(book_model.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return BookResponse.model_validate(book)

# Update a Book
@router.put("/books/{book_id}", response_model=BookResponse)
async def update_book(book_id: int, request: BookRequest, db: Session = Depends(get_db)):
    book = db.query(book_model.Book).filter(book_model.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    for key, value in request.dict().items():
        setattr(book, key, value)

    db.commit()
    db.refresh(book)
    return BookResponse.model_validate(book)

# Delete a Book
@router.delete("/books/{book_id}")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(book_model.Book).filter(book_model.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}
