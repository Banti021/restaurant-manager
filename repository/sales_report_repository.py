import logging
from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy import cast, Integer

from database.database import SessionLocal
from models.sales_report import SalesReport


class SalesReportRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_sales_reports(self):
        reports = self.session.query(SalesReport).all()
        return reports

    def get_sales_report_by_id(self, sale_id: int):
        return self.session.query(SalesReport).filter(SalesReport.id == cast(sale_id, Integer)).first()

    def get_sales_report_by_creation_date(self, date: str):
        return self.session.query(SalesReport).filter(SalesReport.created_at == date).all()

    def get_sales_report_by_date_range(self, start_date: str, end_date: str):
        return self.session.query(SalesReport).filter(SalesReport.date_from >= start_date, SalesReport.to <= end_date).all()

    def create_sales_report(self, date_from: str, date_to: str, location: str):
        try:
            sales_report = SalesReport(
                date_from=date_from,
                date_to=date_to,
                created_at=datetime.today().strftime('%Y-%m-%d'),
                location=location
            )
            self.session.add(sales_report)
            self.session.commit()
            return sales_report
        except Exception as e:
            logging.error(f"Failed to create sales report: {e}")
            return None


class SalesReportRepositoryManager:
    def __enter__(self):
        self.session = SessionLocal()
        self.repository = SalesReportRepository(self.session)
        return self.repository

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.session.close()
        except Exception as close_exc:
            logging.error(f"Failed to close session: {close_exc}")
        if exc_type:
            raise exc_val
        return True
