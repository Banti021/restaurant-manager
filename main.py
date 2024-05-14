import logging
import os

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


def manage_raports():
    Sales.display_interaction_menu()


def main():
    logging.basicConfig(level=logging.INFO)
    os.environ['TERM'] = 'xterm-256color'

    options = [
        ("Zarządzaj menu restauracji", manage_restaurant_menu),
        ("Obsługa zamówień", manage_orders_menu),
        ("Zarządzanie zapasami", manage_inventory),
        ("Raporty sprzedaży", manage_raports),
        ("Wyjście", exit)
    ]

    menu_handler = InteractiveMenuHandler(options)
    menu_handler.run()


if __name__ == '__main__':
    logger.setup_logging()
    main()
