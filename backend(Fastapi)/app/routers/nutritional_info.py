from fastapi import APIRouter, HTTPException
from typing import List
from app.models import NutritionalInfo

router = APIRouter()

# Dummy data to simulate database
nutritional_info_db = []

@router.get("/nutritional-info", response_model=List[NutritionalInfo])
async def get_nutritional_info():
    """
    Get all nutritional information.

    Retrieves a list of all nutritional information entries from the database.
    """
    return nutritional_info_db

@router.get("/nutritional-info/{recipe_id}", response_model=NutritionalInfo)
async def get_recipe_nutritional_info(recipe_id: int):
    """
    Get nutritional information by recipe ID.

    Retrieves the nutritional information for a specific recipe ID from the database.

    Args:
        recipe_id (int): The ID of the recipe to retrieve nutritional information for.

    Raises:
        HTTPException: If the nutritional information for the specified recipe ID is not found.
    """
    if recipe_id < len(nutritional_info_db):
        return nutritional_info_db[recipe_id]
    else:
        raise HTTPException(status_code=404, detail="Nutritional info not found")

@router.post("/nutritional-info/{recipe_id}", response_model=NutritionalInfo)
async def calculate_and_store_nutritional_info(recipe_id: int):
    """
    Calculate and store nutritional information for a recipe.

    Args:
        recipe_id (int): The ID of the recipe to calculate and store nutritional information for.

    Returns:
        NutritionalInfo: The calculated and stored nutritional information.

  
    """
    nutritional_info = NutritionalInfo(calories=500, fat=20, protein=30, carbohydrates=50)
    nutritional_info_db.append(nutritional_info)
    return nutritional_info

# Additional endpoints for updating and deleting nutritional information can be added here
