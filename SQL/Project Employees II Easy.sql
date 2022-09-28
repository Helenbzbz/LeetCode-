# Write your MySQL query statement below
with counted as (select
     project_id,
     count(employee_id) as project_size 
     from Project group by 1)

select
    project_id
from counted
where project_size = (select max(project_size) from counted)
