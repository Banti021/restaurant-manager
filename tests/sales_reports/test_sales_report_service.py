import unittest
from unittest.mock import patch, MagicMock
from services.sales_report_service import SalesReportService
from repository.sales_report_repository import SalesReportRepositoryManager


class TestSalesReportService(unittest.TestCase):

    @patch('repository.sales_report_repository.SalesReportRepositoryManager')
    def test_get_all_sales_reports(self, MockRepositoryManager):
        mock_repo_instance = MockRepositoryManager.return_value.__enter__.return_value
        mock_repo_instance.get_all_sales_reports.return_value = []

        reports = SalesReportService.get_all_sales_reports()
        mock_repo_instance.get_all_sales_reports.assert_called_once()
        self.assertEqual(reports, [])

    @patch('repository.sales_report_repository.SalesReportRepositoryManager')
    def test_get_sales_report_by_id(self, MockRepositoryManager):
        mock_repo_instance = MockRepositoryManager.return_value.__enter__.return_value
        mock_report = {'id': 1, 'report': 'some_report'}
        mock_repo_instance.get_sales_report_by_id.return_value = mock_report

        report = SalesReportService.get_sales_report_by_id(1)
        mock_repo_instance.get_sales_report_by_id.assert_called_once_with(1)
        self.assertEqual(report, mock_report)

    @patch('repository.sales_report_repository.SalesReportRepositoryManager')
    def test_get_sales_report_by_creation_date(self, MockRepositoryManager):
        mock_repo_instance = MockRepositoryManager.return_value.__enter__.return_value
        mock_report = {'date': '2023-05-15', 'report': 'some_report'}
        mock_repo_instance.get_sales_report_by_creation_date.return_value = mock_report

        report = SalesReportService.get_sales_report_by_creation_date('2023-05-15')
        mock_repo_instance.get_sales_report_by_creation_date.assert_called_once_with('2023-05-15')
        self.assertEqual(report, mock_report)

    @patch('repository.sales_report_repository.SalesReportRepositoryManager')
    def test_get_sales_report_by_date_range(self, MockRepositoryManager):
        mock_repo_instance = MockRepositoryManager.return_value.__enter__.return_value
        mock_reports = [{'date': '2023-05-15', 'report': 'some_report'}]
        mock_repo_instance.get_sales_report_by_date_range.return_value = mock_reports

        reports = SalesReportService.get_sales_report_by_date_range('2023-05-01', '2023-05-31')
        mock_repo_instance.get_sales_report_by_date_range.assert_called_once_with('2023-05-01', '2023-05-31')
        self.assertEqual(reports, mock_reports)

    @patch('repository.sales_report_repository.SalesReportRepositoryManager')
    def test_create_sales_report(self, MockRepositoryManager):
        mock_repo_instance = MockRepositoryManager.return_value.__enter__.return_value
        mock_report = {'date_from': '2023-05-01', 'date_to': '2023-05-31', 'location': 'some_location'}
        mock_repo_instance.create_sales_report.return_value = mock_report

        report = SalesReportService.create_sales_report('2023-05-01', '2023-05-31', 'some_location')
        mock_repo_instance.create_sales_report.assert_called_once_with('2023-05-01', '2023-05-31', 'some_location')
        self.assertEqual(report, mock_report)


if __name__ == '__main__':
    unittest.main()
