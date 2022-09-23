# Write your MySQL query statement below
# Union will eliminate duplicate while union all won't
with scores as (
select 
    host_team as team_id,
    case
    when host_goals > guest_goals then 3
    when host_goals = guest_goals then 1
    else 0
    end as num_points
from Matches
union all
select 
    guest_team as team_id,
    case
    when host_goals < guest_goals then 3
    when host_goals = guest_goals then 1
    else 0
    end as num_points
from Matches)

select
    t.team_id,
    team_name,
    if (sum(num_points) is not null, sum(num_points), 0) as num_points
from teams t left join scores s
on s.team_id = t.team_id
group by 1,2
order by 3 desc, 1 asc
