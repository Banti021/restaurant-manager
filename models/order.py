from sqlalchemy import Column, Integer, String, Numeric, Date
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship

from database.database import Base
from models.custom.custom_order_status import OrderStatusType
from enums.order_status import OrderStatus


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer = Column(String(255), nullable=False)
    total = Column(Numeric(10, 2), nullable=False)
    status = Column(OrderStatusType, default=OrderStatus.OPEN)
    created_at = Column(Date, nullable=False)

    def __str__(self):
        return f"ID: {self.id}, Klient: {self.customer}, Kwota: {self.total}, Status: {self.status.name}"

    @staticmethod
    def list_statuses():
        return OrderStatus.list_statuses()

    @staticmethod
    def order_to_dict(order):
        """Converts an Order object into a dictionary including dynamic relationships."""
        return {
            "id": order.id,
            "customer": order.customer,
            "total": float(order.total),
            "status": order.status.name if order.status else None,
            "created_at": order.created_at.isoformat() if order.created_at else None
        }