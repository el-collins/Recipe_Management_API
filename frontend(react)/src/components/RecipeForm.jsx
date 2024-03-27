import { useState, useEffect } from "react";
import axios from "axios";

// eslint-disable-next-line react/prop-types
const RecipeForm = ({ onSubmit, initialValues }) => {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [cookingInstructions, setCookingInstructions] = useState("");
  const [ingredients, setIngredients] = useState([]);
  const [newIngredient, setNewIngredient] = useState({
    name: "",
    quantity: "",
  });
  const [nutritionalInfo, setNutritionalInfo] = useState({});

  useEffect(() => {
    // If initialValues are provided, set form fields with initial values
    if (initialValues) {
      setTitle(initialValues.title || "");
      setDescription(initialValues.description || "");
      setCookingInstructions(initialValues.cookingInstructions || "");
      setIngredients(initialValues.ingredients || []);
      setNutritionalInfo(initialValues.nutritionalInfo || {});
    }
  }, [initialValues]);

  const handleIngredientChange = (index, field, value) => {
    const updatedIngredients = [...ingredients];
    updatedIngredients[index][field] = value;
    setIngredients(updatedIngredients);
  };

  const handleAddIngredient = () => {
    setIngredients([...ingredients, { ...newIngredient }]);
    setNewIngredient({ name: "", quantity: "" });
  };

  const handleDeleteIngredient = (index) => {
    const updatedIngredients = [...ingredients];
    updatedIngredients.splice(index, 1);
    setIngredients(updatedIngredients);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("YOUR_API_ENDPOINT", {
        title,
        description,
        cookingInstructions,
        ingredients,
        nutritionalInfo,
      });
      onSubmit(response.data); // Assuming your onSubmit function takes the created recipe data as an argument
    } catch (error) {
      console.error("Error submitting recipe:", error);
      // Handle error
    }
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto mt-20">
      <div className="mb-4">
        <label htmlFor="title" className="block text-[#003366] font-semibold">
          Title:
        </label>
        <input
          type="text"
          id="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Title"
          required
          className="w-full mt-2 p-2 border rounded-xl"
        />
      </div>
      <div className="mb-4">
        <label
          htmlFor="description"
          className="block text-[#003366] font-semibold"
        >
          Description:
        </label>
        <textarea
          id="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Description"
          required
          className="w-full mt-2 p-2 border rounded-xl"
        />
      </div>
      <div className="mb-4">
        <label
          htmlFor="cookingInstructions"
          className="block text-[#003366] font-semibold"
        >
          Cooking Instructions:
        </label>
        <textarea
          id="cookingInstructions"
          value={cookingInstructions}
          onChange={(e) => setCookingInstructions(e.target.value)}
          placeholder="Cooking Instructions"
          required
          className="w-full mt-2 p-2 border rounded-xl"
        />
      </div>
      <div className="mb-4">
        <label className="block text-[#003366] font-semibold">
          Ingredients:
        </label>
        {ingredients.map((ingredient, index) => (
          <div key={index} className="flex items-center mb-2">
            <input
              type="text"
              value={ingredient.name}
              onChange={(e) =>
                handleIngredientChange(index, "name", e.target.value)
              }
              placeholder="Ingredient name"
              required
              className="w-1/2 mr-2 p-2 border rounded-xl"
            />
            <input
              type="text"
              value={ingredient.quantity}
              onChange={(e) =>
                handleIngredientChange(index, "quantity", e.target.value)
              }
              placeholder="Quantity"
              className="w-1/4 p-2 border rounded-xl"
            />
            <button
              type="button"
              onClick={() => handleDeleteIngredient(index)}
              className="ml-2 bg-red-500 text-white px-4 py-2 rounded-xl"
            >
              Delete
            </button>
          </div>
        ))}
        <div className="flex items-center">
          <input
            type="text"
            value={newIngredient.name}
            onChange={(e) =>
              setNewIngredient({ ...newIngredient, name: e.target.value })
            }
            placeholder="Ingredient name"
            className="w-1/2 mr-2 p-2 border rounded-xl"
          />
          <input
            type="text"
            value={newIngredient.quantity}
            onChange={(e) =>
              setNewIngredient({ ...newIngredient, quantity: e.target.value })
            }
            placeholder="Quantity"
            className="w-1/4 p-2 border rounded-xl"
          />
          <button
            type="button"
            onClick={handleAddIngredient}
            className="ml-2 bg-blue-500 text-[#003366] px-4 py-2 rounded-xl"
          >
            Add
          </button>
        </div>
      </div>
      {/* <div className="mb-4">
        <label
          htmlFor="nutritionalInfo"
          className="block text-[#003366] font-semibold"
        >
          Nutritional Information:
        </label>
      </div> */}
      <button
        type="submit"
        className="bg-green-500 text-[#003366] px-4 py-2 rounded-xl"
      >
        Submit
      </button>
    </form>
  );
};

export default RecipeForm;
