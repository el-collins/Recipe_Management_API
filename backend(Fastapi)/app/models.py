from typing import List
from pydantic import BaseModel, Field



class NutritionalInfo(BaseModel):
    calories: float | None = Field(default=None, ge=0, description="Calories in kcal")
    fat: float | None = Field(default=None, ge=0, description="Fat in grams")
    protein: float | None = Field(default=None, ge=0, description="Protein in grams")
    carbohydrates: float | None = Field(
        default=None, ge=0, description="Carbohydrates in grams"
    )

class Ingredient(BaseModel):
    name: str = Field(..., description="Name of the ingredient")
    quantity: str = Field(..., description="Quantity of the ingredient")


class Recipe(BaseModel):
    id: int
    title: str = Field(..., description="Title of the recipe")
    description: str = Field(..., description="Description of the dish")
    instructions: str = Field(..., description="Cooking instructions")
    ingredients: List[Ingredient] = Field(..., description="List of ingredients")
    nutritional_info: NutritionalInfo = Field(
        ..., description="Nutritional information"
    )
