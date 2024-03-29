from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test cases for /recipes endpoints
def test_get_recipes():
    response = client.get("/api/recipes")
    assert response.status_code == 200
    assert response.json() == []

def test_get_recipe_not_found():
    response = client.get("/api/recipes/1")
    assert response.status_code == 404

def test_create_recipe():
    recipe_data = {
        "title": "Test Recipe",
        "description": "Test description",
        "instructions": "Test instructions",
        "ingredients": [{"name": "Test Ingredient", "quantity": "100g"}],
        "nutritional_info": {
            "calories": 100,
            "fat": 10,
            "protein": 5,
            "carbohydrates": 15
        }
    }
    response = client.post("/api/recipes", json=recipe_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Test Recipe"

def test_update_recipe_not_found():
    updated_recipe_data = {
        "title": "Updated Test Recipe",
        "description": "Updated test description",
        "instructions": "Updated test instructions",
        "ingredients": [{"name": "Updated Test Ingredient", "quantity": "150g"}],
        "nutritional_info": {
            "calories": 150,
            "fat": 15,
            "protein": 8,
            "carbohydrates": 20
        }
    }
    response = client.put("/api/recipes/1000", json=updated_recipe_data)  # Non-existent ID
    assert response.status_code == 404

def test_delete_recipe_not_found():
    response = client.delete("/api/recipes/1")
    assert response.status_code == 404

# Test cases for /ingredients endpoints
# Add similar tests for other endpoints

# Test case for getting all ingredients
def test_get_ingredients():
    response = client.get("/api/ingredients")
    assert response.status_code == 200
    assert response.json() == []

# Test case for getting a specific ingredient that doesn't exist
def test_get_ingredient_not_found():
    response = client.get("/api/ingredients/1")
    assert response.status_code == 404

# Test case for creating an ingredient
def test_create_ingredient():
    ingredient_data = {"name": "Test Ingredient", "quantity": "100g"}
    response = client.post("/api/ingredients", json=ingredient_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Ingredient"

# Test case for updating an ingredient that doesn't exist
def test_update_ingredient_not_found():
    updated_ingredient_data = {"name": "Updated Test Ingredient", "quantity": "150g"}
    response = client.put("/api/ingredients/1", json=updated_ingredient_data)
    assert response.status_code == 404

# Test case for deleting an ingredient that doesn't exist
def test_delete_ingredient_not_found():
    response = client.delete("/api/ingredients/1")
    assert response.status_code == 404

# Add test cases for other endpoints as needed
