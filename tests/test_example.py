import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/api/v1/items", json={"name": "Test Item", "description": "This is a test item"})
    assert response.status_code == 200
    assert "id" in response.json()

def test_list_items():
    response = client.get("/api/v1/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)