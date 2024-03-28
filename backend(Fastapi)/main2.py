from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from pydantic import BaseModel, Field

# Define Pydantic models

class NutritionalInfo(BaseModel):
    calories: float | None = Field(None, gt=0, description="Calories in kcal")

    #  calories: Optional[float] = Field(None, gt=0, description="Calories in kcal")
    protein: Optional[float]
    carbs: Optional[float]
    fat: Optional[float]

class Ingredient(BaseModel):
    name: str
    quantity: str

class Recipe(BaseModel):
    title: str
    description: str
    cooking_instructions: str
    ingredients: List[Ingredient]
    nutritional_info: NutritionalInfo

# Create FastAPI app instance
app = FastAPI()

# In-memory database for storing recipes
recipes_db = []

# Routes

@app.get("/recipes/", response_model=List[Recipe])
def get_recipes():
    return recipes_db

@app.get("/recipes/{recipe_id}", response_model=Recipe)
def get_recipe(recipe_id: int):
    try:
        return recipes_db[recipe_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Recipe not found")

@app.post("/recipes/", response_model=Recipe)
def create_recipe(recipe: Recipe):
    recipes_db.append(recipe)
    return recipe

@app.put("/recipes/{recipe_id}", response_model=Recipe)
def update_recipe(recipe_id: int, recipe: Recipe):
    try:
        recipes_db[recipe_id] = recipe
        return recipe
    except IndexError:
        raise HTTPException(status_code=404, detail="Recipe not found")

@app.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int):
    try:
        del recipes_db[recipe_id]
        return {"message": "Recipe deleted successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Recipe not found")
