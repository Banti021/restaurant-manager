from sqlalchemy.orm import Session
from sqlalchemy import cast, String, Integer
from models.drink import Drink


class DrinkRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_drinks(self):
        return self.session.query(Drink).all()

    def get_drink_by_id(self, drink_id: int):
        return self.session.query(Drink).filter(Drink.id == cast(drink_id, Integer)).first()

    def get_drink_by_name(self, name: str):
        return self.session.query(Drink).filter(Drink.name == cast(name, String)).first()

    def create_drink(self, drink: Drink):
        self.session.add(drink)
        self.session.commit()
        return drink

    def update_drink(self, drink: Drink):
        self.session.add(drink)
        self.session.commit()
        return drink

    def delete_drink(self, drink: Drink):
        self.session.delete(drink)
        self.session.commit()
        return drink
