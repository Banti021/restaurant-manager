import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection parameters
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def run_sql_scripts(filename, cursor):
    with open(filename, 'r') as file:
        sql_script = file.read()
    cursor.execute(sql_script)


def migrate():
    print(f"Attempting to connect to database '{DB_DATABASE}' at host '{DB_HOST}'...")
    connection = None
    try:
        connection = psycopg2.connect(
            dbname=DB_DATABASE,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
        cursor = connection.cursor()
        run_sql_scripts('database/scripts/migration.sql', cursor)
        connection.commit()
        print("Schema created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            connection.close()
            print("Database connection closed.")


if __name__ == "__main__":
    migrate()
