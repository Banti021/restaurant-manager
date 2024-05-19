import logging
import re

from services.order_service import OrderService
from utils.console_manager import ConsoleManager
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
        dish_ids = ConsoleManager.get_input("Podaj id dań (oddzielone przecinkiem): ").split(',')
        drink_ids = ConsoleManager.get_input("Podaj id napojów (oddzielone przecinkiem): ").split(',')

        try:
            dish_ids_int = OrderManager._filter_and_convert(dish_ids)
            drink_ids_int = OrderManager._filter_and_convert(drink_ids)

            # Get all dish and drink ids from database
            db_drink_objs = DrinkService.get_all_drinks()
            db_dish_objs = DishService.get_all_dishes()

            db_drink_ids = OrderManager._convert_object_to_int_list(db_drink_objs)
            db_dish_ids = OrderManager._convert_object_to_int_list(db_dish_objs)

            # Check if all dish and drink ids are valid
            drink_ids_actual = [drink_id for drink_id in drink_ids_int if drink_id in db_drink_ids]
            dish_ids_actual = [dish_id for dish_id in dish_ids_int if dish_id in db_dish_ids]

            drink_cost = sum(OrderManager._get_drink_cost(drink_id) for drink_id in drink_ids_actual)
            dish_cost = sum(OrderManager._get_dish_cost(dish_id) for dish_id in dish_ids_actual)

            total = dish_cost + drink_cost
        except ValueError:
            ConsoleManager.display_message("Podano nieprawidłowe id dań lub napojów.")
            logging.error("Błąd podczas parsowania id dań i napojów.")
            return None

        return customer, total, dish_ids_actual, drink_ids_actual


    @staticmethod
    def _convert_object_to_int_list(object_list: list) -> list[int]:
        return [obj.id for obj in object_list]

    @staticmethod
    def _filter_and_convert(input_list: list[str]):
        filtered_input = [re.sub(r'[^0-9]', '', item) for item in input_list]
        return [int(id_str) for id_str in filtered_input if id_str.strip()]

    @staticmethod
    def _get_dish_cost(dish_id: int):
        dish_db = DishService.get_dish_by_id(dish_id)
        return dish_db.price

    @staticmethod
    def _get_drink_cost(drink_id: int):
        drink_db = DrinkService.get_drink_by_id(drink_id)
        return drink_db.price

    @staticmethod
    def update_order(order_id: int, status: int):
        order = OrderService.update_order(order_id, status)
        return order
