SELECT
    COUNT(*) AS Total_Students,
    AVG(marks) AS Average_Marks,
    MIN(marks) AS Lowest_Marks,
    MAX(marks) AS Highest_Marks,
    SUM(marks) AS Total_Marks
FROM School;