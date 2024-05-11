from sqlalchemy.orm import Session
from sqlalchemy import cast, String, Integer

from database.database import SessionLocal
from models.order import Order


class OrderRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_orders(self):
        return self.session.query(Order).all()

    def get_order_by_id(self, order_id: int):
        return self.session.query(Order).filter(Order.id == cast(order_id, Integer)).first()

    def get_order_by_customer(self, customer: str):
        return self.session.query(Order).filter(Order.customer == cast(customer, String)).first()

    def create_order(self, customer: str, order_date: str):
        order = Order(customer=customer, order_date=order_date)
        self.session.add(order)
        self.session.commit()
        return order

    def update_order(self, order_id: int, customer: str, order_date: str):
        order = self.get_order_by_id(order_id)
        order.customer = customer
        order.order_date = order_date
        self.session.add(order)
        self.session.commit()
        return order

    def delete_order(self, order_id: int):
        order = self.get_order_by_id(order_id)
        self.session.delete(order)
        self.session.commit()
        return order


class OrderRepositoryManager:
    def __enter__(self):
        self.session = SessionLocal()
        self.repository = OrderRepository(self.session)
        return self.repository

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        if exc_type:
            raise exc_val
        return True
