from repository.sales_report_repository import SalesReportRepositoryManager


class SalesReportService:
    @staticmethod
    def get_all_sales_reports():
        with SalesReportRepositoryManager() as repository:
            return repository.get_sales_reports()

    @staticmethod
    def get_sales_report_by_id(report_id: int):
        with SalesReportRepositoryManager() as repository:
            return repository.get_sales_report(report_id)

    @staticmethod
    def get_sales_report_by_date(date: str):
        with SalesReportRepositoryManager() as repository:
            return repository.get_sales_report_by_date(date)

    @staticmethod
    def create_sales_report(date: str, total_sales: float, total_orders: int):
        with SalesReportRepositoryManager() as repository:
            return repository.create_sales_report(date, total_sales, total_orders)

    @staticmethod
    def update_sales_report(report_id: int, date: str, total_sales: float, total_orders: int):
        with SalesReportRepositoryManager() as repository:
            return repository.update_sales_report(report_id, date, total_sales, total_orders)

    @staticmethod
    def delete_sales_report(report_id: int):
        with SalesReportRepositoryManager() as repository:
            return repository.delete_sales_report(report_id)
