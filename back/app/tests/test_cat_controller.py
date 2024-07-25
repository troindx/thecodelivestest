from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_cat():
    response = client.post("/api/cats/", json={
        "name": "Mittens",
        "age": 3,
        "breed": "Siamese",
        "vaccinations": [{"type": "Rabies", "date": "2024-01-01"}]
    })
    assert response.status_code == 200
    assert response.json() is not None

def test_read_cat():
    response = client.post("/api/cats/", json={
        "name": "Mittens",
        "age": 3,
        "breed": "Siamese",
        "vaccinations": [{"type": "Rabies", "date": "2024-01-01"}]
    })
    cat_id = response.json()
    response = client.get(f"/api/cats/{cat_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Mittens"

def test_update_cat():
    response = client.post("/api/cats/", json={
        "name": "Mittens",
        "age": 3,
        "breed": "Siamese",
        "vaccinations": [{"type": "Rabies", "date": "2024-01-01"}]
    })
    cat_id = response.json()
    response = client.put(f"/api/cats/{cat_id}", json={
        "name": "Whiskers",
        "age": 5,
        "breed": "Sphynx",
        "vaccinations": [{"type": "Rabies", "date": "2024-01-01"}]
    })
    assert response.status_code == 200
    assert response.json() == True

def test_delete_cat():
    response = client.post("/api/cats/", json={
        "name": "Mittens",
        "age": 3,
        "breed": "Siamese",
        "vaccinations": [{"type": "Rabies", "date": "2024-01-01"}]
    })
    cat_id = response.json()
    response = client.delete(f"/api/cats/{cat_id}")
    assert response.status_code == 200
    assert response.json() == True

def test_list_cats():
    response = client.post("/api/cats/", json={
        "name": "Mittens",
        "age": 3,
        "breed": "Siamese",
        "vaccinations": [{"type": "Rabies", "date": "2024-01-01"}]
    })
    response = client.get("/api/cats/")
    assert response.status_code == 200
    assert len(response.json()) > 0
