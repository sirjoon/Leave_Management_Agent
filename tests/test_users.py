import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_rbac_enforcement():
    # Register manager
    client.post("/api/v1/auth/register", json={
        "name": "Manager",
        "email": "manager@example.com",
        "password": "managerpass",
        "role": "Manager"
    })
    # Register employee
    client.post("/api/v1/auth/register", json={
        "name": "Employee",
        "email": "employee@example.com",
        "password": "employeepass",
        "role": "Employee"
    })
    # Login as employee
    login = client.post("/api/v1/auth/login", data={"username": "employee@example.com", "password": "employeepass"})
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    # Try to approve leave as employee (should fail)
    response = client.post("/api/v1/leaves/approve/1", headers=headers)
    assert response.status_code in (401, 403, 404)
