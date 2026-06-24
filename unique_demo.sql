CREATE TABLE Users (
    id INTEGER,
    email TEXT UNIQUE
);

INSERT INTO Users VALUES
(1,'ravi@gmail.com');

SELECT * FROM Users;