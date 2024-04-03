import Navbar from './components/Navbar'
import RecipeForm from './components/RecipeForm'
import { useState, useEffect } from "react";
import axios from 'axios';
import RecipeView from './components/RecipeView';



const App = () => {
  const [recipeList, setRecipeList] = useState([{}]);

  // Read all recipes
  useEffect(() => {
    axios.get("http://localhost:8000/api/recipes").then((res) => {
      setRecipeList(res.data);
    });
  });


  return (
    <div>
      <Navbar/>
      <RecipeForm/>
      <RecipeView recipeList={recipeList}/>
    </div>
  )
}

export default App