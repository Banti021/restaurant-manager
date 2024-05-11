-- Seed dishes
INSERT INTO dishes (name, price, dish_of_the_day) VALUES
('Spaghetti Carbonara', 12.50, FALSE),
('Pizza Margherita', 10.00, FALSE),
('Lasagna', 15.00, FALSE),
('Tiramisu', 6.00, FALSE);

-- Seed drinks
INSERT INTO drinks (name, price, alcohol_content) VALUES
('Water', 1.50, 0),
('Coke', 2.00, 0),
('Beer', 3.00, 5.0),
('Wine', 5.00, 12.0),
('Mojito', 7.00, 10.0),
('Margarita', 8.00, 15.0);

-- Seed orders
INSERT INTO orders (customer, total, status) VALUES
('Alice', 0.00, 'open'),
('Bob', 0.00, 'open'),
('Charlie', 0.00, 'open'),
('David', 0.00, 'open'),
('Eve', 0.00, 'open'),
('Frank', 0.00, 'open'),
('Grace', 0.00, 'open'),
('Heidi', 0.00, 'open'),
('Ivan', 0.00, 'open'),
('Judy', 0.00, 'open');

-- Seed inventory
INSERT INTO inventory (name, quantity, unit) VALUES
('Spaghetti', 100, 'PCS'),
('Tomato Sauce', 100, 'PCS'),
('Eggs', 100, 'PCS'),
('Pasta', 100, 'PCS'),
('Flour', 100, 'PCS'),
('Mozzarella', 100, 'PCS'),
('Basil', 100, 'PCS'),
('Beef', 100, 'PCS'),
('Pork', 100, 'PCS'),
('Chicken', 100, 'PCS'),
('Milk', 100, 'PCS'),
('Sugar', 100, 'PCS'),
('Coffee', 100, 'PCS'),
('Tea', 100, 'PCS'),
('Lemon', 100, 'PCS'),
('Mint', 100, 'PCS'),
('Rum', 100, 'PCS'),
('Vodka', 100, 'PCS'),
('Gin', 100, 'PCS'),
('Lime', 100, 'PCS');

-- Seed order_dishes
INSERT INTO order_dishes (order_id, dish_id, quantity) VALUES
(1, 1, 1),
(1, 2, 1),
(1, 3, 1),
(1, 4, 1),
(2, 1, 1),
(2, 2, 1),
(2, 3, 1),
(2, 4, 1),
(3, 1, 1),
(3, 2, 1),
(3, 3, 1),
(3, 4, 1),
(4, 1, 1),
(4, 2, 1),
(4, 3, 1),
(4, 4, 1);

-- Seed order_drinks
INSERT INTO order_drinks (order_id, drink_id, quantity) VALUES
(1, 1, 1),
(1, 2, 1),
(1, 3, 1),
(1, 4, 1),
(2, 1, 1),
(2, 2, 1),
(2, 3, 1),
(2, 4, 1),
(3, 1, 1),
(3, 2, 1),
(3, 3, 1),
(3, 4, 1),
(4, 1, 1),
(4, 2, 1),
(4, 3, 1),
(4, 4, 1);