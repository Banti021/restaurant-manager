from sqlalchemy.orm import Session
from sqlalchemy import cast, Integer

from database.database import SessionLocal
from models.order_dish import OrderDish


class OrderDishRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_order_dish(self, order_id: int, dish_id: int):
        return self.session.query(OrderDish).filter(OrderDish.order_id == cast(order_id, Integer),
                                                    OrderDish.dish_id == cast(dish_id, Integer)).first()

    def get_order_dishes(self, order_id: int):
        return self.session.query(OrderDish).filter(OrderDish.order_id == cast(order_id, Integer)).all()

    def get_order_dish_quantity(self, order_id: int, dish_id: int):
        order_dish = self.get_order_dish(order_id, dish_id)
        return order_dish.quantity if order_dish else 0

    def create_order_dish(self, order_id: int, dish_id: int, quantity: int):
        order_dish = OrderDish(order_id=order_id, dish_id=dish_id, quantity=quantity)
        self.session.add(order_dish)
        self.session.commit()
        self.session.refresh(order_dish)
        return order_dish

    def update_order_dish(self, order_id: int, dish_id: int, quantity: int):
        order_dish = self.get_order_dish(order_id, dish_id)
        order_dish.quantity = quantity
        self.session.commit()
        self.session.refresh(order_dish)
        return order_dish

    def delete_order_dish(self, order_id: int, dish_id: int):
        order_dish = self.get_order_dish(order_id, dish_id)
        self.session.delete(order_dish)
        self.session.commit()
        return order_dish

    def delete_order_dishes(self, order_id: int):
        order_dishes = self.get_order_dishes(order_id)
        for order_dish in order_dishes:
            self.session.delete(order_dish)
        self.session.commit()
        return order_dishes


class OrderDishRepositoryManager:
    def __enter__(self):
        self.session = SessionLocal()
        self.repository = OrderDishRepository(self.session)
        return self.repository

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        if exc_type:
            raise exc_val
        return True