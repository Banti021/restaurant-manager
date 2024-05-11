from sqlalchemy.orm import Session
from sqlalchemy import cast, String, Integer
from models.dish import Dish
from database.database import SessionLocal

class DishRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_dishes(self):
        return self.session.query(Dish).all()

    def get_dish_by_id(self, dish_id: int):
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
        dish = self.get_dish_by_id(dish_id)
        self.session.delete(dish)
        self.session.commit()
        return dish


class DishRepositoryManager:
    def __enter__(self):
        self.session = SessionLocal()
        self.repository = DishRepository(self.session)
        return self.repository

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        if exc_type:
            raise exc_val
        return True
