import logging

from sqlalchemy.orm import Session
from sqlalchemy import cast, String, Integer, Boolean, asc
from models.dish import Dish
from database.database import SessionLocal


class DishRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_dishes(self):
        return (self.session.query(Dish)
                .filter(Dish.is_deleted == cast(False, Boolean))
                .order_by(asc(cast(Dish.id, Integer)))
                .all())

    def get_dish_by_id(self, dish_id: int):
        return self.session.query(Dish).filter(
            Dish.id == cast(dish_id, Integer),
            Dish.is_deleted == cast(False, Boolean)
        ).first()

    def get_dish_by_id_with_deleted(self, dish_id: int):
        return self.session.query(Dish).filter(Dish.id == cast(dish_id, Integer)).first()

    def get_dish_by_name(self, name: str):
        return self.session.query(Dish).filter(Dish.name == cast(name, String)).first()

    def create_dish(self, name: str, price: float, dish_of_the_day: bool):
        dish = Dish(name=name, price=price, dish_of_the_day=dish_of_the_day)
        self.session.add(dish)
        self.session.commit()
        return dish

    def update_dish(self, dish_id: int, name: str, price: float, dish_of_the_day: bool):
        dish = self.get_dish_by_id(dish_id)
        dish.name = name
        dish.price = price
        dish.dish_of_the_day = dish_of_the_day
        self.session.commit()
        self.session.refresh(dish)
        return dish

    def delete_dish(self, dish_id: int):
        dish = self.get_dish_by_id_with_deleted(dish_id)
        dish.is_deleted = True
        self.session.commit()
        return dish

    def set_dish_of_the_day(self, dish_id: int):
        dish = self.get_dish_by_id(dish_id)
        dish.dish_of_the_day = True
        self.session.commit()
        self.session.refresh(dish)
        return dish


class DishRepositoryManager:
    def __enter__(self):
        self.session = SessionLocal()
        self.repository = DishRepository(self.session)
        return self.repository

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.session.close()
        except Exception as close_exc:
            logging.error(f"Failed to close session: {close_exc}")
        if exc_type:
            raise exc_val
        return True
