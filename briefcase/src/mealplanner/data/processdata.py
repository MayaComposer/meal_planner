import numpy as np
import pandas as pd
import random
import datetime
import json

def read_data() -> pd.DataFrame:
    # file = pd.ExcelFile('./data/meals.xlsx')
    # df = pd.read_excel(file, index_col=0, header=0, keep_default_na=False)
    df = pd.read_json('./data/data.json', orient='index')
    return df

def save_data(df: pd.DataFrame) -> None:
    df.to_json('./data/data.json', orient='index', indent=4)

def save_mealplan(mealplan: list, filepath: str = './data/previous_mealplan.json') -> None:
    """Save the current meal plan to a JSON file."""
    with open(filepath, 'w') as file:
        json.dump([meal.Index for meal in mealplan], file)

def load_previous_mealplan(filepath: str = './data/previous_mealplan.json') -> list:
    """Load the previous meal plan from a JSON file."""
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def sort_recipes(df: pd.DataFrame):
    current_season = 'winter'  # season filter
    week = datetime.datetime.now().isocalendar()[1]
    if week >= 40 or week <= 14:
        current_season = 'winter'
    else:
        current_season = 'summer'
    # print('current season: ' + current_season)

    fish_recipes, meat_recipes, veg_recipes = [], [], []
    for row in df.itertuples():
        if row.season == current_season or row.season == 'both':
            # print(row.season)
            if row.category == 'f':
                fish_recipes.append(row)
            elif row.category == 'm':
                meat_recipes.append(row)
            elif row.category == 'v':
                veg_recipes.append(row)
    return fish_recipes, meat_recipes, veg_recipes

def generate_mealplan(fish_recipes, meat_recipes, veg_recipes) -> list:
    random.seed()
    previous_mealplan = load_previous_mealplan()

    # Filter out previous meals
    fish_recipes = [recipe for recipe in fish_recipes if recipe.Index not in previous_mealplan]
    meat_recipes = [recipe for recipe in meat_recipes if recipe.Index not in previous_mealplan]
    veg_recipes = [recipe for recipe in veg_recipes if recipe.Index not in previous_mealplan]

    # Shuffle and select meals
    _fish_recipes = random.sample(fish_recipes, min(2, len(fish_recipes)))
    _meat_recipes = random.sample(meat_recipes, min(1, len(meat_recipes)))
    _veg_recipes = random.sample(veg_recipes, min(4, len(veg_recipes)))

    meals = []
    meals.extend(_fish_recipes)
    meals.extend(_meat_recipes)
    meals.extend(_veg_recipes)

    np.random.shuffle(meals)

    # Save the new meal plan
    #save_mealplan(meals)
    return meals

def add_recipe(df: pd.DataFrame, recipe=pd.DataFrame([['TEST_INGREDIENTS', 'v', 'TEST_FRESH_INGREDIENTS', '', 'both']], columns=['ingredients', 'category', 'fresh_ingredients', 'instructions', 'season'], index=['ADDED_RECIPE'])) -> pd.DataFrame:
    print('recipe added')
    return pd.concat([df, recipe])

def main():
    print('TESTING processdata.py')
    from utils.helpers import configure_mealplan_text, write_to_file
    df = read_data()
    fish_recipes, meat_recipes, veg_recipes = sort_recipes(df)
    meals = generate_mealplan(fish_recipes, meat_recipes, veg_recipes)
    mealplan_text = configure_mealplan_text(meals)
    write_to_file(mealplan_text)

    meals = df.to_json('data.json', orient='index')

    mealstwo = pd.read_json('data.json', orient='index')

    print(mealstwo.loc['curry'])

if __name__ == "__main__":
    main()