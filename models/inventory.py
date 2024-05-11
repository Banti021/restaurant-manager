from sqlalchemy import Column, Integer, String, Numeric
from database.database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    item_id = Column(Integer, primary_key=True, index=True)
    customer = Column(String(255), nullable=False)
    total = Column(Numeric(10, 2), nullable=False)
    status = Column(String(50), default="open")