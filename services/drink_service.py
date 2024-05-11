from repository.drink_repository import DrinkRepositoryManager


class DrinkService:
    @staticmethod
    def get_all_drinks():
        with DrinkRepositoryManager() as repository:
            return repository.get_all_drinks()

    @staticmethod
    def get_drink_by_id(drink_id: int):
        with DrinkRepositoryManager() as repository:
            return repository.get_drink_by_id(drink_id)

    @staticmethod
    def get_drink_by_name(name: str):
        with DrinkRepositoryManager() as repository:
            return repository.get_drink_by_name(name)

    @staticmethod
    def create_drink(name: str, price: float, is_alcoholic: str, alcohol_content: int):
        with DrinkRepositoryManager() as repository:
            return repository.create_drink(name, price, is_alcoholic == 't', alcohol_content)

    @staticmethod
    def update_drink(drink_id: int, name: str, price: float, is_alcoholic: str, alcohol_content: int):
        with DrinkRepositoryManager() as repository:
            return repository.update_drink(drink_id, name, price, is_alcoholic == 't', alcohol_content)

    @staticmethod
    def delete_drink(drink_id: int):
        with DrinkRepositoryManager() as repository:
            return repository.delete_drink(drink_id)
