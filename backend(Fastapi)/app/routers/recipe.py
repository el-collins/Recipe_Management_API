from fastapi import APIRouter, HTTPException, Path
from typing import List, Annotated
from app.models import Recipe
from app.database import fetch_all_recipes, fetch_one_recipe, create_new_recipe, update_existing_recipe, remove_recipe


router = APIRouter(prefix="/api")


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
    response = await fetch_all_recipes()
    return response


# Get recipe by id
@router.get("/recipes/{recipe_id}", response_model=Recipe, tags=["Recipes"])
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
    response =  await fetch_one_recipe(recipe_id)
    if not response:
        raise HTTPException(status_code=404, detail="Item not found")
    return response
 

@router.post(
    "/recipes",
    response_model=Recipe,
    summary="Create new recipe", tags=["Recipes"]
)
async def create_recipe(recipe: Recipe):
    """
    Create a new recipe.

    Add a new recipe to the database.
    """
    lowercase_recipe = {k.lower(): v for k, v in recipe.dict().items()}
    response = await create_new_recipe(lowercase_recipe)
    if response:
        print(f"successfully created recipe: {response}")
        return response
    raise HTTPException(400, "Something went wrong")

# UPDATE
@router.put("/recipes/{recipe_id}", response_model=Recipe, tags=["Recipes"])
async def update_recipe(recipe_id: Annotated[int, Path(description="The ID of the item to delete")],
    recipe: Recipe,):
    """
    Update a recipe by ID.

    Update the details of a recipe with the given ID in the database.
    """
    response = await update_existing_recipe(recipe_id, recipe)
    if response:
        return response
    raise HTTPException(status_code=404, detail="Recipe not found")


@router.delete("/recipes/{recipe_id}", tags=["Recipes"])
async def delete_recipe(
    recipe_id: Annotated[int, Path(description="The ID of the item to delete")]
):
    """
    Delete a recipe by ID.

    Remove a recipe with the specified ID from the database.
    """
    response = await remove_recipe(recipe_id)
    if response:
        return {"message": f"Deleted recipe with id {recipe_id}"}
    raise HTTPException(status_code=404, detail="Recipe not found")

    