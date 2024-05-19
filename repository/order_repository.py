import logging
from datetime import datetime
from sqlalchemy.orm import Session, joinedload, contains_eager
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

    def get_open_orders(self):
        return self.session.query(Order).filter(Order.status == cast(0, Integer)).all()

    def get_order_by_customer(self, customer: str):
        return self.session.query(Order).filter(Order.customer == cast(customer, String)).first()

    def get_order_by_date_range(self, start_date: str, end_date: str, status: int):
        return (self.session.query(Order)
                .filter(Order.status == status)
                .filter(Order.created_at >= start_date, Order.created_at <= end_date)
                .all())

    def create_order(self, customer: str, total: float):
        order = Order(customer=customer, total=total, created_at=datetime.now())
        self.session.add(order)
        self.session.commit()
        return order

    def update_order(self, order_id: int, status: int):
        order = self.get_order_by_id(order_id)
        order.status = status
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
        try:
            self.session.close()
        except Exception as close_exc:
            logging.error(f"Failed to close session: {close_exc}")
        if exc_type:
            raise exc_val
        return True
