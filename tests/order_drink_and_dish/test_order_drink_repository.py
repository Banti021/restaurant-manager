import unittest
from datetime import datetime
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from repository.order_drink_repository import OrderDrinkRepository
from models.order_drink import OrderDrink
from models.drink import Drink
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


class TestOrderDrinkRepository(unittest.TestCase):
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
        self.repo = OrderDrinkRepository(self.session)

        self.session.add(Order(id=1, customer="Adam", total=0, created_at=datetime.now()))
        self.session.add(Drink(id=1, name="Test Drink", price=2.5))
        self.session.add(Drink(id=2, name="Test Drink 2", price=3.0))
        self.session.commit()

    def tearDown(self):
        """Rollback transaction and close session after each test."""
        self.transaction.rollback()
        self.connection.close()

    def test_create_order_drink(self):
        order_drink = self.repo.create_order_drink(1, 1, 2)
        self.session.flush()
        self.assertEqual(order_drink.order_id, 1)
        self.assertEqual(order_drink.drink_id, 1)
        self.assertEqual(order_drink.quantity, 2)
        self.assertIsNotNone(self.session.query(OrderDrink).filter(OrderDrink.order_id == 1, OrderDrink.drink_id == 1).first())

    def test_get_order_drink(self):
        order_drink = self.repo.create_order_drink(1, 1, 2)
        self.session.flush()
        retrieved_order_drink = self.repo.get_order_drink(1, 1)
        self.assertEqual(retrieved_order_drink.order_id, order_drink.order_id)
        self.assertEqual(retrieved_order_drink.drink_id, order_drink.drink_id)

    def test_get_order_drinks(self):
        order_drink1 = self.repo.create_order_drink(1, 1, 2)
        order_drink2 = self.repo.create_order_drink(1, 2, 3)
        self.session.flush()
        order_drinks = self.repo.get_order_drinks(1)
        self.assertIn(order_drink1, order_drinks)
        self.assertIn(order_drink2, order_drinks)

    def test_get_order_drink_quantity(self):
        order_drink = self.repo.create_order_drink(1, 1, 2)
        self.session.flush()
        quantity = self.repo.get_order_drink_quantity(1, 1)
        self.assertEqual(quantity, 2)

    def test_update_order_drink(self):
        order_drink = self.repo.create_order_drink(1, 1, 2)
        self.session.flush()
        updated_order_drink = self.repo.update_order_drink(1, 1, 5)
        self.assertEqual(updated_order_drink.quantity, 5)

    def test_delete_order_drink(self):
        order_drink = self.repo.create_order_drink(1, 1, 2)
        self.session.flush()
        self.repo.delete_order_drink(1, 1)
        deleted_order_drink = self.repo.get_order_drink(1, 1)
        self.assertIsNone(deleted_order_drink)

    def test_delete_order_drink_id(self):
        order_drink1 = self.repo.create_order_drink(1, 1, 2)
        order_drink2 = self.repo.create_order_drink(1, 2, 3)
        self.session.flush()
        deleted_order_drinks = self.repo.delete_order_drink_id(1)
        self.assertIn(order_drink1, deleted_order_drinks)
        self.assertIn(order_drink2, deleted_order_drinks)
        self.assertEqual(len(self.repo.get_order_drinks(1)), 0)


if __name__ == '__main__':
    unittest.main()
