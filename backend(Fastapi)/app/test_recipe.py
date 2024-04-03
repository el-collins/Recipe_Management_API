import pytest # type: ignore
from httpx import AsyncClient # type: ignore
from app.main import app


@pytest.mark.asyncio(scope="module")
async def test_get_all_recipes():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as client:
        response = await client.get("/api/recipes")
        assert response.status_code == 200
        assert len(response.json()) > 0


@pytest.mark.asyncio(scope="module")
async def test_get_recipe_by_id():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as client:
        recipe_id = 1
        response = await client.get(f"/api/recipes/{recipe_id}")
        assert response.status_code == 200
        assert response.json()["id"] == recipe_id

        # Test case for recipe not found
        invalid_recipe_id = 9999
        response = await client.get(f"/api/recipes/{invalid_recipe_id}")
        assert response.status_code == 404


@pytest.mark.asyncio(scope="module")
async def test_create_recipe():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as client:
        # Create a new recipe
        new_recipe_data = {
            "id": 0,
            "title": "Test Recipe",
            "description": "Test Description",
            "instructions": "Test Instructions",
            "ingredients": [{"name": "Ingredient 1", "quantity": "1 unit"}],
            "nutritional_info": {
                "calories": 100,
                "fat": 10,
                "protein": 5,
                "carbohydrates": 20,
            },
        }
        response = await client.post("/api/recipes", json=new_recipe_data)
        assert response.status_code == 200
        assert response.json()["title"] == new_recipe_data["title"]


@pytest.mark.asyncio(scope="module")
async def test_update_recipe():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as client:
        recipe_id = 4
        updated_recipe_data = {
            "id": 0,
            "title": "Updated Recipe Title",
            "description": "Updated Recipe Description",
            "instructions": "Updated Recipe Instructions",
            "ingredients": [{"name": "Updated Ingredient", "quantity": "2 units"}],
            "nutritional_info": {
                "calories": 200,
                "fat": 20,
                "protein": 10,
                "carbohydrates": 30,
            },
        }
        response = await client.put(
            f"/api/recipes/{recipe_id}", json=updated_recipe_data
        )
        assert response.status_code == 200
        assert response.json()["title"] == updated_recipe_data["title"]

        # Test case for recipe not found
        invalid_recipe_id = 9999
        response = await client.put(
            f"/api/recipes/{invalid_recipe_id}", json=updated_recipe_data
        )
        assert response.status_code == 404


@pytest.mark.asyncio(scope="module")
async def test_delete_recipe():
    async with AsyncClient(app=app, base_url="http://test") as client:
        recipe_id = 4  
        response = await client.delete(f"/api/recipes/{recipe_id}")
        assert response.status_code == 200
        assert response.json()["message"] == f"Deleted recipe with id {recipe_id}"

        # Test case for recipe not found
        invalid_recipe_id = 9999
        response = await client.delete(f"/api/recipes/{invalid_recipe_id}")
        assert response.status_code == 404