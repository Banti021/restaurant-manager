from models.dish import Dish
from models.drink import Drink
from utils.console_manager import ConsoleManager
from utils.data_loader import DataLoader


class MenuManager:
    @staticmethod
    def get_dish_details():
        name = ConsoleManager.get_input("Podaj nazwę dania: ")
        price = float(ConsoleManager.get_input("Podaj cenę dania: "))
        is_dish_of_the_day = MenuManager.is_dish_of_the_day(ConsoleManager.get_input("Czy danie dnia (t/n):"))
        return name, price, is_dish_of_the_day

    @staticmethod
    def get_drink_details():
        name = ConsoleManager.get_input("Podaj nazwę napoju: ")
        price = float(ConsoleManager.get_input("Podaj cenę napoju: "))
        return name, price

    @staticmethod
    def save_new_dish(dish: Dish):
        dishes = DataLoader.load_items('data/dishes.json', Dish)
        dishes.append(dish)
        DataLoader.save_data('data/dishes.json', dishes)

    @staticmethod
    def save_new_drink(drink: Drink):
        drinks = DataLoader.load_items('data/drinks.json', Drink)
        drinks.append(drink)
        DataLoader.save_data('data/drinks.json', drinks)

    @staticmethod
    def delete_dish(dish_id):
        dishes = DataLoader.load_items('data/dishes.json', Dish)
        dishes = [dish for dish in dishes if dish.id != dish_id]
        DataLoader.save_data('data/dishes.json', dishes)

    @staticmethod
    def delete_drink(drink_id):
        drinks = DataLoader.load_items('data/drinks.json', Drink)
        drinks = [drink for drink in drinks if drink.id != drink_id]
        DataLoader.save_data('data/drinks.json', drinks)

    @staticmethod
    def update_dish(dish_id, new_dish: Dish):
        dishes = DataLoader.load_items('data/dishes.json', Dish)
        dishes = [new_dish if dish.id == dish_id else dish for dish in dishes]
        DataLoader.save_data('data/dishes.json', dishes)

    @staticmethod
    def update_drink(drink_id, new_drink: Drink):
        drinks = DataLoader.load_items('data/drinks.json', Drink)
        drinks = [new_drink if drink.id == drink_id else drink for drink in drinks]
        DataLoader.save_data('data/drinks.json', drinks)

    @staticmethod
    def is_dish_of_the_day(answer):
        if answer == 't':
            return True

        return False
