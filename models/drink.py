from sqlalchemy import Column, Integer, String, Numeric, Boolean
from database.database import Base


class Drink(Base):
    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Numeric(6, 2), nullable=False)
    is_alcoholic = Column(Boolean, default=False, nullable=False)
    alcohol_content = Column(Numeric(3, 1), nullable=True)

    def __str__(self):
        return f"{self.id}. {self.name} {f'(Alkohol, {self.alcohol_content}%)' if self.is_alcoholic else ''} - {self.price} PLN"

    def __repr__(self):
        return f"{self.id}. {self.name} - {self.price} PLN"
