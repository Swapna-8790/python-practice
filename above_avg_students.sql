SELECT *
FROM School
WHERE marks >
(
    SELECT AVG(marks)
    FROM School
);