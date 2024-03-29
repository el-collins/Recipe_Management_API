from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_nutritional_info():
    response = client.get("/nutritional-info")
    assert response.status_code == 200
    assert response.json() == []

def test_get_recipe_nutritional_info_not_found():
    response = client.get("/nutritional-info/1")
    assert response.status_code == 404

def test_calculate_and_store_nutritional_info():
    response = client.post("/nutritional-info/1")
    assert response.status_code == 200
    nutritional_info = response.json()
    assert nutritional_info["calories"] == 500
    assert nutritional_info["fat"] == 20
    assert nutritional_info["protein"] == 30
    assert nutritional_info["carbohydrates"] == 50

