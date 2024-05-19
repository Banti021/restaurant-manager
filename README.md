
# Restaurant Manager

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PostgreSQL](https://img.shields.io/badge/postgresql-336791?style=for-the-badge&logo=postgresql&logoColor=white)

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [Testing](#testing) 
- [Authors](#authors)
- [Acknowledgements](#acknowledgements)

## Description
Restaurant Manager is a command-line application designed to help restaurant owners efficiently manage their menu, orders and sales reports. Leveraging the power of Python and PostgreSQL, it provides a robust back-end system capable of handling the dynamic needs of a modern restaurant.

## Features

### Menu Management
- Display the entire menu.
- Add or remove dishes and drinks.
- Update existing menu items.
- Set special dishes of the day.

### Order Management
- View and manage open orders.
- Create new orders.
- Update existing orders.
- Cancel orders.

### Sales Reporting
- Generate detailed sales reports for specific days, months, or custom date ranges.
- Export sales reports to PDF for easy sharing and printing.

## Installation
1. Clone the repository:
```
git clone https://github.com/Banti021/restaurant-manager.git
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Create a `.env` file in the root directory and add the following environment variables:
```
DB_HOST=localhost
DB_DATABASE=restaurant
DB_USER=restaurant_manager
DB_PASSWORD=restaurant_password
```
4. Start the application using Docker:
```bash
docker-compose up
```
5. Run the application:
```bash
python main.py
```

## Database Setup
### Using Docker
1. Start the application with Docker Compose (migrations and seeder will automatically run):
```bash
docker-compose up
```

### Manual Setup
1. Install PostgreSQL:
```bash
    brew install postgresql
```
2. Create a database:
```sql
    CREATE DATABASE restaurant_manager;
```
3. Activate the virtual environment:
```bash
    source venv/bin/activate
```
4. Create tables by running the migration script:
```bash
python database/migrations.py
```
5. Seed the database:
```bash
python database/seeder.py
```

## Usage
```bash
python main.py
```
Use the command-line interface to manage your restaurant's menu, orders and generate sales reports.

## Testing
Testing is done using the built-in `unittest` module in Python.
Tests are using separate test database, so you can run them without affecting the main database.
It is done in separate Docker container, so you need to have Docker installed.

### Running the Test Suite
1. Activate the virtual environment:
```bash
source venv/bin/activate
```
2. Run the test suite:
```bash
python -m unittest discover tests
```
3. To run a specific test file:
```bash
python -m unittest tests/test_file.py
```

## Authors
- [Banti021](https://github.com/Banti021)
- [KrzysztofPawl](https://github.com/KrzysztofPawl)


## Acknowledgements
- [Python](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Docker](https://www.docker.com/)
