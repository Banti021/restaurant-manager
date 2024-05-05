import logging

from utils.data_loader import DataLoader
from models.dish import Dish
from models.drink import Drink
from utils.console_manager import ConsoleManager
from utils.interactive_menu_handler import InteractiveMenuHandler
from utils.menu_manager import MenuManager


class Menu:
    @staticmethod
    def display_interaction_menu():
        options = [
            ("Wyświetl menu", Menu.display_restaurant_menu),
            ("Dodaj danie do menu", Menu.add_dish_to_menu),
            ("Dodaj napoj do menu", Menu.add_drink_to_menu),
            ("Usuń danie z menu", Menu.remove_dish_from_menu),
            ("Usuń napoj z menu", Menu.remove_drink_from_menu),
            ("Aktualizuj danie na menu", Menu.update_dish_on_menu),
            ("Ustaw danie dnia", Menu.set_dish_of_the_day),
            ("Powrót", None)
        ]
        menu_handler = InteractiveMenuHandler(options)
        menu_handler.run()

    @staticmethod
    def display_restaurant_menu():
        dishes = DataLoader.load_items('data/dishes.json', Dish)
        drinks = DataLoader.load_items('data/drinks.json', Drink)

        ConsoleManager.clear_screen()
        ConsoleManager.display_message("Aktualne Menu:")

        for dish in dishes:
            ConsoleManager.display_message(str(dish))
        for drink in drinks:
            ConsoleManager.display_message(str(drink))

        input("Naciśnij Enter aby wrócić do menu...")
        ConsoleManager.clear_screen()

    @staticmethod
    def add_dish_to_menu():
        try:
            name, price, is_dish_of_the_day = MenuManager.get_dish_details()
            dishes = DataLoader.load_items('data/dishes.json', Dish)
            dish_id = DataLoader.get_next_id(dishes)
            dish = Dish(dish_id, name, price, is_dish_of_the_day)
            MenuManager.save_new_dish(dish)
            logging.info(f"Dish added successfully: {name}")
        except Exception as e:
            logging.error(f"Failed to add dish: {e}")
            ConsoleManager.display_message("Error adding dish.")

    @staticmethod
    def add_drink_to_menu():
        name, price = MenuManager.get_drink_details()
        drink_id = DataLoader.get_next_id('data/drinks.json')
        drink = Drink(drink_id, name, price)
        MenuManager.save_new_drink(drink)

    @staticmethod
    def remove_dish_from_menu():
        dishes = DataLoader.load_items('data/dishes.json', Dish)
        for dish in dishes:
            ConsoleManager.display_message(str(dish))

        dish_id = int(ConsoleManager.get_input("Podaj id dania do usunięcia: "))
        MenuManager.delete_dish(dish_id)

    @staticmethod
    def remove_drink_from_menu():
        drinks = DataLoader.load_items('data/drinks.json', Drink)
        for drink in drinks:
            ConsoleManager.display_message(str(drink))

        drink_id = int(ConsoleManager.get_input("Podaj id napoju do usunięcia: "))
        MenuManager.delete_drink(drink_id)

    @staticmethod
    def update_dish_on_menu():
        dishes = DataLoader.load_items('data/dishes.json', Dish)
        for dish in dishes:
            ConsoleManager.display_message(str(dish))

        dish_id = int(ConsoleManager.get_input("Podaj id dania do aktualizacji: "))
        name, price, is_dish_of_the_day = MenuManager.get_dish_details()
        new_dish = Dish(dish_id, name, price, is_dish_of_the_day)
        MenuManager.update_dish(dish_id, new_dish)

    @staticmethod
    def set_dish_of_the_day():
        dishes = DataLoader.load_items('data/dishes.json', Dish)
        for dish in dishes:
            ConsoleManager.display_message(str(dish))

        dish_id = int(ConsoleManager.get_input("Podaj id dania dnia: "))
        dish = next((dish for dish in dishes if dish.id == dish_id), None)
        MenuManager.update_dish(dish_id, dish)
