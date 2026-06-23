SELECT
    COUNT(*) AS Total_Students,
    SUM(marks) AS Total_Marks,
    AVG(marks) AS Average_Marks,
    MIN(marks) AS Lowest_Marks,
    MAX(marks) AS Highest_Marks
FROM Students;