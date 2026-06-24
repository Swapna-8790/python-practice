CREATE TABLE Orderss (
    id INTEGER,
    status TEXT DEFAULT 'Pending'
);

INSERT INTO Orderss(id)
VALUES (1);

SELECT * FROM Orderss;