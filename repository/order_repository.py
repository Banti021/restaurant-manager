from sqlalchemy.orm import Session
from sqlalchemy import cast, String, Integer
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

    def create_order(self, order: Order):
        self.session.add(order)
        self.session.commit()
        return order

    def update_order(self, order: Order):
        self.session.add(order)
        self.session.commit()
        return order

    def delete_order(self, order: Order):
        self.session.delete(order)
        self.session.commit()
        return order

