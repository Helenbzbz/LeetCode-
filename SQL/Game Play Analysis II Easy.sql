# Write your MySQL query statement below
with first_login as (select
    player_id,
    device_id,
    rank() over (partition by player_id order by event_date) as rank_id
from Activity)

select player_id, device_id
from first_login
where rank_id = 1

