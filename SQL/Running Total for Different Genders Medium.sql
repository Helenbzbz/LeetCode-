# Write your MySQL query statement below
select
    a.gender,
    a.day,
    sum(b.score_points) as total
from Scores a
join Scores b
on a.day >= b.day
and a.gender = b.gender
group by 1,2
order by 1 asc, 2 asc
