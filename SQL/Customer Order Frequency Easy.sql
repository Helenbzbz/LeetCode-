# Write your MySQL query statement below
with month_customer as (
    select
    c.customer_id,
    name,
    date_format(order_date,'%Y-%m') as purchase_month,
    sum(price*quantity) as paid
from Customers c
join Orders o on o.customer_id = c.customer_id
join Product p on p.product_id = o.product_id
where date_format(order_date,'%Y-%m') in ('2020-06','2020-07')
group by 1,2,3)

select
    customer_id,
    name
from
(select
    count(purchase_month) as month_count,
    customer_id,
    name
from month_customer
where paid >= 100
group by 2,3) as month_count
where month_count =2

## That is really slow we can solve this without subquery
SELECT 
    customer_id,
    name
FROM Customers 
JOIN Orders USING(customer_id) 
JOIN Product USING(product_id)
GROUP BY customer_id
HAVING SUM(IF(MONTH(order_date) = 6, quantity, 0) * price) >= 100 AND 
    SUM(IF(MONTH(order_date) = 7, quantity, 0) * price) >= 100;
