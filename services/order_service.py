import logging
from repository.order_repository import OrderRepositoryManager
from services.order_dish_service import OrderDishService
from services.order_drink_service import OrderDrinkService


class OrderService:
    @staticmethod
    def get_all_orders():
        with OrderRepositoryManager() as repository:
            return repository.get_all_orders()

    @staticmethod
    def get_order_by_id(order_id: int):
        with OrderRepositoryManager() as repository:
            return repository.get_order_by_id(order_id)

    @staticmethod
    def get_open_orders():
        with OrderRepositoryManager() as repository:
            return repository.get_open_orders()

    @staticmethod
    def get_order_by_customer(customer: str):
        with OrderRepositoryManager() as repository:
            return repository.get_order_by_customer(customer)

    @staticmethod
    def get_order_by_date(order_date: str):
        with OrderRepositoryManager() as repository:
            return repository.get_order_by_date(order_date)

    @staticmethod
    def create_order(customer: str, total: float):
        logging.debug(f"Creating order for customer: {customer} with total: {total}")
        with OrderRepositoryManager() as repository:
            order = repository.create_order(customer, total)
            logging.debug(f"Created order: {order}")
            return order

    @staticmethod
    def update_order(order_id: int, status: int):
        logging.debug(f"Updating order with id: {order_id}, with status: {status}")
        with OrderRepositoryManager() as repository:
            order = repository.update_order(order_id, status)
            logging.debug(f"Updated order: {order}")
            return order

    @staticmethod
    def delete_order(order_id: int):
        logging.debug(f"Deleting order with id: {order_id}")
        OrderDishService.delete_order_dish(order_id)
        OrderDrinkService.delete_order_drink(order_id)

        with OrderRepositoryManager() as repository:
            order = repository.delete_order(order_id)
            logging.debug(f"Deleted order: {order}")
