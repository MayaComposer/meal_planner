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

column_names = ['Recipe', 'Difficulty', 'M/F/V', 'Ingredients', 'Time']

#list of recipes
recipes = []

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

meals = []

#read excel sheet into dataframe
dataframe = pd.read_excel(file, index_col=0, header=0, keep_default_na=False)

#open excel file
#for each column in excel file
#if the header is recipe, create a dataframe with names=column_names
#add dataframe to a list "recipes"

#for col in 
for col_name in dataframe:
    #check if the column starts with recipe
    if col_name.startswith('Recipe'):
        loc = dataframe.columns.get_loc(col_name)
        new_dataframe = dataframe.iloc[:,loc:loc+5] #dataframe from recipe location+5, end of recipe table

        recipes.append(new_dataframe) #add dataframes to list
        # print(loc)
        # print(new_dataframe)
        # print('\n')

#pick 7 recipes from recipes list and put into meal_plan list
random.shuffle(recipes)
for r in range(7):
    meals.append(recipes[r])
    print(meals[r])

output = open('output.txt', 'w')

#make a file with 7 meals

for r in range(7):
    print(str(r+1) + ' ' + days[r], file=output)
    print(meals[r], file=output)
    print('\n')

output.close()