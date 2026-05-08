from fastapi.testclient import TestClient
from app.main import app


def test_inventory_endpoint() -> None:
    client = TestClient(app)
    response = client.get("/api/v1/inventory?page=1&page_size=20")
    assert response.status_code == 200
    body = response.json()
    assert body["total"] >= 1
    assert {"sku", "quantity", "warehouse"}.issubset(body["items"][0].keys())
