from sqlalchemy.orm import Session
from sqlalchemy import cast, String, Integer
from models.drink import Drink
from database.database import SessionLocal

class DrinkRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_drinks(self):
        return self.session.query(Drink).all()

    def get_drink_by_id(self, drink_id: int):
        return self.session.query(Drink).filter(Drink.id == cast(drink_id, Integer)).first()

    def get_drink_by_name(self, name: str):
        return self.session.query(Drink).filter(Drink.name == cast(name, String)).first()

    def create_drink(self, name: str, price: float, alcohol_content: float):
        drink = Drink(name=name, price=price, alcohol_content=alcohol_content)
        self.session.add(drink)
        self.session.commit()
        return drink

    def update_drink(self, drink_id: int, name: str, price: float, alcohol_content: float):
        drink = self.get_drink_by_id(drink_id)
        drink.name = name
        drink.price = price
        drink.alcohol_content = alcohol_content
        self.session.commit()
        self.session.refresh(drink)
        return drink

    def delete_drink(self, drink_id: int):
        drink = self.get_drink_by_id(drink_id)
        self.session.delete(drink)
        self.session.commit()
        return drink


class DrinkRepositoryManager:
    def __enter__(self):
        self.session = SessionLocal()
        self.repository = DrinkRepository(self.session)
        return self.repository

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        if exc_type:
            raise exc_val
        return True

