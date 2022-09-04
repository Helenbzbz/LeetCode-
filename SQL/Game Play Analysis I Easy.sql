with rank_table as (select
    player_id,
    event_date,
    rank() over (partition by player_id order by event_date) as rank_id
    from Activity)
    select player_id, event_date as first_login
    from rank_table
    where rank_id = 1
     
select
    player_id,
    min(event_date) as first_login
from Activity
group by player_id
     
