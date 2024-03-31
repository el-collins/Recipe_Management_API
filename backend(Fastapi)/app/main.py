from fastapi import FastAPI
from app.routers import recipe, ingredient
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(recipe.router)
app.include_router(ingredient.router)
# app.include_router(nutritional_info.router)
