-- Creating the 'dishes' table
CREATE TABLE IF NOT EXISTS dishes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    price DECIMAL(6,2) NOT NULL,
    dish_of_the_day BOOLEAN DEFAULT FALSE,
    is_deleted BOOLEAN DEFAULT FALSE
);

-- Creating the 'drinks' table
CREATE TABLE IF NOT EXISTS drinks (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    price DECIMAL(6,2) NOT NULL,
    is_alcoholic BOOLEAN DEFAULT FALSE,
    alcohol_content DECIMAL(3,1) DEFAULT 0,
    is_deleted BOOLEAN DEFAULT FALSE
);

-- Creating the 'orders' table
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    customer VARCHAR(255) NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    status INT DEFAULT 0,
    created_at DATE NOT NULL DEFAULT CURRENT_DATE
);

-- Creating the 'order_dishes' table
CREATE TABLE IF NOT EXISTS order_dishes (
    order_id INT,
    dish_id INT,
    quantity INT DEFAULT 1,
    PRIMARY KEY (order_id, dish_id),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (dish_id) REFERENCES dishes(id)
);

-- Creating the 'order_drinks' table
CREATE TABLE IF NOT EXISTS order_drinks (
    order_id INT,
    drink_id INT,
    quantity INT DEFAULT 1,
    PRIMARY KEY (order_id, drink_id),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (drink_id) REFERENCES drinks(id)
);

-- Creating the 'sales_details' table
CREATE TABLE IF NOT EXISTS sales_reports (
    id SERIAL PRIMARY KEY,
    date_from DATE NOT NULL,
    date_to DATE NOT NULL,
    created_at DATE NOT NULL DEFAULT CURRENT_DATE,
    location VARCHAR(255) NOT NULL
);
