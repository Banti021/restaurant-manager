import logging

from sqlalchemy.orm import Session
from sqlalchemy import cast, Integer

from database.database import SessionLocal
from models.order_drink import OrderDrink


class OrderDrinkRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_order_drink(self, order_id: int, drink_id: int):
        return self.session.query(OrderDrink).filter(OrderDrink.order_id == cast(order_id, Integer),
                                                    OrderDrink.drink_id == cast(drink_id, Integer)).first()

    def get_order_drinks(self, order_id: int):
        return self.session.query(OrderDrink).filter(OrderDrink.order_id == cast(order_id, Integer)).all()

    def get_order_drink_quantity(self, order_id: int, drink_id: int):
        order_drink = self.get_order_drink(order_id, drink_id)
        return order_drink.quantity if order_drink else 0

    def create_order_drink(self, order_id: int, drink_id: int, quantity: int):
        order_drink = OrderDrink(order_id=order_id, drink_id=drink_id, quantity=quantity)
        self.session.add(order_drink)
        self.session.commit()
        self.session.refresh(order_drink)
        return order_drink

    def update_order_drink(self, order_id: int, drink_id: int, quantity: int):
        order_drink = self.get_order_drink(order_id, drink_id)
        order_drink.quantity = quantity
        self.session.commit()
        self.session.refresh(order_drink)
        return order_drink

    def delete_order_drink(self, order_id: int, drink_id: int):
        order_drink = self.get_order_drink(order_id, drink_id)
        self.session.delete(order_drink)
        self.session.commit()
        return order_drink

    def delete_order_drink_id(self, order_id: int):
        logging.debug(f"Deleting order drinks for order_id: {order_id}")
        order_drinks = self.get_order_drinks(order_id)
        for order_drink in order_drinks:
            self.session.delete(order_drink)
        self.session.commit()
        return order_drinks


class OrderDrinkRepositoryManager:
    def __enter__(self):
        self.session = SessionLocal()
        self.repository = OrderDrinkRepository(self.session)
        return self.repository

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.session.close()
        except Exception as close_exc:
            logging.error(f"Failed to close session: {close_exc}")
        if exc_type:
            raise exc_val
        return True
