from fastapi.testclient import TestClient
from app import app
import json

client = TestClient(app)

def test_root():
    response_auth = client.get("/")
    assert response_auth.status_code == 200
    
def test_some_post():
    data = {"id": "2"}
    response_auth = client.post("/predict",
                           headers={"X-Token": "coneofsilence"},
                           json=data)
    assert response_auth.status_code == 200 
    assert response_auth.json()["predictions"] == "{'weighted_similarity': {1: 1.7320508075688767, 2: 0.7071067811865475}}"