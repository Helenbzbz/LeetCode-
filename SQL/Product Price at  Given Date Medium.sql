# Write your MySQL query statement below
with cte as (
	select max(change_date) as dat, product_id
	from Products
	where change_date <= '2019-08-16'
	group by product_id)

select t.product_id, 
case when new_price is null then 10 else new_price end as price       
from (select distinct product_id from Products) as t 
left join cte c on t.product_id=c.product_id 
left join Products p on p.product_id=c.product_id and p.change_date=c.dat
