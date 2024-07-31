from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_cat():
    response = client.post("/api/cats/", json={
        "name": "Mittens",
        "age": 3,
        "breed": "Siamese",
        "image": "base64EncodedImage",
        "vaccinations": [{"type": "Rabies", "date": "2024-01-01"}]
    })
    assert response.status_code == 200
    assert response.json() is not None

def test_read_cat():
    response = client.post("/api/cats/", json={
        "name": "Mittens",
        "age": 3,
        "breed": "Siamese",
        "image": "base64EncodedImage",
        "vaccinations": [{"type": "Rabies", "date": "2024-01-01"}]
    })
    cat_id = response.json()
    response = client.get(f"/api/cats/{cat_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Mittens"
    assert response.json()["age"] == 3
    assert response.json()["breed"] == "Siamese"
    assert response.json()["image"] == "base64EncodedImage"
    assert response.json()["vaccinations"][0]["type"] == "Rabies"
    assert response.json()["vaccinations"][0]["date"] == "2024-01-01T00:00:00"
    assert response.json()["id"] == cat_id


def test_update_cat():
    response = client.post("/api/cats/", json={
        "name": "Mittens",
        "age": 3,
        "breed": "Siamese",
        "image": "base64EncodedImage",
        "vaccinations": [{"type": "Rabies", "date": "2024-01-01"}]
    })
    cat_id = response.json()
    response = client.put(f"/api/cats/{cat_id}", json={
        "name": "Whiskers",
        "age": 5,
        "breed": "Sphynx",
        "image": "base64EncodedImage",
        "vaccinations": [{"type": "Rabies", "date": "2024-01-01"}]
    })
    assert response.status_code == 200
    assert response.json() == True

def test_delete_cat():
    response = client.post("/api/cats/", json={
        "name": "Mittens",
        "age": 3,
        "breed": "Siamese",
        "image": "base64EncodedImage",
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
        "image": "base64EncodedImage",
        "vaccinations": [{"type": "Rabies", "date": "2024-01-01"}]
    })
    response = client.get("/api/cats/")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["name"] == "Mittens"
    assert response.json()[0]["age"] == 3
    assert response.json()[0]["breed"] == "Siamese"
    assert response.json()[0]["image"] == "base64EncodedImage"
    assert response.json()[0]["vaccinations"][0]["type"] == "Rabies"
    assert response.json()[0]["vaccinations"][0]["date"] == "2024-01-01T00:00:00"
    assert response.json()[0]["id"] is not None
