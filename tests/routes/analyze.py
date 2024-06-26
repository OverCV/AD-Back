# test_analyze.py

from fastapi.testclient import TestClient
from main import app  # Asegúrate de importar tu aplicación FastAPI aquí

client = TestClient(app)

def test_genetic_strategy():
    response = client.get('/sia-genetic/')
    assert response.status_code == 200
    # Aquí puedes añadir más aserciones para verificar la integridad de los datos devueltos
