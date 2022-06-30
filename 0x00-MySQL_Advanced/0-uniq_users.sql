-- SQL script that creates a table users

CREATE TABLE IF NOT EXISTS users (
    id NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
