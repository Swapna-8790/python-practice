SELECT
    genre,
    SUM(rating) AS Total_Rating
FROM Movies
GROUP BY genre;