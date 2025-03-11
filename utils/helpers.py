from collections import OrderedDict
import datetime

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def remove_duplicates(input_list: list) -> list:
    return list(OrderedDict.fromkeys(input_list))

def shopping_list_to_text(shopping_list) -> str:
    shopping_list_text = 'Shopping list: \n'
    for ingredient in shopping_list:
        shopping_list_text += f'- {ingredient}\n'
    return shopping_list_text

def write_to_file(text: str, file_path: str = "output.txt") -> None:
    with open(file_path, "w") as file:
        file.write(text)

def shopping_list_to_string(meals) -> str:
    shopping_list = []
    for meal in meals:
        all_ingredients = meal.ingredients + meal.fresh_ingredients
        ingredients = all_ingredients.replace(' ', '')
        ingredients = ingredients.split(',')
        if '' in ingredients:
            ingredients.remove('')
        shopping_list.append(list(ingredients))

    shopping_list_string = ''
    #for each set of ingredients in shopping_list
    #get integer place in shopping_list
    #shopping_list_string += Days[int] 
    for meal in shopping_list:
        shopping_list_string += f'\n {days[shopping_list.index(meal)]} \n'
        for ingredient in meal:
            shopping_list_string += f'- {ingredient} \n'
    return shopping_list_string

def configure_mealplan_text(meals):
    
    # date.isocalendar() 
    # Return a named tuple object with three components: year, week and weekday.
    #add 1 to week because we generate on sunday

    week = 'Week ' + str(datetime.datetime.now().isocalendar()[1])

    if datetime.datetime.now().isocalendar()[2] == 7:
        week = 'Week ' + str(datetime.datetime.now().isocalendar()[1] + 1)
    else:
        week = 'Week ' + str(datetime.datetime.now().isocalendar()[1])
    #instead implement:
    #if day == sunday
    #week = week + 1

    
    mealplan_text: str = ''
    mealplan_text += week
    mealplan_text += '\n'
    for count, meal in enumerate(meals):
        mealplan_text += f'{days[count]}: \n{meal.Index} ({meal.category})\n'
        mealplan_text += f'Ingredients: {meal.ingredients} {meal.fresh_ingredients}\n'
        mealplan_text += f'Instructions: {meal.instructions}\n\n'
    return mealplan_text

def main() -> None:
    from data.processdata import read_data, sort_recipes, generate_mealplan, add_recipe
    df = read_data()
    fish_recipes, meat_recipes, veg_recipes = sort_recipes(df)
    meals = generate_mealplan(fish_recipes, meat_recipes, veg_recipes)
    mealplan_text = configure_mealplan_text(meals)
    shopping_list_text = shopping_list_to_string(meals)
    write_to_file(mealplan_text + shopping_list_text)

        
if __name__ == "__main__":
    main()