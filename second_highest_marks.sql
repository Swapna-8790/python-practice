SELECT MAX(marks)
FROM Children
WHERE marks <
(
    SELECT MAX(marks)
    FROM Children
);