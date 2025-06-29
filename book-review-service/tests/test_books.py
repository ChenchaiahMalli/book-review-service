def test_create_book(client):
    response = client.post(
        "/books/",
        json={"title": "Test Book", "author": "Test Author", "description": "Test Description"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Book"
    assert "id" in data

def test_read_books(client):
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)