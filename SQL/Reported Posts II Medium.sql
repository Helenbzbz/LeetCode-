# Write your MySQL query statement below
select
    round(avg(percent)*100.00,2) as average_daily_percent
from (select
    count(distinct r.post_id)/count(distinct a.post_id) as percent,
    action_date
from Actions a left join Removals r
on a.post_id = r.post_id
where a.extra = 'spam'
group by 2) as sum_day
