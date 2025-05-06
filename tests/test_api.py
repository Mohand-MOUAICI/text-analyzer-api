from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_route_api():
    response = client.get("/route?from_city=Paris&to_city=Lyon&mode=car")
    assert response.status_code == 200
    data = response.json()
    assert "distance_km" in data
    assert "carbon_footprint_kg" in data

def test_summarize():
    response = client.post("/summarize", json={"text": "FastAPI is a modern web framework for building APIs."})
    assert response.status_code == 200
    assert "summary" in response.json()

def test_sentiment():
    response = client.post("/sentiment", json={"text": "I love this product!"})
    assert response.status_code == 200
    assert "sentiment" in response.json()

def test_entities():
    response = client.post("/entities", json={"text": "Elon Musk founded SpaceX."})
    assert response.status_code == 200
    entities = response.json().get("entities")
    assert any(ent["label"] == "PERSON" for ent in entities)
