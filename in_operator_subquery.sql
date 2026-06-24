CREATE TABLE TopChildren(
     id INTEGER
);
INSERT INTO TopChildren VALUES
(1),
(4);

SELECT *
FROM Children
WHERE id IN
(
    SELECT id
    FROM TopChildren
);