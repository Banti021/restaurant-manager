import unittest
from unittest.mock import patch, MagicMock
from sales import Sales
import os


class TestSales(unittest.TestCase):

    @patch('sales.ConsoleManager')
    @patch('sales.SalesReportService')
    def test_get_all_sales_reports(self, MockSalesReportService, MockConsoleManager):
        sample_report = MagicMock()
        sample_report.__str__.return_value = "Sample Report"
        MockSalesReportService.get_all_sales_reports.return_value = [sample_report]
        Sales._Sales__get_all_sales_reports()
        MockConsoleManager.display_message.assert_called_with("Sample Report")

    @patch('sales.ConsoleManager')
    @patch('sales.SalesReportService')
    def test_get_sales_report_by_id(self, MockSalesReportService, MockConsoleManager):
        MockConsoleManager.get_input.return_value = "1"
        sample_report = MagicMock()
        sample_report.__str__.return_value = "Sample Report"
        MockSalesReportService.get_sales_report_by_id.return_value = sample_report
        Sales._Sales__get_sales_report_by_id()
        MockConsoleManager.display_message.assert_called_with("Sample Report")

    @patch('sales.ConsoleManager')
    @patch('sales.SalesReportService')
    def test_get_sales_report_by_creation_date(self, MockSalesReportService, MockConsoleManager):
        MockConsoleManager.get_input.return_value = "2023-05-01"
        sample_report = MagicMock()
        sample_report.__str__.return_value = "Sample Report"
        MockSalesReportService.get_sales_report_by_creation_date.return_value = [sample_report]
        Sales._Sales__get_sales_report_by_creation_date()
        MockConsoleManager.display_message.assert_called_with("Sample Report")

    @patch('sales.ConsoleManager')
    @patch('sales.SalesReportService')
    def test_get_sales_report_by_date_range(self, MockSalesReportService, MockConsoleManager):
        MockConsoleManager.get_input.side_effect = ["2023-05-01", "2023-05-31"]
        sample_report = MagicMock()
        sample_report.__str__.return_value = "Sample Report"
        MockSalesReportService.get_sales_report_by_date_range.return_value = [sample_report]
        Sales._Sales__get_sales_report_by_date_range()
        MockConsoleManager.display_message.assert_called_with("Sample Report")

    @patch('sales.os.makedirs')
    @patch('sales.ConsoleManager')
    @patch('sales.OrderService')
    @patch('sales.SalesReportPdfGenerator.generate_pdf_with_pdfkit')
    def test_generate_sales_reports(self, MockGeneratePdf, MockOrderService, MockConsoleManager, MockMakedirs):
        MockConsoleManager.get_input.side_effect = ["2023-05-01", "2023-05-31"]
        sample_orders = [MagicMock()]
        MockOrderService.get_order_by_date_range.return_value = sample_orders
        MockGeneratePdf.return_value = "reports/sample_report.pdf"
        Sales.generate_sales_reports()
        MockConsoleManager.display_message.assert_called_with(
            "Raport sprzedaży został wygenerowany w pliku: reports/sample_report.pdf")
        MockMakedirs.assert_called_with("reports")


if __name__ == '__main__':
    unittest.main()
