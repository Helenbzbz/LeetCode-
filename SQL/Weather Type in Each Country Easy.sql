# Write your MySQL query statement below
select
    country_name,
    case
    when avg(weather_state) <=15 then 'Cold'
    when avg(weather_state) >= 25 then 'Hot'
    else 'Warm'
    end as weather_type
from Countries c
join Weather w on c.country_id = w.country_id
where day < '2019-12-01'
and day > '2019-10-31'
group by 1
