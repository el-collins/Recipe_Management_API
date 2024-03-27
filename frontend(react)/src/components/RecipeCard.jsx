// src/components/RecipeCard.js
import React from 'react';

const RecipeCard = ({ recipe }) => {
  return (
    <div className="border rounded-lg p-4 shadow-lg">
      <h3 className="text-lg font-bold">{recipe.title}</h3>
      {/* Display other recipe details */}
    </div>
  );
};

export default RecipeCard;
