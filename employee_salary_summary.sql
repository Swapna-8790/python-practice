SELECT
    COUNT(*) AS Employee,
    SUM(salary) AS Total_Salary,
    AVG(salary) AS Average_Salary,
    MIN(salary) AS Lowest_Salary,
    MAX(salary) AS Highest_Salary
FROM Employee