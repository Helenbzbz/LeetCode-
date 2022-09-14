# Write your MySQL query statement below
select
    name
from Employee e
join (select managerID, count(*) as count_id
from Employee group by 1) m
on e.id = m.managerID
where count_id >= 5
