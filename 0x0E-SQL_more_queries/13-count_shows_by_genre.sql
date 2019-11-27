-- select cities california
SELECT tv_genres.name AS "genre", count(*) AS "number_of_shows"
FROM tv_show_genres
LEFT JOIN tv_genres
ON tv_genres.id = genre_id
GROUP BY genre_id
ORDER BY count(*) DESC;
