import React, { useState } from 'react';
import axios from 'axios';

const RecipeForm = ({ onSubmit, initialValues }) => {
  const [title, setTitle] = useState(initialValues.title || '');
  const [description, setDescription] = useState(initialValues.description || '');
  const [cookingInstructions, setCookingInstructions] = useState(initialValues.cookingInstructions || '');
  const [ingredients, setIngredients] = useState(initialValues.ingredients || []);
  const [newIngredient, setNewIngredient] = useState({ name: '', quantity: '' });
  const [nutritionalInfo, setNutritionalInfo] = useState(initialValues.nutritionalInfo || {});

  const handleIngredientChange = (index, field, value) => {
    const updatedIngredients = [...ingredients];
    updatedIngredients[index][field] = value;
    setIngredients(updatedIngredients);
  };

  const handleAddIngredient = () => {
    setIngredients([...ingredients, { ...newIngredient }]);
    setNewIngredient({ name: '', quantity: '' });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('YOUR_API_ENDPOINT', {
        title,
        description,
        cookingInstructions,
        ingredients,
        nutritionalInfo
      });
      onSubmit(response.data); // Assuming your onSubmit function takes the created recipe data as an argument
    } catch (error) {
      console.error('Error submitting recipe:', error);
      // Handle error
    }
  };
  
  
  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto">
      <div className="mb-4">
        <label htmlFor="title" className="block text-gray-700 font-semibold">Title:</label>
        <input type="text" id="title" value={title} onChange={(e) => setTitle(e.target.value)} className="w-full mt-1 p-2 border rounded" />
      </div>
      <div className="mb-4">
        <label htmlFor="description" className="block text-gray-700 font-semibold">Description:</label>
        <textarea id="description" value={description} onChange={(e) => setDescription(e.target.value)} className="w-full mt-1 p-2 border rounded" />
      </div>
      <div className="mb-4">
        <label htmlFor="cookingInstructions" className="block text-gray-700 font-semibold">Cooking Instructions:</label>
        <textarea id="cookingInstructions" value={cookingInstructions} onChange={(e) => setCookingInstructions(e.target.value)} className="w-full mt-1 p-2 border rounded" />
      </div>
      <div className="mb-4">
        <label className="block text-gray-700 font-semibold">Ingredients:</label>
        {ingredients.map((ingredient, index) => (
          <div key={index} className="flex items-center mb-2">
            <input type="text" value={ingredient.name} onChange={(e) => handleIngredientChange(index, 'name', e.target.value)} placeholder="Ingredient name" className="w-1/2 mr-2 p-2 border rounded" />
            <input type="text" value={ingredient.quantity} onChange={(e) => handleIngredientChange(index, 'quantity', e.target.value)} placeholder="Quantity" className="w-1/4 p-2 border rounded" />
          </div>
        ))}
        <div className="flex items-center">
          <input type="text" value={newIngredient.name} onChange={(e) => setNewIngredient({ ...newIngredient, name: e.target.value })} placeholder="Ingredient name" className="w-1/2 mr-2 p-2 border rounded" />
          <input type="text" value={newIngredient.quantity} onChange={(e) => setNewIngredient({ ...newIngredient, quantity: e.target.value })} placeholder="Quantity" className="w-1/4 p-2 border rounded" />
          <button type="button" onClick={handleAddIngredient} className="ml-2 bg-blue-500 text-white px-4 py-2 rounded">Add</button>
        </div>
      </div>
      <div className="mb-4">
        <label htmlFor="nutritionalInfo" className="block text-gray-700 font-semibold">Nutritional Information:</label>
        {/* Add input fields for nutritional information here */}
      </div>
      <button type="submit" className="bg-green-500 text-white px-4 py-2 rounded">Submit</button>
    </form>
  );
};

export default RecipeForm;
