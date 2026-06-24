SELECT
    Section,
    COUNT(*) AS Students,
    AVG(marks) AS Average_Marks
FROM School
GROUP BY Section;

