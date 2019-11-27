-- select cities california
SELECT a.name
FROM tv_genres a, tv_show_genres b, tv_shows c
WHERE a.id = b.genre_id AND b.show_id = c.id AND c.title = 'Dexter'
ORDER BY a.name ASC;
