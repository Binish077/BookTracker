DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS users;

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    beginDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    thoughts TEXT NOT NULL,
    pageNumber INTEGER
);

CREATE TABLE users (
    email TEXT NOT NULL,
    userName TEXT NOT NULL,
    userPassword TEXT NOT NULL
);
