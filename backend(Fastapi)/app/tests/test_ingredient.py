from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_get_ingredients():
    response = client.get("/ingredients")
    assert response.status_code == 200
    assert response.json() == []

def test_get_ingredient():
    # Assuming there's an ingredient with ID 1 in the database
    response = client.get("/ingredients/1")
    assert response.status_code == 404  # Assuming the ingredient with ID 1 doesn't exist
    # Add more tests after adding data to the database

def test_create_ingredient():
    ingredient_data = {
        "name": "Test Ingredient",
        "quantity": "100g"
    }
    response = client.post("/ingredients", json=ingredient_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Ingredient"
    # Add more assertions after adding data to the database

def test_update_ingredient():
    # Assuming there's an ingredient with ID 1 in the database
    updated_ingredient_data = {
        "name": "Updated Test Ingredient",
        "quantity": "150g"
    }
    response = client.put("/ingredients/1", json=updated_ingredient_data)
    assert response.status_code == 404  # Assuming the ingredient with ID 1 doesn't exist
    # Add more tests after adding data to the database

def test_delete_ingredient():
    # Assuming there's an ingredient with ID 1 in the database
    response = client.delete("/ingredients/1")
    assert response.status_code == 404  # Assuming the ingredient with ID 1 doesn't exist
    # Add more tests after adding data to the database
