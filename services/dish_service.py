from repository.dish_repository import DishRepositoryManager


class DishService:
    @staticmethod
    def get_all_dishes():
        with DishRepositoryManager() as repository:
            return repository.get_all_dishes()

    @staticmethod
    def get_dish_by_id(dish_id: int):
        with DishRepositoryManager() as repository:
            return repository.get_dish_by_id(dish_id)

    @staticmethod
    def get_dish_by_name(name: str):
        with DishRepositoryManager() as repository:
            return repository.get_dish_by_name(name)

    @staticmethod
    def create_dish(name: str, price: float, dish_of_the_day: bool):
        with DishRepositoryManager() as repository:
            return repository.create_dish(name, price, dish_of_the_day)

    @staticmethod
    def update_dish(dish_id: int, name: str, price: float, dish_of_the_day: bool):
        with DishRepositoryManager() as repository:
            return repository.update_dish(dish_id, name, price, dish_of_the_day)

    @staticmethod
    def set_dish_of_the_day(dish_id: int):
        with DishRepositoryManager() as repository:
            return repository.set_dish_of_the_day(dish_id)

    @staticmethod
    def delete_dish(dish_id: int):
        with DishRepositoryManager() as repository:
            return repository.delete_dish(dish_id)