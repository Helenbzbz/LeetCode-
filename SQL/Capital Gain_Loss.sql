# Write your MySQL query statement below
# We don't need a subquery here we can use sum case to make the query faster
# select
#     stock_name,
#     sum(capital) as capital_gain_loss
# from
# (select
#     stock_name,
#     case when operation = 'Buy' then -price
#     when operation = 'Sell' then price
#     end as capital
# from Stocks) as capital
# group by 1

## In SQL we need to keep function close to the parenthesis
select
stock_name,
sum(case 
when operation = 'Buy' then -price
when operation = 'Sell' then price end)
as capital_gain_loss
from Stocks
group by 1
