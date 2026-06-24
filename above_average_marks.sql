SELECT *
FROM Children
WHERE marks >
(
    SELECT AVG(marks)
    FROM Children
);