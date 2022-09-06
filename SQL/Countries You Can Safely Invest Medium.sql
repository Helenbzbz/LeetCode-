# Write your MySQL query statement below
with people_country as (
select
    id as user_id,
    c.name as country
from Person as p
join Country c on substr(p.phone_number, 1,3) = c.country_code)

select country
from people_country as cp
join Calls as c on user_id = caller_id or user_id = callee_id
group by 1
having avg(duration) > (select avg(duration) from Calls)

## Can also USE UNION to combine results from two select
with total_duration as (
select caller_id as user_id, duration
from Calls
Union All
select callee_id as user_id, duration
from Calls),

people_country as (
select
    id as user_id,
    c.name as country
from Person as p
join Country c on substr(p.phone_number, 1,3) = c.country_code)

select
    country
from people_country as pc
join total_duration as td on td.user_id = pc.user_id
group by 1
having avg(duration) > (select avg(duration) from Calls)
