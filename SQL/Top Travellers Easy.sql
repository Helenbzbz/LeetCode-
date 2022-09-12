# Write your MySQL query statement below
select
    name,
    if (travelled_distance is not null, travelled_distance, 0)
    as travelled_distance
from
(select
    user_id,
    name,
    sum(distance) as travelled_distance
from Users u
left join Rides r on u.id = r.user_id
group by 1,2
order by 3 desc, 2 asc) as processed
