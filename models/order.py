from sqlalchemy import Column, Integer, String, Numeric
from database.database import Base
from models.custom.custom_order_status import OrderStatusType
from enums.order_status import OrderStatus


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer = Column(String(255), nullable=False)
    total = Column(Numeric(10, 2), nullable=False)
    status = Column(OrderStatusType, default=OrderStatus.OPEN)

    def __str__(self):
        return f"ID: {self.id}, Klient: {self.customer}, Kwota: {self.total}, Status: {self.status.name}"

    def __repr__(self):
        return f"ID: {self.id}, Klient: {self.customer}, Kwota: {self.total}, Status: {self.status.name}"

    @staticmethod
    def list_statuses():
        return OrderStatus.list_statuses()