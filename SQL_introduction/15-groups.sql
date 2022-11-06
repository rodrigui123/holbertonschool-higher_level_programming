-- lists the number of records with the same score in second_table
SELECT score, COUNT(score) as 'number'
FROM second_table
GROUP BY score
ORDER BY number DESC
