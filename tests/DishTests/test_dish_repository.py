# test_dish_repository.py
import pytest
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


@pytest.fixture(scope="session")
def engine():
    return create_engine(TEST_DATABASE_URL)


@pytest.fixture(scope="session")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    with engine.connect() as connection:
        connection.execute(text("DROP SCHEMA public CASCADE;"))
        connection.execute(text("CREATE SCHEMA public;"))


@pytest.fixture
def db_session(engine, tables):
    """Creates a new database session for a test, with a transaction rolled back at the end."""
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    yield session
    session.rollback()
    connection.close()


@pytest.fixture
def dish_repo(db_session):
    return DishRepository(db_session)


@pytest.fixture
def clean_dishes(db_session):
    """Clean up all dishes before and after the test."""
    yield
    db_session.execute(text('DELETE FROM dishes;'))
    db_session.commit()


def test_create_dish(dish_repo, db_session, clean_dishes):
    dish = dish_repo.create_dish("Test Pasta", 9.99, False)
    db_session.flush()
    assert dish.id is not None
    assert dish.name == "Test Pasta"
    assert db_session.query(Dish).filter(Dish.id == dish.id).first() is not None


def test_get_dish_by_id(dish_repo, db_session):
    dish = dish_repo.create_dish("Test Salad", 5.55, False)
    db_session.flush()
    retrieved_dish = dish_repo.get_dish_by_id(dish.id)
    assert retrieved_dish.id == dish.id
    assert retrieved_dish.name == "Test Salad"


def test_update_dish(dish_repo, db_session):
    dish = dish_repo.create_dish("Test Soup", 3.50, False)
    dish_repo.update_dish(dish.id, "Updated Soup", 4.00, True)
    updated_dish = dish_repo.get_dish_by_id(dish.id)
    assert updated_dish.name == "Updated Soup"
    assert updated_dish.price == 4.00
    assert updated_dish.dish_of_the_day is True


def test_delete_dish(dish_repo, db_session):
    dish = dish_repo.create_dish("Test Dessert", 2.50, False)
    dish_repo.delete_dish(dish.id)
    db_session.flush()
    assert dish_repo.get_dish_by_id(dish.id) is None


def test_set_dish_of_the_day(dish_repo, db_session):
    dish = dish_repo.create_dish("Test Drink", 1.99, False)
    dish_repo.set_dish_of_the_day(dish.id)
    assert dish_repo.get_dish_by_id(dish.id).dish_of_the_day is True
