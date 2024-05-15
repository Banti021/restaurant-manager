import unittest
from datetime import datetime, date, timedelta
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from repository.order_repository import OrderRepository
from models.order import Order
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


class TestOrderRepository(unittest.TestCase):
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
        self.repo = OrderRepository(self.session)

    def tearDown(self):
        """Rollback transaction and close session after each test."""
        self.transaction.rollback()
        self.connection.close()

    def test_create_order(self):
        order = self.repo.create_order("Test Customer", 100.0)
        self.session.flush()
        self.assertIsNotNone(order.id)
        self.assertEqual(order.customer, "Test Customer")
        self.assertEqual(order.total, 100.0)
        self.assertIsNotNone(self.session.query(Order).filter(Order.id == order.id).first())

    def test_get_all_orders(self):
        order1 = self.repo.create_order("Customer 1", 50.0)
        order2 = self.repo.create_order("Customer 2", 75.0)
        self.session.flush()
        orders = self.repo.get_all_orders()
        self.assertIn(order1, orders)
        self.assertIn(order2, orders)

    def test_get_order_by_id(self):
        order = self.repo.create_order("Test Customer", 100.0)
        self.session.flush()
        retrieved_order = self.repo.get_order_by_id(order.id)
        self.assertEqual(retrieved_order.id, order.id)
        self.assertEqual(retrieved_order.customer, "Test Customer")

    def test_get_open_orders(self):
        order1 = self.repo.create_order("Customer 1", 50.0)
        order2 = self.repo.create_order("Customer 2", 75.0)
        self.repo.update_order(order2.id, 1)  # Mark order2 as closed
        self.session.flush()
        open_orders = self.repo.get_open_orders()
        self.assertIn(order1, open_orders)
        self.assertNotIn(order2, open_orders)

    def test_get_order_by_customer(self):
        order = self.repo.create_order("Unique Customer", 100.0)
        self.session.flush()
        retrieved_order = self.repo.get_order_by_customer("Unique Customer")
        self.assertEqual(retrieved_order.customer, "Unique Customer")

    def test_get_order_by_date_range(self):
        order1 = self.repo.create_order("Customer 1", 50.0)
        order2 = self.repo.create_order("Customer 2", 75.0)
        self.session.flush()
        start_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        end_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        orders = self.repo.get_order_by_date_range(start_date, end_date, 0)
        self.assertIn(order1, orders)
        self.assertIn(order2, orders)

    def test_update_order(self):
        order = self.repo.create_order("Customer to Update", 100.0)
        self.session.flush()
        updated_order = self.repo.update_order(order.id, 1)
        self.assertEqual(updated_order.status, 1)

    def test_delete_order(self):
        order = self.repo.create_order("Customer to Delete", 100.0)
        self.session.flush()
        deleted_order = self.repo.delete_order(order.id)
        self.assertIsNone(self.session.query(Order).filter(Order.id == order.id).first())

    def test_get_non_existent_order(self):
        non_existent_order = self.repo.get_order_by_id(9999)
        self.assertIsNone(non_existent_order)


if __name__ == '__main__':
    unittest.main()
