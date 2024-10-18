import pytest
from fastapi.testclient import TestClient
from main import app  # Importa tu aplicación FastAPI

client = TestClient(app)

def test_pyphi_strategy():
    response = client.get(
        "/analyze/sia-pyphi/",
        params={
            "title": "R5A",
            "istate": "10000",
            "subsys": "11100",
            "effect": "11111",
            "actual": "11111",
            "dual": "false"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "DATA" in data  # Reemplaza con la estructura esperada de tu respuesta
