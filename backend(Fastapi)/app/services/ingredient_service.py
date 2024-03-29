from typing import List, Optional
from app.models import Ingredient

class IngredientService:
    def __init__(self):
        # Dummy data to simulate database
        self.ingredients_db = []

    def get_ingredients(self) -> List[Ingredient]:
        return self.ingredients_db

    def get_ingredient(self, ingredient_id: int) -> Optional[Ingredient]:
        if ingredient_id < len(self.ingredients_db):
            return self.ingredients_db[ingredient_id]
        else:
            return None

    def create_ingredient(self, ingredient: Ingredient) -> Ingredient:
        self.ingredients_db.append(ingredient)
        return ingredient

    def update_ingredient(self, ingredient_id: int, ingredient: Ingredient) -> Optional[Ingredient]:
        if ingredient_id < len(self.ingredients_db):
            self.ingredients_db[ingredient_id] = ingredient
            return ingredient
        else:
            return None

    def delete_ingredient(self, ingredient_id: int) -> bool:
        if ingredient_id < len(self.ingredients_db):
            del self.ingredients_db[ingredient_id]
            return True
        else:
            return False
