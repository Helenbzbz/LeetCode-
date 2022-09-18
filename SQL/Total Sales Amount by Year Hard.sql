# Write your MySQL query statement below
# My thought is to first process Sales table so that we get by product_id, by year's total sale; Recursion allows to select the select within this select

# Bascially this generates all the date form the earliest start to the latest end
WITH RECURSIVE CTE AS(
SELECT MIN(period_start) as date
     FROM Sales 
     UNION all
     SELECT DATE_ADD(date, INTERVAL 1 day)
     FROM CTE
     WHERE date <= all(SELECT MAX(period_end) FROM Sales))

 
select
    p.product_id,
    product_name,
    left(date,4) as report_year,
    sum(average_daily_sales) as total_amount
from Sales s
join CTE on s.period_start <= date
and s.period_end >= date
join Product p on s.product_id = p.product_id
group by 1,2,3
order by 1,3
