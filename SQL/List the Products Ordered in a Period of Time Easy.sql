# Write your MySQL query statement below
select
    product_name,
    sum(unit) as unit
from Orders o
join Products p
on o.product_id = p.product_id
where order_date > '2020-01-31'
and order_date < '2020-03-01'
group by 1
having sum(unit) >=100
