# Write your MySQL query statement below
select
    employee_id,
    team_size
from Employee join (select
    team_id, count(employee_id) as team_size 
    from Employee group by 1) as counted
on employee.team_id = counted.team_id
