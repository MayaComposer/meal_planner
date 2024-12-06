from collections import OrderedDict

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

def configure_shopping_list(meals) -> str:
    shopping_list = []
    shopping_list_string = ''
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for count, meal in enumerate(meals):
        shopping_list_string += f'{days[count]} \n {meal.ingredients},{meal.fresh_ingredients},'

    shopping_list_string = shopping_list_string.replace(' ', '')
    shopping_list = shopping_list_string.split(',')
    shopping_list = list(filter(None, shopping_list))

    shopping_list = remove_duplicates(shopping_list)
    shopping_list_text = shopping_list_to_text(shopping_list)
    return shopping_list_text

def configure_mealplan_text(meals):
    mealplan_text: str = ''
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for count, meal in enumerate(meals):
        mealplan_text += f'{days[count]}: \n{meal.Index} ({meal.category})\n'
        mealplan_text += f'Ingredients: {meal.ingredients} {meal.fresh_ingredients}\n\n'
    return mealplan_text