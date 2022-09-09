# Write your MySQL query statement below
with rank_table as (
select x,
rank() over (order by x) as rank_id
from Point)

select min(distance) as shortest from(
select abs(a.x-b.x) as distance
    from rank_table a
    join rank_table b on a.rank_id = b.rank_id-1) as distance
