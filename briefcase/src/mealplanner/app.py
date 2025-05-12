"""
A meal planner app
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class Mealplanner(toga.App):
    def startup(self):
        """Construct and show the Toga application."""
        # Create a main box to hold widgets
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Create a button and add it to the main box
        button = toga.Button(
            "Click me", 
            on_press=self.my_callback, 
            style=Pack(padding=10)
        )
        main_box.add(button)

        # Set up the main window
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def my_callback(self, widget):
        """Handle button press event."""
        print("Button clicked!")


def main() -> Mealplanner:
    return Mealplanner()
