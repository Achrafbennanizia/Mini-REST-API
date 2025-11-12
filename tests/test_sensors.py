from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_sensor_crud():
r = client.post("/sensors", json={"value": 12.34, "unit": "V"})
assert r.status_code == 201
sid = r.json()["id"]

r = client.get(f"/sensors/{sid}")
assert r.status_code == 200
assert r.json()["unit"] == "V"

r = client.get("/sensors?limit=1")
assert r.status_code == 200
assert len(r.json()) >= 1

r = client.delete(f"/sensors/{sid}")
assert r.status_code == 204