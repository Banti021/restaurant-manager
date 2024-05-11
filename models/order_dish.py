from sqlalchemy import Column, Integer, ForeignKey
from database.database import Base


class OrderDish(Base):
    __tablename__ = "order_dishes"

    order_id = Column(Integer, ForeignKey("orders.id"), primary_key=True, index=True)
    dish_id = Column(Integer, ForeignKey("dishes.id"), primary_key=True, index=True)
    quantity = Column(Integer, default=1)

    def __str__(self):
        return f"ID zamówienia: {self.order_id}, ID dania: {self.dish_id}, Ilość: {self.quantity}"

    def __repr__(self):
        return f"ID zamówienia: {self.order_id}, ID dania: {self.dish_id}, Ilość: {self.quantity}"