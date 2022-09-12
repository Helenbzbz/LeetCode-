# Write your MySQL query statement below
# The issue of this code is if the player continously login in the future they are recalcualted multiple times

with first_install as (select 
    min(event_date) as install_dt,
    player_id
from Activity
group by 2),

retention as (select 
    date_add(install_dt, interval 1 day) as next_date, 
    a.player_id
from Activity a
inner join first_install b 
on a.player_id = b.player_id
where a.event_date = date_add(install_dt, interval 1 day))
              
select
    install_dt, 
    count(i.player_id) as installs, 
    round(avg((case when next_date is null then 0 else 1 end)), 2) as Day1_retention
from first_install i left join retention r
on i.player_id = r.player_id
group by 1
