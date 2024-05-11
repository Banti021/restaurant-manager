from sqlalchemy import Column, Integer, String, Numeric, Date
from database.database import Base


class SalesReport(Base):
    __tablename__ = "sales_reports"

    report_id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    total_sales = Column(Numeric(10, 2), nullable=False)
    total_orders = Column(Integer, nullable=False)