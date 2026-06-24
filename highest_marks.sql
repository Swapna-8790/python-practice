SELECT *
FROM Children
WHERE marks =
(
    SELECT MAX(marks)
    FROM Children
);