from pydantic import BaseModel

class ReviewBase(BaseModel):
    reviewer_name: str
    content: str
    rating: int

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    book_id: int

    class Config:
        from_attributes = True