SELECT
    genre,
    MAX(rating) AS Highest_Rating
FROM Movies
GROUP BY genre;