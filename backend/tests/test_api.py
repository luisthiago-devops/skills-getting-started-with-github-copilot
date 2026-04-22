from fastapi.testclient import TestClient
from {backend_app_module} import app

client = TestClient(app)

def test_openapi_disponivel():
    # Arrange
    endpoint = "/openapi.json"

    # Act
    resp = client.get(endpoint)

    # Assert
    assert resp.status_code == 200
    assert "openapi" in resp.json()
