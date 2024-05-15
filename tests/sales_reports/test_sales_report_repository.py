import unittest
from datetime import datetime, date
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from repository.sales_report_repository import SalesReportRepository
from models.sales_report import SalesReport
from database.database import Base
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection parameters
DB_HOST = os.getenv("TEST_DB_HOST", "localhost")
DB_DATABASE = os.getenv("TEST_DB_DATABASE", "test_restaurant")
DB_USER = os.getenv("TEST_DB_USER", "test_restaurant_manager")
DB_PASSWORD = os.getenv("TEST_DB_PASSWORD", "test_restauranto")
DB_PORT = os.getenv("TEST_DB_PORT", 5433)  # Default to 5433 for test-db

# Define the database URL
TEST_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"


class TestSalesReportRepository(unittest.TestCase):
    engine = None

    @classmethod
    def setUpClass(cls):
        """Set up database connection and create tables."""
        cls.engine = create_engine(TEST_DATABASE_URL)
        Base.metadata.create_all(cls.engine)

    @classmethod
    def tearDownClass(cls):
        """Drop all tables and close connection."""
        with cls.engine.connect() as connection:
            connection.execute(text("DROP SCHEMA public CASCADE;"))
            connection.execute(text("CREATE SCHEMA public;"))
        cls.engine.dispose()

    def setUp(self):
        """Create a new database session for each test."""
        self.connection = self.engine.connect()
        self.transaction = self.connection.begin()
        self.Session = sessionmaker(bind=self.connection)
        self.session = self.Session()
        self.repo = SalesReportRepository(self.session)

    def tearDown(self):
        """Rollback transaction and close session after each test."""
        self.transaction.rollback()
        self.connection.close()

    def test_create_sales_report(self):
        report = self.repo.create_sales_report("2023-05-01", "2023-05-31", "Test Location")
        self.session.flush()
        self.assertIsNotNone(report.id)
        self.assertEqual(report.date_from, date(2023, 5, 1))
        self.assertEqual(report.date_to, date(2023, 5, 31))
        self.assertEqual(report.location, "Test Location")
        self.assertIsNotNone(self.session.query(SalesReport).filter(SalesReport.id == report.id).first())

    def test_get_all_sales_reports(self):
        report1 = self.repo.create_sales_report("2023-05-01", "2023-05-31", "Test Location 1")
        report2 = self.repo.create_sales_report("2023-06-01", "2023-06-30", "Test Location 2")
        self.session.flush()
        reports = self.repo.get_all_sales_reports()
        self.assertIn(report1, reports)
        self.assertIn(report2, reports)

    def test_get_sales_report_by_id(self):
        report = self.repo.create_sales_report("2023-05-01", "2023-05-31", "Test Location")
        self.session.flush()
        retrieved_report = self.repo.get_sales_report_by_id(report.id)
        self.assertEqual(retrieved_report.id, report.id)
        self.assertEqual(retrieved_report.date_from, date(2023, 5, 1))

    def test_get_sales_report_by_creation_date(self):
        date_str = datetime.today().strftime('%Y-%m-%d')
        report = self.repo.create_sales_report("2023-05-01", "2023-05-31", "Test Location")
        self.session.flush()
        retrieved_reports = self.repo.get_sales_report_by_creation_date(date_str)
        self.assertIn(report, retrieved_reports)

    def test_get_sales_report_by_date_range(self):
        report1 = self.repo.create_sales_report("2023-05-01", "2023-05-31", "Test Location 1")
        report2 = self.repo.create_sales_report("2023-06-01", "2023-06-30", "Test Location 2")
        self.session.flush()
        reports = self.repo.get_sales_report_by_date_range("2023-05-01", "2023-06-30")
        self.assertIn(report1, reports)
        self.assertIn(report2, reports)

    def test_get_non_existent_sales_report(self):
        non_existent_report = self.repo.get_sales_report_by_id(9999)
        self.assertIsNone(non_existent_report)


if __name__ == '__main__':
    unittest.main()
