#!/usr/bin/python3.5
from datetime import date
from recipes import Recipes
from flask import Flask, render_template, url_for

app = Flask(__name__)
@app.route("/")

def menu():
    # Determine the season of the year
    month = date.today().month
    if month in range(5,10):
        current_season = "Summer"
    else:
        current_season = "Winter"

    recipes = Recipes()
    recipes.load_from_file('recipes.csv')

    # Sort the recipes
    enabled_recipes = recipes.filter('Enabled', [str(1)])
    seasonal_recipes = enabled_recipes.filter('Season', [current_season, 'Any'])

    red_meat_recipes = seasonal_recipes.filter('Protein', ['Beef', 'Pork'])
    chicken_recipes = seasonal_recipes.filter('Protein', ['Chicken'])
    pesca_recipes = seasonal_recipes.filter('Protein', ['Fish', 'Vegetarian'])

    #print("Red meat recipes: -------------------------------------------")
    #red_meat_recipes.pretty_print()
    #print("--------- Chicken recipes: ----------------------------------")
    #chicken_recipes.pretty_print()
    #print("---------------------------- Pescatarian recipes: -----------")
    #pesca_recipes.pretty_print()

    # Randomly select 3
    week = red_meat_recipes.random_recipe()
    week.add(chicken_recipes.random_recipe())
    week.add(pesca_recipes.random_recipe())

    week.pretty_print()
    print('')
    week.print_grocery_list()
    return render_template('output.html', recipes=week.get_recipe_names(),  groceries=week.get_grocery_list())
