from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_route_api():
    response = client.get("/route?from=Paris&to=Lyon&mode=car")
    assert response.status_code == 200
    data = response.json()
    assert "distance_km" in data
    assert "carbon_footprint_kg" in data
