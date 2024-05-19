import unittest
from datetime import datetime
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from repository.order_dish_repository import OrderDishRepository
from models.order_dish import OrderDish
from models.order import Order  # Ensure this is imported
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


class TestOrderDishRepository(unittest.TestCase):
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
        self.repo = OrderDishRepository(self.session)

        # Create a test order to satisfy foreign key constraint
        self.test_order = Order(customer="Test Customer", total=100.0)
        self.session.add(self.test_order)
        self.session.commit()

    def tearDown(self):
        """Rollback transaction and close session after each test."""
        self.transaction.rollback()
        self.connection.close()

    def test_create_order_dish(self):
        order_dish = self.repo.create_order_dish(self.test_order.id, 1, 2)
        self.session.flush()
        self.assertIsNotNone(order_dish.id)
        self.assertEqual(order_dish.order_id, self.test_order.id)
        self.assertEqual(order_dish.dish_id, 1)
        self.assertEqual(order_dish.quantity, 2)
        self.assertIsNotNone(self.session.query(OrderDish).filter(OrderDish.id == order_dish.id).first())

    def test_get_order_dish(self):
        order_dish = self.repo.create_order_dish(self.test_order.id, 1, 2)
        self.session.flush()
        retrieved_order_dish = self.repo.get_order_dish(self.test_order.id, 1)
        self.assertEqual(retrieved_order_dish.id, order_dish.id)

    def test_get_order_dishes(self):
        order_dish1 = self.repo.create_order_dish(self.test_order.id, 1, 2)
        order_dish2 = self.repo.create_order_dish(self.test_order.id, 2, 3)
        self.session.flush()
        order_dishes = self.repo.get_order_dishes(self.test_order.id)
        self.assertIn(order_dish1, order_dishes)
        self.assertIn(order_dish2, order_dishes)

    def test_update_order_dish(self):
        order_dish = self.repo.create_order_dish(self.test_order.id, 1, 2)
        self.session.flush()
        updated_order_dish = self.repo.update_order_dish(self.test_order.id, 1, 5)
        self.assertEqual(updated_order_dish.quantity, 5)

    def test_delete_order_dish(self):
        order_dish = self.repo.create_order_dish(self.test_order.id, 1, 2)
        self.session.flush()
        self.repo.delete_order_dish(self.test_order.id, 1)
        deleted_order_dish = self.repo.get_order_dish(self.test_order.id, 1)
        self.assertIsNone(deleted_order_dish)

    def test_delete_order_dish_id(self):
        order_dish1 = self.repo.create_order_dish(self.test_order.id, 1, 2)
        order_dish2 = self.repo.create_order_dish(self.test_order.id, 2, 3)
        self.session.flush()
        deleted_order_dishes = self.repo.delete_order_dish_id(self.test_order.id)
        self.assertIn(order_dish1, deleted_order_dishes)
        self.assertIn(order_dish2, deleted_order_dishes)
        self.assertEqual(len(self.repo.get_order_dishes(self.test_order.id)), 0)


if __name__ == '__main__':
    unittest.main()
