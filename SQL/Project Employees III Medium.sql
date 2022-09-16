# Write your MySQL query statement below
select project_id, employee_id from
(select
    rank() over (partition by project_id order by experience_years desc) as rank_id,
    project_id,
    e.employee_id
from Employee e join Project p on p.employee_id = e.employee_id) as ranked
where rank_id = 1
