import json

from models.Dish import Dish
from models.Drink import Drink


class DataLoader:
    @staticmethod
    def load_dishes(filepath):
        """
        Loads dishes from a JSON file and returns a list of Dish objects.
        """
        try:
            with open(filepath, 'r') as file:
                dishes_data = json.load(file)
            return [Dish(dish['name'], dish['price'], dish.get('dish_of_the_day', False)) for dish in dishes_data]
        except FileNotFoundError:
            print(f"File not found: {filepath}")
            return []
        except json.JSONDecodeError:
            print("Failed to decode JSON.")
            return []

    @staticmethod
    def load_drinks(filepath):
        """
        Loads drinks from a JSON file and returns a list of Drink objects.
        """
        try:
            with open(filepath, 'r') as file:
                drinks_data = json.load(file)
            return [Drink(drink['name'], drink['price']) for drink in drinks_data]
        except FileNotFoundError:
            print(f"File not found: {filepath}")
            return []
        except json.JSONDecodeError:
            print("Failed to decode JSON.")
            return []

    @staticmethod
    def save_data(filepath, objects):
        """
        Saves a list of Dish or Drink objects to a JSON file.
        """
        try:
            with open(filepath, 'w') as file:
                json.dump([obj.__dict__ for obj in objects], file, indent=4)
        except IOError:
            print(f"Error saving data to file: {filepath}")
