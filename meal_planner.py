import pandas as pd
import numpy as np
import random
import customtkinter as ctk

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def read_data():
    # Open excel file
    file = pd.ExcelFile('meals.xlsx')
    print('data read')
    return pd.read_excel(file, index_col=0, header=0, keep_default_na=False)

# Read excel sheet into dataframe
df = read_data()

# Iterate over dataframe and add recipes to lists based on category
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

    # Add a recipe of each category to the meals list
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

def display_mealplan():
    meals = generate_mealplan()
    mealplan_text = ""
    for count, meal in enumerate(meals):
        mealplan_text += f"{days[count]}: \n{meal.Index} ({meal.category})\n"
        mealplan_text += f"Ingredients: {meal.ingredients} {meal.fresh_ingredients}\n\n"
    
    mealplan_label.configure(text=mealplan_text)

    with open("output.txt", "w") as f:
        f.write(mealplan_text)

def add_recipe():
    print('here a recipe would be added')

# Set up customtkinter window
root = ctk.CTk()
root.title("Meal Planner")
root.minsize(400, 400)  # width, height
root.geometry("500x720+0+0")
root.iconbitmap("icon.ico")

# Create button to generate meal plan
generate_button = ctk.CTkButton(root, text="Generate Meal Plan", command=display_mealplan, fg_color='teal', text_color='white')
generate_button.pack(pady=10)

read_data_button = ctk.CTkButton(root, text="Add new recipe", command=add_recipe, fg_color='teal', text_color='white')
read_data_button.pack(pady=10)

# Label to display the meal plan
mealplan_label = ctk.CTkLabel(root, text="", justify="center", font=("Helvetica", 18))
mealplan_label.pack(pady=20)

root.mainloop()