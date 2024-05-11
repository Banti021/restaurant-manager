from sqlalchemy import Column, Integer, String, Numeric, Boolean
from database.database import Base


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Numeric(6, 2), nullable=False)
    dish_of_the_day = Column(Boolean, default=False)

    def __str__(self):
        return f"ID: {self.id}, Nazwa: {self.name}, Cena: {self.price}, Danie dnia: {self.dish_of_the_day}"

    def __repr__(self):
        return f"ID: {self.id}, Nazwa: {self.name}, Cena: {self.price}, Danie dnia: {self.dish_of_the_day}"

