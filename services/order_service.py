from repository.order_repository import OrderRepositoryManager


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
    def get_order_by_customer(customer: str):
        with OrderRepositoryManager() as repository:
            return repository.get_order_by_customer(customer)

    @staticmethod
    def get_order_by_date(order_date: str):
        with OrderRepositoryManager() as repository:
            return repository.get_order_by_date(order_date)

    @staticmethod
    def create_order(customer: str, order_date: str):
        with OrderRepositoryManager() as repo:
            return repo.create_order(customer, order_date)

    @staticmethod
    def update_order(order_id: int, customer: str, order_date: str):
        with OrderRepositoryManager() as repository:
            return repository.update_order(order_id, customer, order_date)

    @staticmethod
    def delete_order(order_id: int):
        with OrderRepositoryManager() as repository:
            return repository.delete_order(order_id)
