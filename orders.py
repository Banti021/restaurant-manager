import logging
from collections import Counter

from models.order import Order
from utils.console_manager import ConsoleManager
from utils.data_loader import DataLoader
from utils.interactive_menu_handler import InteractiveMenuHandler
from utils.order_manager import OrderManager
from services.order_service import OrderService
from services.dish_service import DishService
from services.drink_service import DrinkService
from services.order_dish_service import OrderDishService
from services.order_drink_service import OrderDrinkService


class Orders:
    @staticmethod
    def display_interaction_menu():
        options = [
            ("Wyświetl otwarte zamówienia", Orders.display_open_orders),
            ("Dodaj zamówienie", Orders.add_order),
            ("Aktualizuj zamówienie", Orders.update_order),
            ("Usuń zamówienie", Orders.remove_order),
            ("Powrót", None)
        ]
        menu_handler = InteractiveMenuHandler(options)
        menu_handler.run()

    @staticmethod
    def display_open_orders():
        try:
            orders = OrderService.get_open_orders()
            ConsoleManager.clear_screen()
            ConsoleManager.display_message("Otwarte zamówienia:")

            for order in orders:
                ConsoleManager.display_message(str(order))

            input("Naciśnij Enter aby wrócić do menu...")
            ConsoleManager.clear_screen()

        except Exception as e:
            logging.error(f"Nie udało się wyświetlić zamówień: {e}")
            ConsoleManager.display_message(f"Nie udało się wyświetlić zamówień: {e}")

    @staticmethod
    def add_order():
        try:
            customer, total, dishes, drinks = OrderManager.create_order()
            order = OrderService.create_order(customer, total)
            order_id = order.id
            dish_counts = Orders.count_quantity(dishes)
            drink_counts = Orders.count_quantity(drinks)

            for dish_id, quantity in dish_counts.items():
                OrderDishService.create_order_dish(order_id, dish_id, quantity)

            for drink_id, quantity in drink_counts.items():
                OrderDrinkService.create_order_drink(order_id, drink_id, quantity)

            ConsoleManager.display_message("Zamówienie zostało dodane.")
        except Exception as e:
            logging.error(f"Nie udało się dodać zamówienia: {e}")
            ConsoleManager.display_message(f"Nie udało się dodać zamówienia: {e}")

    @staticmethod
    def count_quantity(items: list[int]) -> dict[int, int]:
        return dict(Counter(items))

    @staticmethod
    def remove_order():
        try:
            orders = DataLoader.load_items('data/orders.json', Order)
            for order in orders:
                ConsoleManager.display_message(str(order))

            order_id = ConsoleManager.get_input("Podaj id zamówienia do usunięcia: ")
            OrderManager.delete_order(order_id)
            ConsoleManager.display_message("Zamówienie zostało usunięte.")
        except Exception as e:
            logging.error(f"Nie udało się usunąć zamówienia: {e}")
            ConsoleManager.display_message(f"Nie udało się usunąć zamówienia: {e}")

    @staticmethod
    def update_order():
        try:
            orders = DataLoader.load_items('data/orders.json', Order)
            for order in orders:
                ConsoleManager.display_message(str(order))

            order_id = ConsoleManager.get_input("Podaj id zamówienia do zaktualizowania: ")
            OrderManager.update_order(order_id)
            ConsoleManager.display_message("Zamówienie zostało zaktualizowane.")
        except Exception as e:
            logging.error(f"Nie udało się zaktualizować zamówienia: {e}")
            ConsoleManager.display_message(f"Nie udało się zaktualizować zamówienia: {e}")
