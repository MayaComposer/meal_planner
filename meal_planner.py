#list of recipes
#list of ingredients
# pick random recipe based on ingredients in pantry, 
#               only the fresh ingredients are needed to check. Herbs and stuff not really.
# then fill up the rest of the days of the week with recipes.
#create a shopping list 

import pandas as pd
import numpy as np
import random

from tkinter import *

#open excel file
file = pd.ExcelFile('meals.xlsx')

column_names = ['Recipe', 'Difficulty', 'M/F/V', 'Ingredients']

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def read_data():
    return pd.read_excel(file, index_col=0, header=0, keep_default_na=False)

#read excel sheet into dataframe
df = read_data()



#iterate over dataframe and add recipes to lists based on category
def sort_recipes():
    fish_recipes = []
    meat_recipes = []
    veg_recipes = []
    for row in df.itertuples():
        if row.category == 'f':
            fish_recipes.append(row)
        if row.category == 'm':
            meat_recipes.append(row)
        if row.category == 'v':
            veg_recipes.append(row)
    return fish_recipes, meat_recipes, veg_recipes

fish_recipes, meat_recipes, veg_recipes = sort_recipes()

def generate_mealplan() -> list:
    meals = []

    #add a recipe of each category to the meals list
    np.random.shuffle(fish_recipes)
    np.random.shuffle(meat_recipes)
    np.random.shuffle(veg_recipes)
    for recipe in range(0, 2):
        meals.append(fish_recipes[recipe])

    for recipe in range(0, 1):
        meals.append(meat_recipes[recipe])

    for recipe in range(0, 4):
        meals.append(veg_recipes[recipe])

    np.random.shuffle(meals)

    print('mealplan generated')

    return meals

meals = generate_mealplan()


mealplan_text = []

print('meal plan generated')

def display_mealplan():
    meals = generate_mealplan()
    mealplan_text = ""
    for count, meal in enumerate(meals):
        mealplan_text += f"{days[count]}: {meal.Index} ({meal.category})\n"
        mealplan_text += f"Ingredients: {meal.ingredients} {meal.fresh_ingredients}\n\n"
    
    mealplan_label.config(text=mealplan_text)

    with open("output.txt", "w") as f:
        f.write(mealplan_text)

# Set up Tkinter window
root = Tk()
root.title("Meal Planner")
root.minsize(400, 400)  # width, height
root.geometry("400x600")

# Create button to generate meal plan
generate_button = Button(root, text="Generate Meal Plan", command=display_mealplan)
generate_button.pack(pady=20)

# Label to display the meal plan
mealplan_label = Label(root, text="", justify=LEFT)
mealplan_label.pack(pady=20)

root.mainloop()