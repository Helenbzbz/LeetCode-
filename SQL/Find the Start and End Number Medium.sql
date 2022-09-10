# Write your MySQL query statement below
select
    min(log_id) as start_id,
    max(log_id) as end_id
from (select
    log_id,
    rank()over(order by log_id) as rank_id
from Logs) as log_rank
group by (log_id - rank_id)
