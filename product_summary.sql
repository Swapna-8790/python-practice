SELECT
    COUNT(*) AS Total_Things,
    AVG(price) AS Average_Price,
    MAX(price) AS Highest_Price,
    MIN(price) AS Lowest_Price
FROM Things;