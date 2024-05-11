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

print(f"Attempting to connect to database '{DB_DATABASE}' at host '{DB_HOST}'...")


def create_schema():
    connection = None
    try:
        # Connect to the database
        connection = psycopg2.connect(
            dbname=DB_DATABASE,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
        print("Connected to the database successfully.")
        cursor = connection.cursor()

        # Define the SQL statements to create the tables
        create_tables_sql = [
            """
            CREATE TABLE IF NOT EXISTS dishes (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                price DECIMAL(6,2) NOT NULL,
                dish_of_the_day BOOLEAN DEFAULT FALSE
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS drinks (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                price DECIMAL(6,2) NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS orders (
                id SERIAL PRIMARY KEY,
                customer VARCHAR(255) NOT NULL,
                total DECIMAL(10,2) NOT NULL,
                status VARCHAR(50) DEFAULT 'open'
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS inventory (
                item_id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                quantity INT NOT NULL,
                unit VARCHAR(50) NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS order_dishes (
                order_id INT,
                dish_id INT,
                quantity INT DEFAULT 1,
                PRIMARY KEY (order_id, dish_id),
                FOREIGN KEY (order_id) REFERENCES orders(id),
                FOREIGN KEY (dish_id) REFERENCES dishes(id)
              );
            """,
            """
            CREATE TABLE IF NOT EXISTS order_drinks (
                order_id INT,
                drink_id INT,
                quantity INT DEFAULT 1,
                PRIMARY KEY (order_id, drink_id),
                FOREIGN KEY (order_id) REFERENCES orders(id),
                FOREIGN KEY (drink_id) REFERENCES drinks(id)
            );
            """,
            """
               CREATE TABLE IF NOT EXISTS sales_reports (
                   report_id SERIAL PRIMARY KEY,
                   date DATE NOT NULL,
                   total_sales NUMERIC(10,2) NOT NULL,
                   total_orders INT NOT NULL
               );
           """
        ]

        # Execute the SQL statements
        for query in create_tables_sql:
            cursor.execute(query)
            print(f"Executed query: {query}")

        # Commit the changes
        connection.commit()
        print("Schema created successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if connection:
            connection.close()
            print("Database connection closed.")


if __name__ == "__main__":
    create_schema()
