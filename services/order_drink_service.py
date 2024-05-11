from repository.order_drink_repository import OrderDrinkRepositoryManager


class OrderDrinkService:
    @staticmethod
    def get_order_drink(order_id: int, drink_id: int):
        with OrderDrinkRepositoryManager() as repository:
            return repository.get_order_drink(order_id, drink_id)

    @staticmethod
    def get_order_drinks(order_id: int):
        with OrderDrinkRepositoryManager() as repository:
            return repository.get_order_drinks(order_id)

    @staticmethod
    def get_order_drink_quantity(order_id: int, drink_id: int):
        with OrderDrinkRepositoryManager() as repository:
            return repository.get_order_drink_quantity(order_id, drink_id)

    @staticmethod
    def create_order_drink(order_id: int, drink_id: int, quantity: int):
        with OrderDrinkRepositoryManager() as repository:
            return repository.create_order_drink(order_id, drink_id, quantity)

    @staticmethod
    def update_order_drink(order_id: int, drink_id: int, quantity: int):
        with OrderDrinkRepositoryManager() as repository:
            return repository.update_order_drink(order_id, drink_id, quantity)

    @staticmethod
    def delete_order_drink(order_id: int, drink_id: int):
        with OrderDrinkRepositoryManager() as repository:
            return repository.delete_order_drink(order_id, drink_id)

    @staticmethod
    def delete_order_drinks(order_id: int):
        with OrderDrinkRepositoryManager() as repository:
            return repository.delete_order_drinks(order_id)