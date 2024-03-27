import React, { useState, useEffect } from 'react';
import axios from 'axios';
// import RecipeForm from './components/RecipeForm';
import Navbar from './components/Navbar';


// Assuming you have a function to fetch a single recipe by ID
const fetchRecipeById = async (recipeId) => {
  try {
    const response = await axios.get(`http://your-api-url.com/recipes/${recipeId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching recipe:', error);
    return null;
  }
};

const App = () => {
  const [recipes, setRecipes] = useState([]);

  useEffect(() => {
    // Fetch recipes from the server when the component mounts
    fetchRecipes();
  }, []);

  const fetchRecipes = async () => {
    try {
      const response = await axios.get('http://your-api-url.com/recipes');
      setRecipes(response.data);
    } catch (error) {
      console.error('Error fetching recipes:', error);
    }
  };
  
  const handleEditRecipe = async (recipeId) => {
    // Fetch the recipe data for editing
    const recipe = await fetchRecipeById(recipeId);
    if (recipe) {
      // Set the editingRecipeId and pass initialValues to RecipeForm
      setEditingRecipeId(recipeId);
    } else {
      // Handle error
    }
  };

  const handleSubmit = async (formData) => {
    try {
      if (editingRecipeId) {
        // If editing an existing recipe, update it
        await axios.put(`http://your-api-url.com/recipes/${editingRecipeId}`, formData);
      } else {
        // If creating a new recipe, add it
        await axios.post('http://your-api-url.com/recipes', formData);
      }
      // Fetch updated recipes after creating/editing a recipe
      fetchRecipes();
    } catch (error) {
      console.error('Error creating/editing recipe:', error);
    }
    // Reset editingRecipeId after submission
    setEditingRecipeId(null);
  };


  return (
    <div>
      <Navbar/>
      <div className="container mx-auto mt-8">
        <h1 className="text-3xl font-semibold mb-4">Recipe Management</h1>
        {/* <RecipeForm onSubmit={handleSubmit} /> */}
        {/* Render RecipeList component passing recipes as prop */}
      
      </div>
    </div>
  );
};

export default App;
