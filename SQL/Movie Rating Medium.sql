# Write your MySQL query statement below
# with rank_by_name as (
with total_movie as (select
    user_id,
    count(distinct movie_id) as total_movie
from MovieRating group by 1),

avg_rank as (select
    movie_id,
    avg(rating) as movie_rating
from MovieRating 
where created_at like '2020-02%'
group by 1)

(select
    name as results
from total_movie tm join Users u on u.user_id = tm.user_id 
order by total_movie desc, name asc limit 1)
union
(select
    title as results
from avg_rank ar join Movies m on ar.movie_id = m.movie_id
order by movie_rating desc, title asc limit 1)
