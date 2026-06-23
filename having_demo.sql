SELECT
    genre,
    AVG(rating) AS Average_Rating
FROM Movies
GROUP BY genre
HAVING AVG(rating) > 7;