-- 1. In and not out 
-- creates a table users
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT, 
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL,
    PRIMARY KEY (id)
);
