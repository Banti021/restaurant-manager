from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.database import Base


class OrderDrink(Base):
    __tablename__ = 'order_drinks'

    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True)
    drink_id = Column(Integer, ForeignKey('drinks.id'), primary_key=True)
    quantity = Column(Integer, default=1)
