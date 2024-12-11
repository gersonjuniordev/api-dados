import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bem-vindo à API de Processamento de Dados"}

@pytest.mark.asyncio
async def test_process_data():
    test_data = {
        "data": [
            {"idade": 25, "salario": 5000},
            {"idade": 30, "salario": 6000}
        ],
        "parameters": {}
    }
    
    response = client.post("/api/v1/process", json=test_data)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "result" in response.json() 