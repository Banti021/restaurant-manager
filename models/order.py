class Order:
    def __init__(self, id, customer, total, dishes, drinks, status='open'):
        self.id = id
        self.customer = customer
        self.total = total
        self.dishes = dishes
        self.drinks = drinks
        self.status = status

    def __str__(self):
        return f"{self.id}. {self.customer} - {self.total} PLN"

    def to_dict(self):
        return {
            'id': self.id,
            'customer': self.customer,
            'total': self.total,
            'dishes': [dish.to_dict() for dish in self.dishes],
            'drinks': [drink.to_dict() for drink in self.drinks],
            'status': self.status
        }