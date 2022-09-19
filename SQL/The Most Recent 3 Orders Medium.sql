# Write your MySQL query statement below
select
    name as customer_name,
    c.customer_id,
    order_id,
    order_date
from 
Customers c join (select
    rank()over(partition by customer_id order by order_date desc) as latest,
    order_date,
    customer_id,
    order_id
from Orders) r
on c.customer_id = r.customer_id
where latest <= 3
order by 1,2,4 desc
