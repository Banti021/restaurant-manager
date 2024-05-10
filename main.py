import logging

import logger
from inventory import Inventory
from menu import Menu
from orders import Orders
from sales import Sales
from utils.interactive_menu_handler import InteractiveMenuHandler


def manage_restaurant_menu():
    Menu.display_interaction_menu()


def manage_orders_menu():
    Orders.display_interaction_menu()


def manage_inventory():
    Inventory.manage_inventory()


def generate_reports():
    Sales.generate_sales_reports()


def main():
    logging.basicConfig(level=logging.INFO)

    options = [
        ("Zarządzaj menu restauracji", manage_restaurant_menu),
        ("Obsługa zamówień", manage_orders_menu),
        ("Zarządzanie zapasami", manage_inventory),
        ("Generuj raporty sprzedaży", generate_reports),
        ("Wyjście", exit)
    ]

    menu_handler = InteractiveMenuHandler(options)
    menu_handler.run()


if __name__ == '__main__':
    logger.setup_logging()
    main()
