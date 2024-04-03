import RecipeItems from "./Recipe";

const RecipeView = ({ recipeList }) => {
  return (
    // flex-1 break-inside-avoid rounded-lg border border-gray-300 bg-white/20 bg-clip-padding p-6 pb-4 backdrop-blur-lg backdrop-filter md:w-[360px] w-full h-fit mx-auto
    <div className="flex justify-center items-center h-screen">
      <div classNam="w-1/2 bg-white rounded shadow p-8 mt-4">
        <h3 className="font-bold text-xl mb-4">{recipeList.title}</h3>

        <div className="my-4 text-sm text-gray-700"></div>

        {recipeList.map((recipe) => (
          <div>
            <div>
              <p>{recipe.name}</p>
              <p>{recipe.description}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RecipeView;
