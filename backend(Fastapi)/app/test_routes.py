from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_recipe():
    new_recipe = {
  "id": 0,
  "title": "Test Recipe",
  "description": "This is a test recipe",
  "instructions": "Test instructions",
  "ingredients": [
    {
      "name": "Ingredient 1",
      "quantity": "100g"
    },
    {
      "name": "Ingredient 2",
      "quantity": "200g"
    }
  ],
  "nutritional_info": {
    "calories": 300,
    "fat": 10,
    "protein": 20,
    "carbohydrates": 30
  }
}
    response = client.post("/api/recipes", json=new_recipe)
    assert response.status_code == 200
    assert response.json()["title"] == "Test Recipe"



async def test_get_recipes():
    response = client.get("/api/recipes")
    assert response.status_code == 200
    assert len(response.json()) > 0



async def test_get_recipe_by_id():
    response = client.get("/api/recipes/4")
    assert response.status_code == 200
    assert response.json()["id"] == 1



async def test_update_recipe():
    updated_recipe = {
  "id": 4,
  "title": "Helllo here",
  "description": "string",
  "instructions": "string",
  "ingredients": [
    {
      "name": "string",
      "quantity": "string"
    }
  ],
  "nutritional_info": {
    "calories": 0,
    "fat": 0,
    "protein": 0,
    "carbohydrates": 0
  }
}
    response = client.put("/api/recipes/1", json=updated_recipe)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Recipe"


async def test_delete_recipe():
    response = client.delete("/api/recipes/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Deleted recipe with id 1"
