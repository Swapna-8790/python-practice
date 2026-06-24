SELECT *
FROM Children
WHERE marks =
(
    SELECT Round(AVG(marks))
    FROM Children
);