class Dish:
    def __init__(self, id, name, price, dish_of_the_day=False):
        self.id = id
        self.name = name
        self.price = price
        self.dish_of_the_day = dish_of_the_day

    def __str__(self):
        dish_status = " - danie dnia" if self.dish_of_the_day else ""
        return f"{self.id}. {self.name} - {self.price} PLN{dish_status}"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'dish_of_the_day': self.dish_of_the_day
        }
