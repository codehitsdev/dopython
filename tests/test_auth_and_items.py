from fastapi.testclient import TestClient
import app as app_module

client = TestClient(app_module.app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
