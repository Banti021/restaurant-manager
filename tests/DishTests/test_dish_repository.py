import unittest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from repository.dish_repository import DishRepository
from models.dish import Dish
from database.database import Base
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection parameters
DB_HOST = os.getenv("TEST_DB_HOST")
DB_DATABASE = os.getenv("TEST_DB_DATABASE")
DB_USER = os.getenv("TEST_DB_USER")
DB_PASSWORD = os.getenv("TEST_DB_PASSWORD")

# Define the database URL
TEST_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5433/{DB_DATABASE}"


class TestDishRepository(unittest.TestCase):
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
        self.dish_repo = DishRepository(self.session)

    def tearDown(self):
        """Rollback transaction and close session after each test."""
        self.session.rollback()
        self.connection.close()

    def test_create_dish(self):
        dish = self.dish_repo.create_dish("Test Pasta", 9.99, False)
        self.session.flush()
        self.assertIsNotNone(dish.id)
        self.assertEqual(dish.name, "Test Pasta")
        self.assertIsNotNone(self.session.query(Dish).filter(Dish.id == dish.id).first())

    def test_get_dish_by_id(self):
        dish = self.dish_repo.create_dish("Test Salad", 5.55, False)
        self.session.flush()
        retrieved_dish = self.dish_repo.get_dish_by_id(dish.id)
        self.assertEqual(retrieved_dish.id, dish.id)
        self.assertEqual(retrieved_dish.name, "Test Salad")

    def test_update_dish(self):
        dish = self.dish_repo.create_dish("Test Soup", 3.50, False)
        self.dish_repo.update_dish(dish.id, "Updated Soup", 4.00, True)
        updated_dish = self.dish_repo.get_dish_by_id(dish.id)
        self.assertEqual(updated_dish.name, "Updated Soup")
        self.assertEqual(updated_dish.price, 4.00)
        self.assertTrue(updated_dish.dish_of_the_day)

    def test_delete_dish(self):
        dish = self.dish_repo.create_dish("Test Dessert", 2.50, False)
        self.dish_repo.delete_dish(dish.id)
        self.session.flush()
        self.assertIsNone(self.dish_repo.get_dish_by_id(dish.id))

    def test_set_dish_of_the_day(self):
        dish = self.dish_repo.create_dish("Test Drink", 1.99, False)
        self.dish_repo.set_dish_of_the_day(dish.id)
        self.assertTrue(self.dish_repo.get_dish_by_id(dish.id).dish_of_the_day)


if __name__ == '__main__':
    unittest.main()
