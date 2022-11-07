-- Import the database dump from hbtn_0d_tvshows to your MySQL server

SELECT g.name AS genre,
       COUNT(*) AS number_of_shows
SELECT FROM tv_genres g
JOIN tv_show_genres sg
ON g.id = sg.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
