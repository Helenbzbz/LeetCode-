# Write your MySQL query statement below
## Moving Average problem
## Row function, added in the aggregation function to specify certain number of rows before or between x rows preceding and the current row
## Order by & limit n,n -> to remove n numbers of entries from the beginning
## If we use range instead of row, two entries on one date will both be included

SELECT 
    distinct visited_on, 
    SUM(amount) OVER(ORDER BY visited_on RANGE BETWEEN interval 6 day PRECEDING AND current row) AS amount,
    ROUND(SUM(amount)OVER(order by visited_on range between interval 6 day preceding and current row)/7,2) as average_amount
FROM Customer
limit 6, 1000
