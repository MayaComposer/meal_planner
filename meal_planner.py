#list of recipes
#list of ingredients
# pick random recipe based on ingredients in pantry, 
#               only the fresh ingredients are needed to check. Herbs and stuff not really.
# then fill up the rest of the days of the week with recipes.
#create a shopping list 

import pandas as pd
import numpy as np
import random

#open excel file
file = pd.ExcelFile('meals.xlsx')

column_names = ['Recipe', 'Difficulty', 'M/F/V', 'Ingredients']

#list of recipes
recipes = []

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

meals = []

#read excel sheet into dataframe
df = pd.read_excel(file, index_col=0, header=0, keep_default_na=False)

# #1. pick a random recipe for monday
# #2. check the ingredients, and if use 1-3 of them to pick the next recipe
#check the fresh ingredients and use those to choose recipes so there is overlap between ingredients
# #3. pick a recipe for tuesday
# 4. take into account fish, meat, vegetarian

#1. loop through the recipes
#2. take 7 random recipes
#3. use different filters (I guess) to check if the recipes are correct
#for example, check there is a max of 2 fish recipes, and if there is more, replace with vegetarian ones until there is 2
#check overlap between fresh ingredients


#other method:

#1. pick 2 fish recipes ✅
#2. pick 1 meat recipe✅
#3. pick 4 vegetarian recipes✅
#4. add it to a list✅
#5. check list to see if there is overlap between fresh ingredients, if so, make sure those recipes are right after each other.

#recipes = dataframe.to_dict('index')


#filter recipes and add them to categories
#for each row, if it is a meat recipe, add to meat recipe list
#do the same for veg
#do the same for fish

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

