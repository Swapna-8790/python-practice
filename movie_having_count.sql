SELECT
    genre,
    COUNT(*) AS Total_Movies
FROM Movies
GROUP BY genre
HAVING COUNT(*) > 1;