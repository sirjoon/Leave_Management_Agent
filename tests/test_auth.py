import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_and_login():
    # Register
    response = client.post("/api/v1/auth/register", json={
        "name": "Test User",
        "email": "testuser@example.com",
        "password": "testpass123",
        "role": "Employee"
    })
    assert response.status_code == 200
    # Login
    response = client.post("/api/v1/auth/login", data={"username": "testuser@example.com", "password": "testpass123"})
    assert response.status_code == 200
    assert "access_token" in response.json()
