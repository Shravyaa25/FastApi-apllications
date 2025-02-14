from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from utils.database import Base
from models.user_book import user_book_association


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    age = Column(Integer, nullable=False)

    addresses = relationship("Address", back_populates="user", cascade="all, delete")
    books = relationship("Book", secondary=user_book_association, back_populates="users")