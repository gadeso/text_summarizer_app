import pytest
from fastapi.testclient import TestClient
from api_model import app

# Crear un cliente de prueba para la aplicación FastAPI
client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Bienvenido a la aplicación de LLM con FastAPI" in response.json()["message"]

def test_query_model():
    response = client.post("/query", json={"text": "¿Cuál es la capital de Francia?"})
    assert response.status_code == 200
    assert "París" in response.json()["response"]

def test_query_model_empty_text():
    response = client.post("/query", json={"text": ""})
    assert response.status_code == 200
    assert response.json()["response"] != ""  # Assuming the model always generates some response

def test_query_model_invalid_payload():
    response = client.post("/query", json={})
    assert response.status_code == 422  # Unprocessable Entity for missing 'text' field

if __name__ == "__main__":
    pytest.main()
