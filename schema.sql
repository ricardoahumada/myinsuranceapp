DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP ,
    fullname TEXT NOT NULL,
    email TEXT NOT NULL,
    birthdate TIMESTAMP ,
    country TEXT ,
    city TEXT ,
    adress TEXT 
);