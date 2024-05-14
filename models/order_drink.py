from sqlalchemy import Column, Integer, ForeignKey
from database.database import Base


class OrderDrink(Base):
    __tablename__ = "order_drinks"

    order_id = Column(Integer, ForeignKey("orders.id"), primary_key=True, index=True)
    drink_id = Column(Integer, ForeignKey("drinks.id"), primary_key=True, index=True)
    quantity = Column(Integer, default=1)

    def __str__(self):
        return f"ID zamówienia: {self.order_id}, ID napoju: {self.drink_id}, Ilość: {self.quantity}"

    def __repr__(self):
        return f"ID zamówienia: {self.order_id}, ID napoju: {self.drink_id}, Ilość: {self.quantity}"