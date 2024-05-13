from models.order import Order
from services.order_service import OrderService
from utils.console_manager import ConsoleManager
from utils.data_loader import DataLoader
from services.drink_service import DrinkService
from services.dish_service import DishService


class OrderManager:
    @staticmethod
    def create_order():
        dishes = DishService.get_all_dishes()
        drinks = DrinkService.get_all_drinks()

        ConsoleManager.display_message("Dostępne dania i napoje:")
        ConsoleManager.display_message("<------Dania------>")
        for DISH in dishes:
            ConsoleManager.display_message(str(DISH))
        ConsoleManager.display_message("<------Napoje------>")
        for DRINK in drinks:
            ConsoleManager.display_message(str(DRINK))

        customer = ConsoleManager.get_input("Podaj nazwę klienta: ")
        dishes = ConsoleManager.get_input("Podaj id dań (oddzielone przecinkiem): ").split(',')
        drinks = ConsoleManager.get_input("Podaj id napojów (oddzielone przecinkiem): ").split(',')

        dish_cost = sum([OrderManager._get_dish_cost(int(dish_id)) for dish_id in dishes])
        drink_cost = sum([OrderManager._get_drink_cost(int(drink_id)) for drink_id in drinks])
        total = dish_cost + drink_cost

        return customer, total, dishes, drinks

    @staticmethod
    def _get_dish_cost(dish_id: int):
        dish_db = DishService.get_dish_by_id(dish_id)
        return dish_db.price

    @staticmethod
    def _get_drink_cost(drink_id: int):
        drink_db = DrinkService.get_drink_by_id(drink_id)
        return drink_db.price

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
    def update_order(order_id: int, status: int):
        order = OrderService.update_order(order_id, status)
        return order

