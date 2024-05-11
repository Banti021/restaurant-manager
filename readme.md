# Restaurant Manager

## Description
This is a simple restaurant manager that allows you to add, remove, and update menu items. It also allows you to view the menu and search for items by name or price.

## Available functions 
1. Manage restaurant menu
- Display menu
- Add dish to menu
- Add drink to menu
- Remove dish from menu
- Remove drink from menu
- Update dish
- Update drink
- Set dish of the day
2. Manage orders
- Display open orders
- Add order
- Update order
- Remove order
3. Manage inventory
4. Generate sales report

## Installation
1. Clone the repository
2. Create venv - `python -m venv venv`
3. Activate venv - `source venv/bin/activate`
4. Install requirements - `pip install -r requirements.txt`
5. Run the program - `python main.py`

## Database setup
Install postgresql `brew install postgresql`

Dishes
```
CREATE TABLE dishes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(6,2) NOT NULL,
    dish_of_the_day BOOLEAN DEFAULT FALSE
);
```
Drinks
```
CREATE TABLE drinks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(6,2) NOT NULL
);
```
Orders
```
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer VARCHAR(255) NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    status VARCHAR(50) DEFAULT 'open'
);

```
Inventory
```
CREATE TABLE inventory (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    unit VARCHAR(50) NOT NULL
);
```
Sales reports
```
CREATE TABLE sales_reports (
    report_id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    total_sales DECIMAL(10,2) NOT NULL,
    total_orders INT NOT NULL
);
```