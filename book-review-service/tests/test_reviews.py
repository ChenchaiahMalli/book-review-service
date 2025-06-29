def test_create_and_get_reviews(client):
    # First create a book
    book_response = client.post(
        "/books/",
        json={"title": "Review Test", "author": "Review Author"},
    )
    book_id = book_response.json()["id"]
    
    # Then add a review
    review_response = client.post(
        f"/books/{book_id}/reviews",
        json={"reviewer_name": "Test Reviewer", "content": "Great book!", "rating": 5},
    )
    assert review_response.status_code == 200
    
    # Then get reviews
    reviews_response = client.get(f"/books/{book_id}/reviews")
    assert reviews_response.status_code == 200
    reviews = reviews_response.json()
    assert len(reviews) == 1
    assert reviews[0]["content"] == "Great book!"