CREATE TABLE Customers (
    customer_id INTEGER,
    customer_name TEXT
);

INSERT INTO Customers VALUES
(1,'Ravi'),
(2,'Anu'),
(3,'Rahul');

CREATE TABLE Orders (
    order_id INTEGER,
    customer_id INTEGER,
    amount INTEGER
);

INSERT INTO Orders VALUES
(101,1,500),
(102,2,1000),
(103,1,700);