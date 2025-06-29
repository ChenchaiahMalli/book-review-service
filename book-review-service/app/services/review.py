from sqlalchemy.orm import Session
from app import models, schemas

def get_reviews(db: Session, book_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Review)
        .filter(models.Review.book_id == book_id)
        .offset(skip)
        .limit(limit)
        .all()
    )

def create_review(db: Session, book_id: int, review: schemas.ReviewCreate):
    db_review = models.Review(**review.model_dump(), book_id=book_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review