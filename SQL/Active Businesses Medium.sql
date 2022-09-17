# Write your MySQL query statement below
with occurance as (select
    business_id,
    count(a.event_type) as event_count
from Events a join
(select
    avg(occurences) as avg_occur,
    event_type
from Events
group by 2) as b on a.event_type = b.event_type
where a.occurences > b.avg_occur
group by 1)


select
    business_id
from occurance
where event_count> 1
