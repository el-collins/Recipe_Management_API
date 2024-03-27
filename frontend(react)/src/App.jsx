import { useState, useEffect } from 'react';
import axios from 'axios';
import Navbar from './components/Navbar';
import RecipeForm from './components/RecipeForm';

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
  const [editingRecipeId, setEditingRecipeId] = useState(null);
  const [initialValues, setInitialValues] = useState(null); // State to hold initial values for editing

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
      // Set the editingRecipeId and initialValues
      setEditingRecipeId(recipeId);
      setInitialValues(recipe); // Set the initial values for editing
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
    // Reset initialValues after submission
    setInitialValues(null);
  };

  return (
    <>
      <Navbar/>
      <div className="container mx-auto mt-8">
        {/* Render RecipeForm component */}
        <RecipeForm initialValues={initialValues} onSubmit={handleSubmit} />
        
        {/* Render RecipeList component passing recipes as prop */}
        {/* Here, you can map over recipes and render a list of recipes */}
        {recipes.map((recipe) => (
          <div key={recipe.id}>
            <h2>{recipe.title}</h2>
            <p>{recipe.description}</p>
            {/* Add an edit button for each recipe */}
            <button onClick={() => handleEditRecipe(recipe.id)}>Edit</button>
          </div>
        ))}
      </div>
    </>
  );
};

export default App;
