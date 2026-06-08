import os
import sys
from fastapi.testclient import TestClient

# Ensure the assignment package path is importable when tests run from repo root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from starter_code import app

client = TestClient(app)


def test_list_items():
    r = client.get("/items")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


def test_create_item():
    payload = {"id": 0, "name": "Test Item", "description": "Created by test", "price": 3.14}
    r = client.post("/items", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["name"] == "Test Item"
    assert "id" in data
