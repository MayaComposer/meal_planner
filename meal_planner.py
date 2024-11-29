import pandas as pd
import numpy as np
import random
import customtkinter as ctk

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def read_data() -> pd.DataFrame:
    # Open excel file
    file = pd.ExcelFile('meals.xlsx')
    print('data read')
    df = pd.read_excel(file, index_col=0, header=0, keep_default_na=False)
    return df

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

    #print('mealplan generated')

    return meals

def write_to_file(text: str) -> None:
    with open("output.txt", "w") as file:
        file.write(text)

def add_recipe() -> None:
    print('here a recipe would be added')

def remove_duplicates(input_list: list) -> list:

    # Sample list with duplicate strings
    original_list = input_list

    # Remove duplicates using a set
    unique_list = list(set(original_list))

    #print('unique list: ' + str(unique_list))
    return unique_list

def configure_shopping_list() -> str:
    shopping_list_text = 'Shopping list: \n'
    
    for ingredient in shopping_list:
        shopping_list_text += f'- {ingredient}\n'
    return shopping_list_text

shopping_list_string = ''
shopping_list = []

def display_mealplan() -> None:
    meals = generate_mealplan()
    mealplan_text = ''

    global shopping_list
    global shopping_list_string
    shopping_list = []
    shopping_list_string = ''

    for count, meal in enumerate(meals):
        #meal plan
        mealplan_text += f'{days[count]}: \n{meal.Index} ({meal.category})\n'
        mealplan_text += f'Ingredients: {meal.ingredients} {meal.fresh_ingredients}\n\n'

        #shopping list
        shopping_list_string += f'{meal.ingredients}{meal.fresh_ingredients}'
        shopping_list_string = shopping_list_string.replace(' ', '')
        shopping_list = shopping_list_string.split(',') #returns a list
        shopping_list = list(filter(None, shopping_list))
    
    mealplan_label.configure(text=mealplan_text)


    #configure shopping list
    shopping_list = remove_duplicates(shopping_list)

    shopping_list_text = configure_shopping_list()

    #also add to file
    write_to_file(mealplan_text+shopping_list_text)




# Set up customtkinter window
root = ctk.CTk()
root.title("Meal Planner")
root.minsize(400, 400)  # width, height
root.geometry("500x720+0+0")
root.iconbitmap("icon.ico")

root.grid_columnconfigure(0, weight=1)

# Create button to generate meal plan
generate_mealplan_button = ctk.CTkButton(root, text="Generate Meal Plan", command=display_mealplan, fg_color='teal', text_color='white')
generate_mealplan_button.grid(row=0, column=0, padx=10, pady=10)

add_recipe_button = ctk.CTkButton(root, text="Add new recipe", command=add_recipe, fg_color='teal', text_color='white')
add_recipe_button.grid(row=1, column=0, padx=10, pady=10)

quit_button = ctk.CTkButton(root, text='quit', command=quit, fg_color='teal', text_color='white')
quit_button.grid(row=0, column=1, padx=0, pady=0)

# Label to display the meal plan
mealplan_label = ctk.CTkLabel(root, text="", justify="center", font=("Helvetica", 18))
mealplan_label.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

root.mainloop()

