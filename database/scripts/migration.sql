CREATE TABLE IF NOT EXISTS dishes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    price DECIMAL(6,2) NOT NULL,
    dish_of_the_day BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS drinks (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    price DECIMAL(6,2) NOT NULL,
    alcohol_content DECIMAL(3,1) DEFAULT 0
);

CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    customer VARCHAR(255) NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    status VARCHAR(50) DEFAULT 'open'
);

CREATE TABLE IF NOT EXISTS inventory (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    unit VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS order_dishes (
    order_id INT,
    dish_id INT,
    quantity INT DEFAULT 1,
    PRIMARY KEY (order_id, dish_id),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (dish_id) REFERENCES dishes(id)
);

CREATE TABLE IF NOT EXISTS order_drinks (
    order_id INT,
    drink_id INT,
    quantity INT DEFAULT 1,
    PRIMARY KEY (order_id, drink_id),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (drink_id) REFERENCES drinks(id)
);