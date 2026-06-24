CREATE TABLE CustomersInfo (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    email TEXT UNIQUE,
    city TEXT DEFAULT 'Hyderabad'
);

INSERT INTO CustomersInfo
(customer_id, customer_name, email)
VALUES
(1,'Ravi','ravi@gmail.com');

SELECT * FROM CustomersInfo;