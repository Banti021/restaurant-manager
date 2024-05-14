from sqlalchemy import Column, Integer, String, Numeric, Boolean
from sqlalchemy.orm import relationship

from database.database import Base


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    price = Column(Numeric(6, 2), nullable=False)
    dish_of_the_day = Column(Boolean, default=False)

    def __str__(self):
        return f"{self.id}. {self.name} - {self.price} PLN" + (" - danie dnia" if self.dish_of_the_day else "")

    def __repr__(self):
        return f"{self.id}. {self.name} - {self.price} PLN" + (" - danie dnia" if self.dish_of_the_day else "")
