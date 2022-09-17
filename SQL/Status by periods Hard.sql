# Takeaway Learn how to use the date_add or date_diff funtion
# Date_add or Date_diff(timestamp, interval x day)
# Write your MySQL query statement below
with states as (select
    "succeeded" as states,
    success_date as dates
from Succeeded
where success_date between '2019-01-01' and '2019-12-31'
union
select
    "failed" as states,
    fail_date as dates
from Failed
where fail_date between '2019-01-01' and '2019-12-31')

,start_date as (
 select
    period_state,
    start_date,
    row_number() over(order by start_date asc) as row_num from
(
select
    states as period_state,
    dates as start_date
from states
where dates = (select min(dates) from states)  
union
    select
    a.states as period_state,
    a.dates as start_date
from states a 
join states b on a.dates = Date_add(b.dates, interval 1 day)
where a.states != b.states) as start_date)

,end_date as (select
    end_date,
    row_number() over (order by end_date asc) as row_num from 
(select
    dates as end_date
from states
where dates = (select max(dates) from states)
union
select
    a.dates as end_date
from states a join states c on c.dates = Date_add(a.dates, interval 1 day)
where c.states != a.states) as end_rank)
                
select
    period_state,
    start_date,
    end_date
from start_date sd join end_date ed
on sd.row_num = ed.row_num
