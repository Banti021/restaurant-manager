from sqlalchemy import Column, Integer, Date, String
from database.database import Base


class SalesReport(Base):
    __tablename__ = 'sales_reports'

    id = Column(Integer, primary_key=True)
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    created_at = Column(Date, nullable=False)
    location = Column(String, nullable=False)

    def __str__(self):
        return f"Raport sprzedaży od {self.date_from} do {self.date_to} dostępny w:  {self.location}"
