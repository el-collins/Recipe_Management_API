from typing import List, Optional
from app.models import Recipe

class RecipeService:
    def __init__(self):
        # Dummy data to simulate database
        self.recipes_db = []

    def get_recipes(self) -> List[Recipe]:
        return self.recipes_db

    def get_recipe(self, recipe_id: int) -> Optional[Recipe]:
        if recipe_id < len(self.recipes_db):
            return self.recipes_db[recipe_id]
        else:
            return None

    def create_recipe(self, recipe: Recipe) -> Recipe:
        self.recipes_db.append(recipe)
        return recipe

    def update_recipe(self, recipe_id: int, recipe: Recipe) -> Optional[Recipe]:
        if recipe_id < len(self.recipes_db):
            self.recipes_db[recipe_id] = recipe
            return recipe
        else:
            return None

    def delete_recipe(self, recipe_id: int) -> bool:
        if recipe_id < len(self.recipes_db):
            del self.recipes_db[recipe_id]
            return True
        else:
            return False
