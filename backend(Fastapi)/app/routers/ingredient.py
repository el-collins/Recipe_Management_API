from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Ingredient

router = APIRouter(prefix="/api")

# Dummy data to simulate database
ingredients_db = []

@router.get("/ingredients", response_model=List[Ingredient], tags=["Ingredients"])
async def get_ingredients():
    """
    Retrieve a list of all ingredients.

    Returns:
        List[Ingredient]: A list of Ingredient objects.
    """
    return ingredients_db

@router.get("/ingredients/{ingredient_id}", response_model=Ingredient, tags=["Ingredients"])
async def get_ingredient(ingredient_id: int):
    """
    Retrieve an ingredient by ID.

    Args:
        ingredient_id (int): The ID of the ingredient to retrieve.

    Returns:
        Ingredient: The Ingredient object with the specified ID.

    Raises:
        HTTPException: If the ingredient with the given ID does not exist.
    """
    if ingredient_id < len(ingredients_db):
        return ingredients_db[ingredient_id]
    else:
        raise HTTPException(status_code=404, detail="Ingredient not found")



@router.post("/ingredients", response_model=Ingredient, tags=["Ingredients"])
async def create_ingredient(ingredient: Ingredient):
    """
    Create a new ingredient.

    Args:
        ingredient (Ingredient): The new ingredient to create.

    Returns:
        Ingredient: The created Ingredient object.
    """
    ingredients_db.append(ingredient)
    return ingredient

@router.put("/ingredients/{ingredient_id}", response_model=Ingredient, tags=["Ingredients"])
async def update_ingredient(ingredient_id: int, ingredient: Ingredient):
    """
    Update an existing ingredient by ID.

    Args:
        ingredient_id (int): The ID of the ingredient to update.
        ingredient (Ingredient): The updated ingredient data.

    Returns:
        Ingredient: The updated Ingredient object.

    Raises:
        HTTPException: If the ingredient with the given ID does not exist.
    """
    if ingredient_id < len(ingredients_db):
        ingredients_db[ingredient_id] = ingredient
        return ingredient
    else:
        raise HTTPException(status_code=404, detail="Ingredient not found")


@router.delete("/ingredients/{ingredient_id}", tags=["Ingredients"])
async def delete_ingredient(ingredient_id: int):
    """
    Deletes an ingredient from the database.

    Parameters:
        ingredient_id (int): The ID of the ingredient to delete.

    Returns:
        dict: A message indicating the success of the deletion operation.

    Raises:
        HTTPException: If the ingredient with the specified ID is not found.
    """
    if ingredient_id < len(ingredients_db):
        del ingredients_db[ingredient_id]
        return {"message": "Ingredient deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Ingredient not found")
