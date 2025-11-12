from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_list_tasks():
r = client.post("/tasks", json={"title": "Test"})
assert r.status_code == 201
tid = r.json()["id"]

r = client.get("/tasks")
assert r.status_code == 200
assert any(t["id"] == tid for t in r.json())

r = client.put(f"/tasks/{tid}", json={"done": True})
assert r.status_code == 200
assert r.json()["done"] is True

r = client.delete(f"/tasks/{tid}")
assert r.status_code == 204