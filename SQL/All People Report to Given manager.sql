# Write your MySQL query statement below
with reports as (select
    a.employee_id,
    a.manager_id as 1st,
    b.manager_id as 2nd,
    c.manager_id as 3rd
from Employees as a
left join Employees as b on a.manager_id = b.employee_id
left join Employees as c on b.manager_id = c.employee_id)

select
    employee_id
from reports
where employee_id != 1
and (1st = 1 or 2nd =1 or 3rd = 1)
