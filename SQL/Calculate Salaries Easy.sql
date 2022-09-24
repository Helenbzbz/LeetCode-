select
    s.company_id,
    employee_id,
    employee_name,
    round(salary*(case
    when maxsalary <1000 then 1
    when maxsalary >=1000 and maxsalary <= 10000 then (1-0.24)
    else (1-0.49) end)) as salary
from (select
    max(salary) as maxsalary, company_id
from Salaries group by 2) as ms
join Salaries s on s.company_id = ms.company_id
