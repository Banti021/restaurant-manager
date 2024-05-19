import logging

from sqlalchemy.orm import Session
from sqlalchemy import cast, String, Integer, Boolean, asc
from models.drink import Drink
from database.database import SessionLocal


class DrinkRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_drinks(self):
        return (self.session.query(Drink)
                .filter(Drink.is_deleted == cast(False, Boolean))
                .order_by(asc(cast(Drink.id, Integer)))
                .all())

    def get_drink_by_id(self, drink_id: int):
        return self.session.query(Drink).filter(
            Drink.id == cast(drink_id, Integer),
            Drink.is_deleted == cast(False, Boolean)
        ).first()

    def get_drink_by_id_deleted(self, drink_id: int):
        return self.session.query(Drink).filter(Drink.id == cast(drink_id, Integer)).first()

    def get_drink_by_name(self, name: str):
        return self.session.query(Drink).filter(Drink.name == cast(name, String)).first()

    def create_drink(self, name: str, price: float, is_alcoholic: bool, alcohol_content: int):
        drink = Drink(name=name, price=price, alcohol_content=alcohol_content, is_alcoholic=is_alcoholic)
        self.session.add(drink)
        self.session.commit()
        return drink

    def update_drink(self, drink_id: int, name: str, price: float, is_alcoholic: bool, alcohol_content: int):
        drink = self.get_drink_by_id(drink_id)
        drink.name = name
        drink.price = price
        drink.is_alcoholic = is_alcoholic
        drink.alcohol_content = alcohol_content
        self.session.commit()
        self.session.refresh(drink)
        return drink

    def delete_drink(self, drink_id: int):
        drink = self.get_drink_by_id_deleted(drink_id)
        drink.is_deleted = True
        self.session.commit()
        return drink


class DrinkRepositoryManager:
    def __enter__(self):
        self.session = SessionLocal()
        self.repository = DrinkRepository(self.session)
        return self.repository

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.session.close()
        except Exception as close_exc:
            logging.error(f"Failed to close session: {close_exc}")
        if exc_type:
            raise exc_val
        return True
