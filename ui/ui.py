import customtkinter as ctk
from data.processdata import read_data, sort_recipes, generate_mealplan, add_recipe
from utils.helpers import configure_shopping_list, configure_mealplan_text, write_to_file

class MealPlannerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Meal Planner")
        self.minsize(400, 400)
        self.geometry("500x720+0+0")
        self.iconbitmap("icon.ico")

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.mealplan_label = ctk.CTkLabel(self, text="", justify="center", font=("Helvetica", 16))
        self.mealplan_label.grid(row=0, column=0, padx=0, pady=0, columnspan=3, sticky="ew")

        self.generate_mealplan_button = ctk.CTkButton(self, text="Generate Meal Plan", command=self.display_mealplan, fg_color='teal', text_color='white')
        self.generate_mealplan_button.grid(row=2, column=1, padx=5, pady=0, sticky="ew")

        self.add_recipe_button = ctk.CTkButton(self, text="Add new recipe", command=self.pressed_add_recipe, fg_color='teal', text_color='white')
        self.add_recipe_button.grid(row=2, column=0, padx=5, pady=0, sticky="ew")

        self.quit_button = ctk.CTkButton(self, text='quit', command=self.quit, fg_color='teal', text_color='white')
        self.quit_button.grid(row=2, column=2, padx=5, pady=0, sticky="ew")

        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.df = read_data('./data/meals.xlsx')
        self.fish_recipes, self.meat_recipes, self.veg_recipes = sort_recipes(self.df)
        self.shopping_list_string = ''
        self.shopping_list = []

        self.display_mealplan()

    def display_mealplan(self):
        meals = generate_mealplan(self.fish_recipes, self.meat_recipes, self.veg_recipes)

        mealplan_text = configure_mealplan_text(meals)
        self.mealplan_label.configure(text=mealplan_text)

        shopping_list_text = configure_shopping_list(meals)
        write_to_file(mealplan_text + shopping_list_text)

    def pressed_add_recipe(self):
        self.df = add_recipe(self.df)
        self.fish_recipes, self.meat_recipes, self.veg_recipes = sort_recipes(self.df)

def main():
    app = MealPlannerApp()
    app.mainloop()

if __name__ == "__main__":
    main()