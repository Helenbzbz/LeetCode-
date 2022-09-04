# Write your MySQL query statement below
with rank_login as (select
    min(event_date) as firstdate,
    player_id
from Activity
group by player_id)
select 
    round(count(rl.player_id)/(select count(distinct player_id) from Activity),2) as fraction
from Activity as act
left join rank_login as rl
on rl.player_id = act.player_id
where act.event_date = rl.firstdate + 1
