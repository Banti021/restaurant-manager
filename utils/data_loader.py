import json
import logging


class DataLoader:
    @staticmethod
    def load_items(filepath, cls):
        """
        Generic method to load items from a JSON file and returns a list of objects.
        'cls' should be the class (Dish or Drink) that determines the type of objects to create.
        """
        try:
            with open(filepath, 'r') as file:
                items_data = json.load(file)
            return [cls(**item) for item in items_data]
        except FileNotFoundError:
            logging.error(f"File not found: {filepath}")
            return []
        except json.JSONDecodeError as e:
            logging.error(f"Failed to decode JSON from {filepath}: {e}")
            return []
        except Exception as e:
            logging.error(f"Unexpected error while loading items from {filepath}: {e}")
            return []

    @staticmethod
    def save_data(filepath, objects):
        original_data = None
        try:
            with open(filepath, 'r') as file:
                original_data = file.read()

            data = [obj.to_dict() for obj in objects]
            with open(filepath, 'w') as file:
                json.dump(data, file, indent=4)
            logging.info("Data successfully saved.")
        except Exception as e:
            if original_data is not None:
                with open(filepath, 'w') as file:
                    file.write(original_data)
                logging.error(f"Original data restored after failed save attempt: {e}")
            else:
                logging.error(f"Failed to restore original data because it was not read: {e}")
            raise

    @staticmethod
    def get_next_id(items):
        """
        Returns the next available ID for a new item. It assumes that items may not be empty and should have an 'id' attribute.
        """
        return max((item.id for item in items), default=0) + 1
