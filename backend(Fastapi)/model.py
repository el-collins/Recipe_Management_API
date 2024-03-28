from typing import List, Optional
from pydantic import BaseModel, Field

# Model to represent nutritional information
class NutritionalInfo(BaseModel):
    calories: float = Field(..., gt=0, description="Calories in kcal")
    fat: float = Field(..., gt=0, description="Fat in grams")
    protein: float = Field(..., gt=0, description="Protein in grams")
    carbohydrates: float = Field(..., gt=0, description="Carbohydrates in grams")

# Model to represent an ingredient with its quantity
class Ingredient(BaseModel):
    name: str = Field(..., description="Name of the ingredient")
    quantity: str = Field(..., description="Quantity of the ingredient")

# Model to represent a recipe
class Recipe(BaseModel):
    id: Optional[int] = Field(None, description="Unique ID for the recipe")
    title: str = Field(..., description="Title of the recipe")
    ingredients: List[Ingredient] = Field(..., description="List of ingredients")
    instructions: str = Field(..., description="Cooking instructions")
    nutritional_info: NutritionalInfo = Field(..., description="Nutritional information")
    created_at: Optional[str] = Field(None, description="Creation date of the recipe")

# Example usage
example_recipe = {
    "title": "Avocado Toast",
    "ingredients": [
        {"name": "Avocado", "quantity": "1"},
        {"name": "Bread", "quantity": "2 slices"},
        {"name": "Salt", "quantity": "1 pinch"},
        # Add more ingredients as needed
    ],
    "instructions": "Toast the bread, mash the avocado and spread on the toast, sprinkle with salt.",
    "nutritional_info": {
        "calories": 320,
        "fat": 15,
        "protein": 6,
        "carbohydrates": 42
    }
}

recipe = Recipe(**example_recipe)
print(recipe)
