CREATE TABLE users (
    id INT NOT NULL PRIMARY KEY,
    wp_user_id INT,
    device_id VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE IF NOT EXISTS products (
    id INT PRIMARY KEY,
    wc_product_id INT,
    name VARCHAR(255),
    category VARCHAR(255),
    price DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS user_events (
    id INT PRIMARY KEY,
    user_id INT,
    product_id INT,
    event_type VARCHAR(50),
    value DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);


CREATE TABLE IF NOT EXISTS discount_recommendations (
    id INT PRIMARY KEY,
    product_id INT,
    score DECIMAL(5,2),
    recommended_discount DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id)
);
