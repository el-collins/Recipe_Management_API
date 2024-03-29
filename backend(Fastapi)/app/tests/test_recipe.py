from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_recipes():
    response = client.get("/recipes")
    assert response.status_code == 200
    assert response.json() == []


def test_get_recipe():
    # Assuming there's a recipe with ID 1 in the database
    response = client.get("/recipes/1")
    assert response.status_code == 404  # Assuming the recipe with ID 1 doesn't exist


def test_create_recipe():
    recipe_data = {
        "title": "Test Recipe",
        "description": "Test description",
        "instructions": "Test instructions",
        "ingredients": [{"name": "Ingredient 1", "quantity": "100g"}],
        "nutritional_info": {
            "calories": 100,
            "fat": 10,
            "protein": 5,
            "carbohydrates": 20,
        },
    }
    response = client.post("/recipes", json=recipe_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Test Recipe"


def test_update_recipe():
    # Assuming there's a recipe with ID 1 in the database
    updated_recipe_data = {
        "title": "Updated Test Recipe",
        "description": "Updated test description",
        "instructions": "Updated test instructions",
        "ingredients": [{"name": "Updated Ingredient 1", "quantity": "150g"}],
        "nutritional_info": {
            "calories": 150,
            "fat": 15,
            "protein": 8,
            "carbohydrates": 25,
        },
    }
    response = client.put("/recipes/1", json=updated_recipe_data)
    assert response.status_code == 404  # Assuming the recipe with ID 1 doesn't exist


def test_delete_recipe():
    # Assuming there's a recipe with ID 1 in the database
    response = client.delete("/recipes/1")
    assert response.status_code == 404  # Assuming the recipe with ID 1 doesn't exist
