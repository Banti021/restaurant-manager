from models import dish, drink
from models.dish import Dish
from models.drink import Drink
from models.order import Order
from utils.console_manager import ConsoleManager
from utils.data_loader import DataLoader


class OrderManager:
    @staticmethod
    def get_order_details():
        dishes = DataLoader.load_items('data/dishes.json', Dish)
        drinks = DataLoader.load_items('data/drinks.json', Drink)

        ConsoleManager.display_message("Dostępne dania i napoje:")
        for dishes in dishes:
            ConsoleManager.display_message(str(dish))
        for drinks in drinks:
            ConsoleManager.display_message(str(drink))

        customer = ConsoleManager.get_input("Podaj nazwę klienta: ")
        total = float(ConsoleManager.get_input("Podaj łączną cenę zamówienia: "))
        dishes = ConsoleManager.get_input("Podaj id dań (oddzielone przecinkiem): ").split(',')
        drinks = ConsoleManager.get_input("Podaj id napojów (oddzielone przecinkiem): ").split(',')
        status = True

        return customer, total, dishes, drinks, status

    @staticmethod
    def save_new_order(order: Order):
        orders = DataLoader.load_items('data/orders.json', Order)
        orders.append(order)
        DataLoader.save_data('data/orders.json', orders)

    @staticmethod
    def delete_order(order_id):
        orders = DataLoader.load_items('data/orders.json', Order)
        orders = [order for order in orders if order.id != order_id]
        DataLoader.save_data('data/orders.json', orders)

    @staticmethod
    def update_order(order_id):
        orders = DataLoader.load_items('data/orders.json', Order)
        orders = [order if order.id == order_id else order for order in orders]
        DataLoader.save_data('data/orders.json', orders)