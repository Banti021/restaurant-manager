from sqlalchemy.orm import Session
from sqlalchemy import cast, Integer

from database.database import SessionLocal
from models.sales_report import SalesReport


class SalesReportRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_sales_report(self, date: str, total_sales: float, total_orders: int):
        sales_report = SalesReport(date=date, total_sales=total_sales, total_orders=total_orders)
        self.session.add(sales_report)
        self.session.commit()
        self.session.refresh(sales_report)
        return sales_report

    def get_sales_report(self, report_id: int):
        return self.session.query(SalesReport).filter(SalesReport.report_id == cast(report_id, Integer)).first()

    def get_sales_reports(self):
        return self.session.query(SalesReport).all()

    def update_sales_report(self, report_id: int, date: str, total_sales: float, total_orders: int):
        sales_report = self.get_sales_report(report_id)
        sales_report.date = date
        sales_report.total_sales = total_sales
        sales_report.total_orders = total_orders
        self.session.commit()
        self.session.refresh(sales_report)
        return sales_report

    def delete_sales_report(self, report_id: int):
        sales_report = self.get_sales_report(report_id)
        self.session.delete(sales_report)
        self.session.commit()
        return sales_report

    def get_sales_report_by_date(self, date: str):
        return self.session.query(SalesReport).filter(SalesReport.date == cast(date, Integer)).first()


class SalesReportRepositoryManager:
    def __enter__(self):
        self.session = SessionLocal()
        self.repository = SalesReportRepository(self.session)
        return self.repository

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        if exc_type:
            raise exc_val
        return True