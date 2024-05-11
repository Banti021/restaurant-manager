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

    def create_dish(self, dish: Dish):
        self.session.add(dish)
        self.session.commit()
        return dish

    def update_dish(self, dish: Dish):
        self.session.add(dish)
        self.session.commit()
        return dish

    def delete_dish(self, dish: Dish):
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
