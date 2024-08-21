from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
    
def test_receive_data():
    data = [{"id": 1, "value": 10.5, "timestamp": "2024-08-13T00:00:00"}]  # Corrected field name
    response = client.post("/data", json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "Data received successfully", "data_count": 1}

