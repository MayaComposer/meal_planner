import pandas as pd
import numpy as np
import random
import customtkinter as ctk
from collections import OrderedDict

def read_data() -> pd.DataFrame:
    # Open excel file
    file = pd.ExcelFile('./data/meals.xlsx')
    print('data read')
    df = pd.read_excel(file, index_col=0, header=0, keep_default_na=False)
    return df

#GLOBAL VARIABLES

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

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

shopping_list_string = ''
shopping_list = []

def generate_mealplan() -> list:
    meals = []

    # Add a recipe of each category to the meals list
    _fish_recipes = random.sample(fish_recipes, len(fish_recipes))
    _meat_recipes = random.sample(meat_recipes, len(meat_recipes))
    _veg_recipes = random.sample(veg_recipes, len(veg_recipes))

    meals.extend(_fish_recipes[:2])
    meals.extend(_meat_recipes[:1])
    meals.extend(_veg_recipes[:4])

    np.random.shuffle(meals)

    return meals

def write_to_file(text: str) -> None:
    with open("output.txt", "w") as file:
        file.write(text)

def add_recipe(df: pd.DataFrame, recipe=pd.DataFrame([['TEST_INGREDIENTS', 'v', 'TEST_FRESH_INGREDIENTS', '']], columns=['ingredients', 'category', 'fresh_ingredients', 'instructions'], index=['ADDED_RECIPE'])) -> pd.DataFrame:
    
    #Here we'd probably do smth with the input recipe data so it becomes a dataframe and can be added to df but for now it is just default values
    print('recipe added')

    #add a new recipe to df
    return pd.concat([df, recipe])

def pressed_add_recipe() -> None:
    global df, fish_recipes, meat_recipes, veg_recipes
    df = add_recipe(df)

    #sort the recipes again
    fish_recipes, meat_recipes, veg_recipes = sort_recipes()

def remove_duplicates(input_list: list) -> list:
    # Remove duplicates while preserving order
    return list(OrderedDict.fromkeys(input_list))

def shopping_list_to_text(shopping_list) -> str:
    shopping_list_text = 'Shopping list: \n'
    
    for ingredient in shopping_list:
        shopping_list_text += f'- {ingredient}\n'
    return shopping_list_text

def display_mealplan() -> None:
    meals = generate_mealplan()
    print(meals)
    mealplan_text = ''
    
    mealplan_text = configure_mealplan_text(meals, mealplan_text)
    
    mealplan_label.configure(text=mealplan_text)
    print('mealplan text' + mealplan_text)

    shopping_list_text = configure_shopping_list(meals)

    # Also add to file
    write_to_file(mealplan_text + shopping_list_text)

def configure_shopping_list(meals) -> str:
    shopping_list = []
    shopping_list_string = ''

    for count, meal in enumerate(meals):
        # Shopping list
        shopping_list_string += f'{days[count]} \n {meal.ingredients},{meal.fresh_ingredients},'

    # Remove spaces and split into a list
    shopping_list_string = shopping_list_string.replace(' ', '')


    shopping_list = shopping_list_string.split(',')
    shopping_list = list(filter(None, shopping_list))

    # Configure shopping list
    shopping_list = remove_duplicates(shopping_list)
    shopping_list_text = shopping_list_to_text(shopping_list)
    return shopping_list_text

def configure_mealplan_text(meals, mealplan_text):
    for count, meal in enumerate(meals):
        # Meal plan
        mealplan_text += f'{days[count]}: \n{meal.Index} ({meal.category})\n'
        mealplan_text += f'Ingredients: {meal.ingredients} {meal.fresh_ingredients}\n\n'
    
    print('mealplan function')
    print(mealplan_text)

    return mealplan_text

        

# Set up customtkinter window
root = ctk.CTk()
root.title("Meal Planner")
root.minsize(400, 400)  # width, height
root.geometry("500x720+0+0")
root.iconbitmap("icon.ico")

root.grid_columnconfigure((0, 1, 2), weight=1)
root.grid_rowconfigure((0, 1, 2), weight=1)

# Create button to generate meal plan
generate_mealplan_button = ctk.CTkButton(root, text="Generate Meal Plan", command=display_mealplan, fg_color='teal', text_color='white')
generate_mealplan_button.grid(row=2, column=1, padx=5, pady=0, sticky="ew")

add_recipe_button = ctk.CTkButton(root, text="Add new recipe", command=pressed_add_recipe, fg_color='teal', text_color='white')
add_recipe_button.grid(row=2, column=0, padx=5, pady=0, sticky="ew")

quit_button = ctk.CTkButton(root, text='quit', command=quit, fg_color='teal', text_color='white')
quit_button.grid(row=2, column=2, padx=5, pady=0, sticky="ew")

# Label to display the meal plan
mealplan_label = ctk.CTkLabel(root, text="", justify="center", font=("Helvetica", 16))
mealplan_label.grid(row=0, column=0, padx=0, pady=0, columnspan=3, sticky="ew")

display_mealplan()
root.mainloop()

