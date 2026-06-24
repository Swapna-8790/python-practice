SELECT *
FROM Children
WHERE marks =
(
    SELECT MIN(marks)
    FROM Children
);