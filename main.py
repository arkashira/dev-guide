# tests/unit/test_progress_api.py
import pytest
from fastapi.testclient import TestClient
from app.main import app  # FastAPI instance

client = TestClient(app)

@pytest.fixture
def auth_headers():
    return {"Authorization": "Bearer fake-jwt-token"}

def test_endpoint_exists(auth_headers):
    resp = client.get("/api/progress", headers=auth_headers)
    assert resp.status_code == 200

def test_progress_structure(auth_headers):
    resp = client.get("/api/progress", headers=auth_headers)
    data = resp.json()
    assert isinstance(data["recommendations"], list)
    for rec in data["recommendations"]:
        assert set(rec.keys()) == {"id", "title", "completedLessons", "totalLessons", "percentage"}
        assert 0 <= rec["percentage"] <= 100

def test_unauthenticated_access():
    resp = client.get("/api/progress")
    assert resp.status_code == 401

def test_invalid_recid(auth_headers):
    resp = client.get("/api/progress/999999", headers=auth_headers)
    assert resp.status_code == 404
    assert resp.json()["error"] == "Recommendation not found"

def test_rate_limit(auth_headers):
    for _ in range(101):
        resp = client.get("/api/progress", headers=auth_headers)
    assert resp.status_code == 429