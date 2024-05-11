import logging

from services.dish_service import DishService
from services.drink_service import DrinkService
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
            ("Aktualizuj napój na menu", Menu.update_drink_on_menu),
            ("Ustaw danie dnia", Menu.set_dish_of_the_day),
            ("Powrót", lambda: "back")
        ]
        menu_handler = InteractiveMenuHandler(options)
        menu_handler.run()

    @staticmethod
    def display_restaurant_menu():
        dishes = DishService.get_all_dishes()
        drinks = DrinkService.get_all_drinks()

        ConsoleManager.clear_screen()
        ConsoleManager.display_message("Aktualne Menu:")

        ConsoleManager.display_message("Dania:")
        for dish in dishes:
            ConsoleManager.display_message(str(dish))

        ConsoleManager.display_message("Napoje:")
        for drink in drinks:
            ConsoleManager.display_message(str(drink))

        input("Naciśnij Enter aby wrócić do menu...")
        ConsoleManager.clear_screen()

    @staticmethod
    def add_dish_to_menu():
        try:
            name, price, is_dish_of_the_day = MenuManager.get_dish_details()
            DishService.create_dish(name, price, is_dish_of_the_day)
            ConsoleManager.display_message("Danie zostało dodane do menu")
        except Exception as e:
            logging.exception(f"Error while adding dish to menu: {e}")

    @staticmethod
    def add_drink_to_menu():
        try:
            name, price, is_alcoholic, alcohol_content = MenuManager.get_drink_details()
            DrinkService.create_drink(name, price, is_alcoholic, alcohol_content)
            ConsoleManager.display_message("Napój został dodany do menu")
        except Exception as e:
            logging.exception(f"Error while adding drink to menu: {e}")

    @staticmethod
    def remove_dish_from_menu():
        try:
            dishes = DishService.get_all_dishes()
            for dish in dishes:
                ConsoleManager.display_message(str(dish))

            dish_id = int(ConsoleManager.get_input("Podaj id dania do usunięcia: "))
            DishService.delete_dish(dish_id)
            ConsoleManager.display_message("Danie zostało usunięte z menu")
        except Exception as e:
            logging.exception(f"Error while removing dish from menu: {e}")

    @staticmethod
    def remove_drink_from_menu():
        try:
            drinks = DrinkService.get_all_drinks()
            for drink in drinks:
                ConsoleManager.display_message(str(drink))

            drink_id = int(ConsoleManager.get_input("Podaj id napoju do usunięcia: "))
            DrinkService.delete_drink(drink_id)
        except Exception as e:
            logging.exception(f"Error while removing drink from menu: {e}")

    @staticmethod
    def update_dish_on_menu():
        try:
            dishes = DishService.get_all_dishes()
            for dish in dishes:
                ConsoleManager.display_message(str(dish))

            dish_id = int(ConsoleManager.get_input("Podaj id dania do aktualizacji: "))
            name, price, is_dish_of_the_day = MenuManager.get_dish_details()
            DishService.update_dish(dish_id, name, price, is_dish_of_the_day)
        except Exception as e:
            logging.exception(f"Error while updating dish on menu: {e}")

    @staticmethod
    def update_drink_on_menu():
        try:
            drinks = DrinkService.get_all_drinks()
            for drink in drinks:
                ConsoleManager.display_message(str(drink))

            drink_id = int(ConsoleManager.get_input("Podaj id napoju do aktualizacji: "))
            name, price, is_alcoholic, alcohol_content = MenuManager.get_drink_details()
            DrinkService.update_drink(drink_id, name, price, is_alcoholic, alcohol_content)
        except Exception as e:
            logging.exception(f"Error while updating drink on menu: {e}")

    @staticmethod
    def set_dish_of_the_day():
        try:
            dishes = DishService.get_all_dishes()
            for dish in dishes:
                ConsoleManager.display_message(str(dish))

            dish_id = int(ConsoleManager.get_input("Podaj id dania dnia: "))
            DishService.set_dish_of_the_day(dish_id)
        except Exception as e:
            logging.exception(f"Error while setting dish of the day: {e}")
