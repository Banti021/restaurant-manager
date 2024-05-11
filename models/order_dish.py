from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from database.database import Base


class OrderDish(Base):
    __tablename__ = "order_dishes"

    order_id = Column(Integer, ForeignKey("orders.id"), primary_key=True, index=True)
    drink_id = Column(Integer, ForeignKey("drinks.id"), primary_key=True, index=True)
    quantity = Column(Integer, default=1)