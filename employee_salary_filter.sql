CREATE TABLE Employee (
    id INTEGER,
    name TEXT,
    salary INTEGER
);

INSERT INTO Employee
VALUES (1,'John',30000);

INSERT INTO Employee
VALUES (2,'Sara',50000);

INSERT INTO Employee
VALUES (3,'David',45000);

SELECT *
FROM Employee
WHERE salary>40000
ORDER BY salary DESC;

