import time
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database connection parameters
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def connect_to_database(attempts=5, delay=5):
    """Attempt to connect to the database with a retry mechanism."""
    while attempts > 0:
        try:
            connection = psycopg2.connect(
                dbname=DB_DATABASE,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST
            )
            print("Connected to the database successfully.")
            return connection
        except OperationalError as e:
            print(f"Failed to connect to the database. Retrying in {delay} seconds...")
            time.sleep(delay)
            attempts -= 1
    raise Exception("Could not connect to the database after several attempts")


def run_sql_scripts(filename, cursor):
    with open(filename, 'r') as file:
        sql_script = file.read()
    cursor.execute(sql_script)


def seed_database():
    print(f"Attempting to connect to database '{DB_DATABASE}' at host '{DB_HOST}'...")
    connection = None
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        # Naive checking if database is already seeded
        cursor.execute("SELECT EXISTS(SELECT 1 FROM dishes LIMIT 1);")
        dishes_exist = cursor.fetchone()[0]

        cursor.execute("SELECT EXISTS(SELECT 1 FROM drinks LIMIT 1);")
        drinks_exist = cursor.fetchone()[0]

        if dishes_exist or drinks_exist:
            print("Database already seeded.")
            return

        run_sql_scripts('database/scripts/seeder.sql', cursor)
        connection.commit()
        print("Database seeded properly.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            connection.close()
            print("Database connection closed.")


if __name__ == "__main__":
    seed_database()
