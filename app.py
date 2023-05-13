from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import os, json, random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SECRET_KEY'] = os.urandom(12)

db = SQLAlchemy(app)

number_of_recipes = 10

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), nullable=False)
    description = db.Column(db.Text, nullable=True)
    author = db.Column(db.Text, nullable=True)
    ingredients = db.Column(db.Text, nullable=False)
    method = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Recipe(name={self.name}, description={self.description}, ingredients={self.ingredients}, method={self.method}, author={self.author})'

if os.path.exists('recipes.db'):
    os.remove('recipes.db')

with app.app_context():
    db.create_all()

    with open("recipes.json", "r") as f:
        recipe_data_list = json.load(f)

    random_recipes = random.sample(recipe_data_list, number_of_recipes)

    for recipe_data in random_recipes:
        name = recipe_data["Name"]
        description = recipe_data["Description"]
        ingredients = "\n".join(recipe_data["Ingredients"])
        method = "\n".join(recipe_data["Method"])
        author = recipe_data.get("Author")

        recipe = Recipe(
            name=name,
            description=description,
            ingredients=ingredients,
            method=method,
            author=author,
        )

        db.session.add(recipe)
        db.session.commit()

@app.route('/')
def index():
    recipes = Recipe.query.all()
    return render_template('home.html', recipes=recipes)

@app.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    recipe = Recipe.query.filter_by(id=recipe_id).first_or_404()
    return render_template('recipe.html', recipe=recipe)

if __name__ == '__main__':
    app.run(debug=True)
