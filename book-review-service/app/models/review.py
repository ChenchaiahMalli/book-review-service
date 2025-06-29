from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    reviewer_name = Column(String)
    content = Column(Text)
    rating = Column(Integer)

    book = relationship("Book", back_populates="reviews")