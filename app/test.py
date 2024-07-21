import pytest
from fastapi.testclient import TestClient
from api_model import app

client = TestClient(app)

def test_query_model():
    # Consulta al modelo
    response = client.post("/query", json={"response": "¿Cuál es la capital de Francia?"})
    assert response.status_code == 200
    assert "response" in response.json()
    assert response.json()["response"] != ""

def test_invalid_endpoint():
    # Consulta a un endpoint no existente
    response = client.get("/n")
    assert response.status_code == 404
