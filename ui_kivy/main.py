from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from data.processdata import read_data, sort_recipes, generate_mealplan, add_recipe, save_data
from utils.helpers import shopping_list_to_string, configure_mealplan_text, write_to_file

class MainWindow(MDScreen):

    df = read_data()
    fish_recipes, meat_recipes, veg_recipes = sort_recipes(df)
    shopping_list_string = ''
    shopping_list = []
    meals = []

    def do_action(self):
        print('Button pressed')

    def display_mealplan(self):
        self.meals = generate_mealplan(self.fish_recipes, self.meat_recipes, self.veg_recipes)

        mealplan_text = configure_mealplan_text(self.meals)
        self.ids.mealplan_label.text = mealplan_text

        shopping_list_text = shopping_list_to_string(self.meals)
        write_to_file(mealplan_text + shopping_list_text)

    def pressed_add_recipe(self):
        self.df = add_recipe(self.df)
        self.fish_recipes, self.meat_recipes, self.veg_recipes = sort_recipes(self.df)

    def quit_app(self) -> None: 
        save_data(self.df)
        quit()

class MealplannerApp(MDApp):
    def build(self):
        Window.size = (360, 640)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Olive"  # "Purple", "Red"
        root = ScreenManager()
        root.add_widget(MainWindow(name='main'))
        return root

    def on_start(self):
        main_screen = self.root.get_screen('main') # type: ignore
        main_screen.display_mealplan()

if __name__ == '__main__':
    MealplannerApp().run()