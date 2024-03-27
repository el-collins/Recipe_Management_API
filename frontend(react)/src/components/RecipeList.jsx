// src/components/RecipeList.js
import React from 'react';
import RecipeCard from './RecipeCard';

const RecipeList = ({ recipes }) => {
  return (
<div className="container mx-auto mt-8">
      <h2 className="text-2xl font-semibold mb-4">Recipes</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        {recipes.map(recipe => (
          <div key={recipe.id} className="bg-white shadow rounded p-4">
            <h3 className="text-lg font-semibold mb-2">{recipe.title}</h3>
            <p className="text-gray-600 mb-2">{recipe.description}</p>
            <div className="flex justify-between">
              <span className="text-gray-500">{recipe.ingredients.length} Ingredients</span>
              <a href="#" className="text-blue-500">View Recipe</a>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RecipeList;
