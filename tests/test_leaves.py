import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_leave():
    # Register and login
    client.post("/api/v1/auth/register", json={
        "name": "Leave User",
        "email": "leaveuser@example.com",
        "password": "leavepass123",
        "role": "Employee"
    })
    login = client.post("/api/v1/auth/login", data={"username": "leaveuser@example.com", "password": "leavepass123"})
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    # Create leave
    response = client.post("/api/v1/leaves/request", json={
        "leave_type": "Annual",
        "start_date": "2025-07-10",
        "end_date": "2025-07-12",
        "comments": "Vacation"
    }, headers=headers)
    assert response.status_code == 200
    assert response.json()["status"] == "Pending"
