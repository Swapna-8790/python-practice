DROP TABLE Child;
CREATE TABLE Child (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
);

INSERT INTO Child VALUES
(1,'Ravi',85),
(2,'Anu',90);

SELECT * FROM Child;