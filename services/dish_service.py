from models.dish import Dish
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
        new_dish = Dish(name=name, price=price, dish_of_the_day=dish_of_the_day)
        with DishRepositoryManager() as repo:
            return repo.create_dish(new_dish)

    @staticmethod
    def update_dish(dish: Dish):
        with DishRepositoryManager() as repository:
            return repository.update_dish(dish)

    @staticmethod
    def delete_dish(dish: Dish):
        with DishRepositoryManager() as repository:
            return repository.delete_dish(dish)