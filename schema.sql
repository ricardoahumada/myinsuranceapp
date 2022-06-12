DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP ,
    fullname TEXT NOT NULL,
    email TEXT NOT NULL,
    birthdate TIMESTAMP ,
    country TEXT ,
    city TEXT ,
    address TEXT, 
    password TEXT
);

DROP TABLE IF EXISTS products;

CREATE TABLE products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP ,
    name TEXT ,
    description TEXT,
    cost float ,
    is_active boolean ,
    user INTEGER
);