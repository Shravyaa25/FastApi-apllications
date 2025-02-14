from sqlalchemy import Column, Integer, ForeignKey, Table
from utils.database import Base

user_book_association = Table(
    "user_books",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("book_id", Integer, ForeignKey("books.id", ondelete="CASCADE"), primary_key=True),
)
