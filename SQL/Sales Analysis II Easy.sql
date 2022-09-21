# Write your MySQL query statement below
select
    distinct buyer_id
from Sales
where buyer_id not in (select buyer_id from Sales s join Product p on s.product_id = p.product_id where product_name = 'iPhone')
and buyer_id in (select buyer_id from Sales s join Product p on s.product_id = p.product_id where product_name = 'S8')
