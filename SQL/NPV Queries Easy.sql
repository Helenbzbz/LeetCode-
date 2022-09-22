# Write your MySQL query statement below
select
    q.id,
    q.year,
    if (npv is null, 0, npv) as npv
from Queries q left join NPV n on n.id = q.id
and n.year = q.year
