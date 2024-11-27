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

# #for col in 
# for col_name in dataframe:
#     #check if the column starts with recipe
#     if col_name.startswith('Recipe'):
#         loc = dataframe.columns.get_loc(col_name)
#         new_dataframe = dataframe.iloc[:,loc:loc+5] #dataframe from recipe location+5, end of recipe table

#         recipes.append(new_dataframe) #add dataframes to list
#         # print(loc)
#         # print(new_dataframe)
#         # print('\n')

#pick 7 recipes from recipes list and put into meal_plan list
# random.shuffle(recipes)


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

#1. pick 2 fish recipes
#2. pick 1 meat recipe
#3. pick 4 vegetarian recipes
#4. add it to a list
#5. check list to see if there is overlap between fresh ingredients, if so, make sure those recipes are right after each other.
#6. profit

recipes = dataframe.to_dict()

output = open('output.txt', 'w')

print(recipes, file=output)

output.close()

