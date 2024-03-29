from fastapi import APIRouter, HTTPException, Path
from typing import List, Annotated
from app.models import Recipe

router = APIRouter()

# Dummy data to simulate database
recipes_db = []


@router.get(
    "/recipes",
    response_model=List[Recipe],
    summary="Get All Recipes",
    description="Retrieve a list of all recipes including their ingredients, instructions, and nutritional information.",
    tags=["Recipes"],
)
async def get_recipes():
    """
    Get a list of all the recipes available in the database.

    Retrieve all recipes along with their details from the database.
    """
    return recipes_db


# Get recipe by id
@router.get("/recipes/{recipe_id}", response_model=Recipe)
async def get_recipe(
    recipe_id: Annotated[
        int,
        Path(
            title="The ID of the item to get", description="The ID of the item to get"
        ),
    ]
):
    """
    Get a specific recipe by ID.

    Retrieve the recipe details for a specific recipe ID from the database.
    """
    for recipe in recipes_db:
        if recipe.id == recipe_id:
            return recipe
    raise HTTPException(status_code=404, detail="Recipe not found")


@router.post(
    "/recipes",
    response_model=Recipe,
    summary="Create new recipe",
)
async def create_recipe(recipe: Recipe):
    """
    Create a new recipe.

    Add a new recipe to the database.
    """
    # global recipe_id_counter
    # recipe_id_counter += 1  # Increment the counter for each new recipe
    # recipe.id = recipe_id_counter  # Assign the generated ID to the recipe
    # recipes_db.append(recipe)
    # return recipe
    recipes_db.append(recipe)
    return recipe


@router.put("/recipes/{recipe_id}", response_model=Recipe)
async def update_recipe(recipe_id: Annotated[int, Path(description="The ID of the item to delete")],
    recipe: Recipe,):
    """
    Update a recipe by ID.

    Update the details of a recipe with the given ID in the database.
    """
    for index, db_recipe in enumerate(recipes_db):
        if db_recipe.id == recipe_id:
            recipes_db[index] = recipe
            return recipe
    raise HTTPException(status_code=404, detail="Recipe not found")


@router.delete("/recipes/{recipe_id}")
async def delete_recipe(
    recipe_id: Annotated[int, Path(description="The ID of the item to delete")]
):
    """
    Delete a recipe by ID.

    Remove a recipe with the specified ID from the database.
    """
    for index, recipe in enumerate(recipes_db):
        if recipe.id == recipe_id:
            del recipes_db[index]
            return recipe
    raise HTTPException(status_code=404, detail="Recipe not found")

    
    # if recipe_id < len(recipes_db):
    #     del recipes_db[recipe_id]
    #     return {"message": "Recipe deleted successfully"}
    # else:
    #     raise HTTPException(status_code=404, detail="Recipe not found")
