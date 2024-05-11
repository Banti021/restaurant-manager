from repository.inventory_repository import InventoryRepositoryManager


class InventoryService:
    @staticmethod
    def get_all_inventory():
        with InventoryRepositoryManager() as repository:
            return repository.get_all_inventory()

    @staticmethod
    def get_inventory_by_id(inventory_id: int):
        with InventoryRepositoryManager() as repository:
            return repository.get_inventory_by_id(inventory_id)

    @staticmethod
    def get_inventory_by_name(name: str):
        with InventoryRepositoryManager() as repository:
            return repository.get_inventory_by_name(name)

    @staticmethod
    def create_inventory(name: str, quantity: int):
        with InventoryRepositoryManager() as repository:
            return repository.create_inventory(name, quantity)

    @staticmethod
    def update_inventory(inventory_id: int, name: str, quantity: int):
        with InventoryRepositoryManager() as repository:
            return repository.update_inventory(inventory_id, name, quantity)

    @staticmethod
    def delete_inventory(inventory_id: int):
        with InventoryRepositoryManager() as repository:
            return repository.delete_inventory(inventory_id)