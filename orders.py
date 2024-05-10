import logging

from models.order import Order
from utils.console_manager import ConsoleManager
from utils.data_loader import DataLoader
from utils.interactive_menu_handler import InteractiveMenuHandler
from utils.order_manager import OrderManager


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
        orders = DataLoader.load_items('data/orders.json', Order)
        orders = [order for order in orders if not order.is_closed]

        ConsoleManager.clear_screen()
        ConsoleManager.display_message("Otwarte zamówienia:")
        for order in orders:
            ConsoleManager.display_message(str(order))

        input("Naciśnij Enter aby wrócić do menu...")
        ConsoleManager.clear_screen()

    @staticmethod
    def add_order():
        try:
            customer, total, dishes, drinks, status = OrderManager.get_order_details()
            order_id = DataLoader.get_next_id('data/orders.json')
            order = Order(order_id, customer, total, dishes, drinks, status)
            OrderManager.save_new_order(order)
            ConsoleManager.display_message("Zamówienie zostało dodane.")
        except Exception as e:
            logging.error(f"Nie udało się dodać zamówienia: {e}")
            ConsoleManager.display_message(f"Nie udało się dodać zamówienia: {e}")

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



