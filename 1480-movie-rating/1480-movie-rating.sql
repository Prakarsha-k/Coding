# Write your MySQL query statement below

-- Step 1: Find the user who rated the most movies
WITH user_count AS (
    SELECT u.name,
           COUNT(*) AS total_ratings
    FROM MovieRating mr
    JOIN Users u ON mr.user_id = u.user_id
    GROUP BY u.name
    ORDER BY total_ratings DESC, u.name ASC
    LIMIT 1
),

-- Step 2: Find the movie with highest average rating in February 2020
movie_avg AS (
    SELECT m.title,
           AVG(mr.rating) AS avg_rating
    FROM MovieRating mr
    JOIN Movies m ON mr.movie_id = m.movie_id
    WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY m.title
    ORDER BY avg_rating DESC, m.title ASC
    LIMIT 1
)

-- Step 3: Combine both results vertically
SELECT name AS results FROM user_count
UNION ALL
SELECT title AS results FROM movie_avg;
