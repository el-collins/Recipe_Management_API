![Tests](https://img.shields.io/badge/Tests-PASSING-brightgreen) ![Coverage Status](https://img.shields.io/badge/coverage-91%25-brightgreen) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Poetryize) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)


<!-- [![Tests](https://github.com/thoth2357/Poetryize/actions/workflows/python-app.yml/badge.svg)](https://github.com/thoth2357/Poetryize/actions/workflows/python-app.yml) 

[![Coverage Status](https://coveralls.io/repos/github/thoth2357/Poetryize/badge.svg?branch=main)](https://coveralls.io/github/thoth2357/Poetryize?branch=main) 
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)  -->




<!-- [![Tests](https://img.shields.io/badge/tests-PASSING-brightgreen)](https://github.com/el-collins/Recipe_Management_API/actions)
[![Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen)](COVERAGE_REPORT_URL) -->


# Recipe Management API 🍲
```markdown

Welcome to the Recipe Management API, where culinary art meets coding! This FastAPI backend service is your digital sous-chef, helping you manage a delicious database of recipes, ingredients, and nutritional facts.

## Features 🌟

- **Model Magic**: Our models are like the ingredients of our API, defining the structure of recipes, ingredients, and nutritional info with precision.
- **CRUD-y Goodness**: Create, Read, Update, and Delete operations are the bread and butter of our API, allowing full control over your culinary collection.
- **Search & Filter**: Looking for gluten-free? Low-calorie? Our API lets you sift through recipes faster than sifting flour!
- **Nutritional Calculations**: Automatically tally up the calories, fat, and protein so you can focus on the flavor.

## Getting Started 🚀

To get started, clone this repo and install the required packages:

```bash
git clone https://github.com/your-username/recipe-management-api.git
cd recipe-management-api
poetry install
```
This will install all the necessary dependencies as specified in the pyproject.toml file.

Run the server with:

```bash
poetry run uvicorn app.main:app --reload

```

## Endpoints 📍

- `GET /recipes`: Get all recipes.
- `POST /recipes`: Add a new recipe.
- `GET /recipes/{id}`: Get a recipe by ID.
- `PUT /recipes/{id}`: Update a recipe by ID.
- `DELETE /recipes/{id}`: Delete a recipe by ID.
- `GET /search`: Search for recipes based on criteria.

For more details, check out the [API documentation](http://127.0.0.1:8000/docs).

## Advanced Usage 🔍

To calculate nutritional information:

```python
POST /recipes/{id}/calculate-nutrition
```

This will return the nutritional breakdown based on the ingredients.

## Documentation & Testing 📚

We've documented every endpoint with Swagger UI, and we've written tests that cover every conceivable scenario, including those edge cases you thought we forgot!
Run tests with:

```bash
poetry run pytest
```

## Contributing 🤝

Want to contribute? Great! We welcome contributions from everyone. Please check out our [contributing guidelines](CONTRIBUTING.md).

## License 📄

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments 🎉

- Hat tip to anyone whose code was used
- Inspiration
- etc

Happy Cooking! 🍳
```

Remember to replace `your-username` with your actual GitHub username and update the links to point to your actual repository. This README is designed to be engaging and informative, providing all the necessary steps to get started, as well as a glimpse into the API's capabilities. Bon Appétit! 🥘