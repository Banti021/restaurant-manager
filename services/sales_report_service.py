from repository.sales_report_repository import SalesReportRepositoryManager


class SalesReportService:
    @staticmethod
    def get_all_sales_reports():
        with SalesReportRepositoryManager() as repository:
            return repository.get_all_sales_reports()

    @staticmethod
    def get_sales_report_by_id(sale_id):
        with SalesReportRepositoryManager() as repository:
            return repository.get_sales_report_by_id(sale_id)

    @staticmethod
    def get_sales_report_by_creation_date(date):
        with SalesReportRepositoryManager() as repository:
            return repository.get_sales_report_by_creation_date(date)

    @staticmethod
    def get_sales_report_by_date_range(start_date, end_date):
        with SalesReportRepositoryManager() as repository:
            return repository.get_sales_report_by_date_range(start_date, end_date)

    @staticmethod
    def create_sales_report(date_from, date_to, location):
        with SalesReportRepositoryManager() as repository:
            return repository.create_sales_report(date_from, date_to, location)