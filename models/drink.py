from sqlalchemy import Column, Integer, String, Numeric
from database.database import Base


class Drink(Base):
    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Numeric(6, 2), nullable=False)

    def __str__(self):
        return f"ID: {self.id}, Nazwa: {self.name}, Cena: {self.price}"

    def __repr__(self):
        return f"ID: {self.id}, Nazwa: {self.name}, Cena: {self.price}"