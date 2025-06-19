import os
from fastapi.testclient import TestClient

from backend.src.app import app


def test_frontend_served(tmp_path, monkeypatch):
    # Enable demo mode so the frontend is mounted
    monkeypatch.setenv("DEMO_MODE", "true")
    client = TestClient(app)

    response = client.get("/")
    assert response.status_code == 200
    assert "Demo" in response.text


def test_generate_image_demo(monkeypatch):
    monkeypatch.setenv("DEMO_MODE", "true")
    client = TestClient(app)

    response = client.post("/images/generate-image", json={"prompt": "cat"})
    assert response.status_code == 200
    assert response.json()["image_url"].endswith("default.png")
