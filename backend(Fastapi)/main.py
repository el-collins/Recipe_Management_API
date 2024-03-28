from typing import List, Annotated
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# CORS (Cross-Origin Resource Sharing) Middleware configuration
origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Fake database
recipes = [
  {
    "id": 1,
    "title": "Classic Caesar Salad",
    "ingredients": [
      {"name": "Romaine Lettuce", "quantity": "3 cups"},
      {"name": "Croutons", "quantity": "1 cup"},
      {"name": "Parmesan Cheese", "quantity": "1/2 cup"},
      {"name": "Caesar Dressing", "quantity": "1/3 cup"}
    ],
    "instructions": "Toss the lettuce, croutons, and parmesan cheese with Caesar dressing. Serve chilled.",
    "nutritional_info": {
      "calories": 250,
      "fat": 15,
      "protein": 7,
      "carbohydrates": 22
    }
  },
  {
    "id": 2,
    "title": "Vegan Chocolate Cake",
    "ingredients": [
      {"name": "All-purpose Flour", "quantity": "2 cups"},
      {"name": "Cocoa Powder", "quantity": "3/4 cup"},
      {"name": "Baking Soda", "quantity": "1 teaspoon"},
      {"name": "Sugar", "quantity": "1 cup"},
      {"name": "Vanilla Extract", "quantity": "2 teaspoons"}
    ],
    "instructions": "Mix dry ingredients, add wet ingredients, and bake at 350°F for 35 minutes.",
    "nutritional_info": {
      "calories": 450,
      "fat": 14,
      "protein": 6,
      "carbohydrates": 77
    }
  }
]


# results = [
#             recipe for recipe in results if "Quinoa and Black Bean Salad" in recipe
#         ]
# print(results)


# Models
class NutritionalInfo(BaseModel):
    calories: float | None = Field(default=None, gt=0, description="Calories in kcal")
    fat: float | None = Field(default=None, gt=0, description="Fat in grams")
    protein: float | None = Field(default=None, gt=0, description="Protein in grams")
    carbohydrates: float | None = Field(
        default=None, gt=0, description="Carbohydrates in grams"
    )


class Ingredient(BaseModel):
    name: str = Field(..., description="Name of the ingredient")
    quantity: str = Field(..., description="Quantity of the ingredient")


class Recipe(BaseModel):
    id: int
    title: str = Field(..., description="Title of the recipe")
    ingredients: List[Ingredient] = Field(..., description="List of ingredients")
    instructions: str = Field(..., description="Cooking instructions")
    nutritional_info: NutritionalInfo = Field(
        ..., description="Nutritional information"
    )


# Endpoints


@app.post("/recipes/", response_model=Recipe)
async def create_recipe(recipe: Recipe):
    """
    Create a new recipe.

    Add a new recipe to the database.
    """
    recipes.append(recipe)
    return recipe


@app.get(
    "/recipes/",
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
    print(recipes)
    return recipes


@app.get("/recipes/search", response_model=List[Recipe])
async def search_recipes(
    title: Annotated[str | None, Query(title="Search by recipe title")] = None,
    ingredient: Annotated[str | None, Query(title="Search by ingredient name")] = None, 
    max_calories: Annotated[
        float | None, Query(gt=0, title="Filter by maximum calories")
    ] = None,
    vegetarian: Annotated[
        bool | None, Query(title="Filter for vegetarian recipes")
    ] = None,
    gluten_free: Annotated[
        bool | None, Query(title="Filter for gluten-free recipes")
    ] = None,
):
    """
    Search and filter recipes based on various criteria.

    Search and filter recipes based on ingredient name, title, ingredients, and nutritional content. Supports filtering for dietary preferences such as low-calorie, vegetarian, and gluten-free options.
    """
    results = recipes
    if title:
        results = [recipe for recipe in results if title.lower() in recipe['title'].lower()]
    if ingredient:
        results = [recipe for recipe in results if any(ingredient.lower() in ing['name'].lower() for ing in recipe['ingredients'])]
    if max_calories:
        results = [recipe for recipe in results if recipe['nutritional_info']['calories'] <= max_calories]
    if vegetarian is not None:
        results = [recipe for recipe in results if recipe.vegetarian == vegetarian]
    if gluten_free is not None:
        results = [recipe for recipe in results if recipe.gluten_free == gluten_free]
    return results


@app.get("/recipes/{recipe_id}", response_model=Recipe)
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
    for recipe in recipes:
        if recipe.id == recipe_id:
            return recipe
    raise HTTPException(status_code=404, detail="Recipe not found")


@app.put("/recipes/{recipe_id}", response_model=Recipe)
async def update_recipe(
    recipe_id: Annotated[int, Path(description="The ID of the item to delete")],
    recipe: Recipe,
):
    """
    Update a recipe by ID.

    Update the details of a recipe with the given ID in the database.
    """
    for index, db_recipe in enumerate(recipes):
        if db_recipe.id == recipe_id:
            recipes[index] = recipe
            return recipe
    raise HTTPException(status_code=404, detail="Recipe not found")


@app.delete("/recipes/{recipe_id}", response_model=Recipe)
async def delete_recipe(
    recipe_id: Annotated[int, Path(description="The ID of the item to delete")]
):
    """
    Delete a recipe by ID.

    Remove a recipe with the specified ID from the database.
    """
    for index, recipe in enumerate(recipes):
        if recipe.id == recipe_id:
            del recipes[index]
            return recipe
    raise HTTPException(status_code=404, detail="Recipe not found")

