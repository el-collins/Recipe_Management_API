from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)



def test_get_recipes():
    response = client.get("/recipes")
    assert response.status_code == 200
    assert response.json() == []

def test_get_recipe_not_found():
    response = client.get("/recipes/1")
    assert response.status_code == 404

def test_create_recipe():
    # Test creating a recipe
    recipe_data = {
        "title": "Test Recipe",
        "description": "Test description",
        "instructions": "Test instructions",
        "ingredients": [
            {"name": "Test Ingredient", "quantity": "100"}
        ],
        "nutritional_info": {
            "calories": 100,
            "fat": 10,
            "protein": 5,
            "carbohydrates": 15
        }
    }
    response = client.post("/recipes", json=recipe_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Test Recipe"

def test_update_recipe_not_found():
    # Test updating a recipe that does not exist
    updated_recipe_data = {
        "title": "Updated Test Recipe",
        "description": "Updated test description",
        "instructions": "Updated test instructions",
        "ingredients": [
            {"name": "Updated Test Ingredient", "quantity": "150"}
        ],
        "nutritional_info": {
            "calories": 150,
            "fat": 15,
            "protein": 8,
            "carbohydrates": 20
        }
    }
    response = client.put("/recipes/1000", json=updated_recipe_data)  # Using a non-existent recipe ID
    assert response.status_code == 404

def test_delete_recipe_not_found():
    response = client.delete("/recipes/1")
    assert response.status_code == 404

def test_get_ingredients():
    response = client.get("/ingredients")
    assert response.status_code == 200
    assert response.json() == []

def test_get_ingredient_not_found():
    response = client.get("/ingredients/1")
    assert response.status_code == 404

def test_create_ingredient():
    ingredient_data = {
        "name": "Test Ingredient",
        "quantity": "100g"
    }
    response = client.post("/ingredients", json=ingredient_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Ingredient"

def test_update_ingredient_not_found():
    updated_ingredient_data = {
        "name": "Updated Test Ingredient",
        "quantity": "150g"
    }
    response = client.put("/ingredients/1", json=updated_ingredient_data)
    assert response.status_code == 404

def test_delete_ingredient_not_found():
    response = client.delete("/ingredients/1")
    assert response.status_code == 404

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

