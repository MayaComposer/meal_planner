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

# root = Tk()
# root.title("Tk Example")
# root.minsize(400, 400)  # width, height
# root.geometry("300x300+50+50")

# # Create Label in our window
# text = Label(root, text="fooooooooood")
# text.pack()
# text2 = Label(root, text="fooood")
# text2.pack()
# root.mainloop()

#open excel file
file = pd.ExcelFile('meals.xlsx')

column_names = ['Recipe', 'Difficulty', 'M/F/V', 'Ingredients']

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

meals = []

#read excel sheet into dataframe
df = pd.read_excel(file, index_col=0, header=0, keep_default_na=False)

fish_recipes = []
meat_recipes = []
veg_recipes = []


#iterate over dataframe and add recipes to lists based on category
for row in df.itertuples():
    if row.category == 'f':
        fish_recipes.append(row)
    if row.category == 'm':
        meat_recipes.append(row)
    if row.category == 'v':
        veg_recipes.append(row)

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

with open("output.txt", "w") as f:
    count = 0
    for x in meals:
        f.write(days[count])
        f.write('\n')
        f.write(str(x.Index) + ' (' + str(x.category) + ')')
        f.write('\n')
        f.write('Ingredients: ' + str(x.ingredients + ' ' + x.fresh_ingredients))
        f.write('\n')
        f.write('\n')
        count += 1

    f.write('Shopping list: ')
    for x in meals:
        f.write(str(x.ingredients + ' ' + x.fresh_ingredients + ' '))

print('meal plan generated')