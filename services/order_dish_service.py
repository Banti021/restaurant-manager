import logging
from repository.order_dish_repository import OrderDishRepositoryManager


class OrderDishService:
    @staticmethod
    def get_order_dish(order_id: int, dish_id: int):
        with OrderDishRepositoryManager() as repository:
            return repository.get_order_dish(order_id, dish_id)

    @staticmethod
    def get_order_dishes(order_id: int):
        with OrderDishRepositoryManager() as repository:
            return repository.get_order_dishes(order_id)

    @staticmethod
    def create_order_dish(order_id: int, dish_id: int, quantity: int):
        with OrderDishRepositoryManager() as repository:
            return repository.create_order_dish(order_id, dish_id, quantity)

    @staticmethod
    def update_order_dish(order_id: int, dish_id: int, quantity: int):
        with OrderDishRepositoryManager() as repository:
            return repository.update_order_dish(order_id, dish_id, quantity)

    @staticmethod
    def delete_order_dish(order_id: int):
        logging.debug(f"Deleting order dish with order_id: {order_id}")
        with OrderDishRepositoryManager() as repository:
            return repository.delete_order_dish_id(order_id)
