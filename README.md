# Recipe-App

## Recipe App
This is a basic recipe app built using Python Flask framework and SQLAlchemy. The app allows users to view and search for recipes from a pre-populated database.

## Installation
Clone or download this repository
Install the required dependencies by running pip install -r requirements.txt
Run the app using the command python app.py

## Usage
Once the app is running, users can access it by navigating to http://localhost:5000 in a web browser. The home page displays a list of all available recipes in the database. Users can click on any recipe to view its details.

The app has been pre-populated with a number of randomly selected recipes from the recipes.json file. The number of recipes can be adjusted by changing the number_of_recipes variable in the app.py file.

## Data Model
The app uses a SQLite database to store the recipe data. The Recipe table has the following columns:

id: primary key of the recipe
* **name**: name of the recipe**
* **description**: short description of the recipe
* **author**: name of the author who created the recipe (optional)
* **ingredients**: list of ingredients required for the recipe
* **method**: list of instructions for preparing the recipe

## Routes
The app has two main routes:

/ - displays a list of all available recipes
/recipe/<int:recipe_id> - displays the details of a specific recipe, identified by its ID

## Contributions
Contributions to this project are welcome! Feel free to submit a pull request or open an issue if you encounter any bugs or have suggestions for improvement.
