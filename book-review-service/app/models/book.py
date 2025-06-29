from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    description = Column(String, nullable=True)

    reviews = relationship("Review", back_populates="book")