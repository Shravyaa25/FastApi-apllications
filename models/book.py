from sqlalchemy import Column, Integer, String
from utils.database import Base
from models.user_book import user_book_association
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    description = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    published_date = Column(Integer, nullable=False)

    users = relationship("User", secondary=user_book_association, back_populates="books")
