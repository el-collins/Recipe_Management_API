from fastapi import FastAPI
from app.routers import recipe, ingredient, nutritional_info

app = FastAPI()

# Include routers
app.include_router(recipe.router)
app.include_router(ingredient.router)
app.include_router(nutritional_info.router)
