-- Import the database dump from hbtn_0d_tvshows to your MySQL server

SELECT s.title, g.genre_id
FROM tv_shows s
LEFT JOIN tv_show_genres g ON s.id = g.show_id
WHERE g.show_id IS NULL
ORDER BY s.title, g.genre_id;