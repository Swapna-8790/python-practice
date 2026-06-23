SELECT
    genre,
    COUNT(*) AS Total_Movies,
    AVG(rating) AS Average_Rating,
    MIN(rating) AS Lowest_Rating,
    MAX(rating) AS Highest_Rating
FROM Movies
GROUP BY genre;