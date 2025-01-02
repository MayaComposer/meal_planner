import numpy as np
import pandas as pd
import random
import datetime

def read_data(file_path: str) -> pd.DataFrame:
    file = pd.ExcelFile(file_path)
    df = pd.read_excel(file, index_col=0, header=0, keep_default_na=False)
    return df

def sort_recipes(df: pd.DataFrame):
    current_season = 'winter'
    week = datetime.datetime.now().isocalendar()[1]
    if week >= 40 or week <= 14:
        current_season = 'winter'
    else:
        current_season = 'summer'
    print('current season: ' + current_season)

    fish_recipes, meat_recipes, veg_recipes = [], [], []
    for row in df.itertuples():
        if row.season == current_season or 'both':
            if row.category == 'f':
                fish_recipes.append(row)
            elif row.category == 'm':
                meat_recipes.append(row)
            elif row.category == 'v':
                veg_recipes.append(row)
    return fish_recipes, meat_recipes, veg_recipes

def generate_mealplan(fish_recipes, meat_recipes, veg_recipes) -> list:
    meals = []
    _fish_recipes = random.sample(fish_recipes, len(fish_recipes))
    _meat_recipes = random.sample(meat_recipes, len(meat_recipes))
    _veg_recipes = random.sample(veg_recipes, len(veg_recipes))

    meals.extend(_fish_recipes[:2])
    meals.extend(_meat_recipes[:1])
    meals.extend(_veg_recipes[:4])

    np.random.shuffle(meals)
    return meals

def add_recipe(df: pd.DataFrame, recipe=pd.DataFrame([['TEST_INGREDIENTS', 'v', 'TEST_FRESH_INGREDIENTS', '']], columns=['ingredients', 'category', 'fresh_ingredients', 'instructions'], index=['ADDED_RECIPE'])) -> pd.DataFrame:
    print('recipe added')
    return pd.concat([df, recipe])

def main():
    print('mealplan stuff')
    from utils.helpers import configure_mealplan_text, write_to_file
    df = read_data('data/meals.xlsx')
    fish_recipes, meat_recipes, veg_recipes = sort_recipes(df)
    meals = generate_mealplan(fish_recipes, meat_recipes, veg_recipes)
    mealplan_text = configure_mealplan_text(meals)
    write_to_file(mealplan_text)

    meal_dict = df.to_dict('index')
    print(meal_dict['chicken cheese wraps']['ingredients'])

    with open("dict.txt", "w") as file:
        file.write(str(meal_dict))
        
if __name__ == "__main__":
    main()